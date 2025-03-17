import pandas as pd
import numpy as np
import yaml

def group_and_rename_columns(df, column_dict):
    """
    Groups and renames DataFrame columns according to their category.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The input DataFrame to be processed
    column_dict : dict
        Dictionary with category names as keys and lists of column names as values.
        Expected keys: 'sensitive', 'covariate', 'treatment', 'target'
    
    Returns:
    --------
    pandas.DataFrame
        New DataFrame with reordered and renamed columns
    
    Example:
    --------
    column_dict = {
        'sensitive': ['gender', 'race'],
        'covariate': ['age', 'education', 'income'],
        'treatment': ['intervention'],
        'target': ['outcome']
    }
    new_df = group_and_rename_columns(df, column_dict)
    """

    # Create a new empty DataFrame
    new_df = pd.DataFrame()
    
    # Dictionary to map category prefixes
    prefix_map = {
        'sensitive': 's',
        'covariate': 'x',
        'treatment': 'z',
        'target': 'y'
    }
    
    # Process each category
    for category, columns in column_dict.items():
        if category not in prefix_map:
            raise ValueError(f"Unknown category: {category}. Expected categories: {list(prefix_map.keys())}")
        
        # Check if all columns exist in the original DataFrame
        missing_cols = [col for col in columns if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Columns {missing_cols} not found in DataFrame")
        
        # Get the prefix for this category
        prefix = prefix_map[category]
        
        # Add columns to the new DataFrame with renamed columns
        for i, col_name in enumerate(columns, 1):
            new_col_name = f"{prefix}{i}"
            new_df[new_col_name] = df[col_name]
    
    return new_df

def get_features_type_info(df):
    # Create empty lists to store information
    column_names = []
    data_types = []
    unique_counts = []
    
    # Iterate through each column
    for column in df.columns:
        column_names.append(column)
        data_types.append(str(df[column].dtype))
        unique_counts.append(df[column].nunique())
    
    # Create a DataFrame with the analysis
    analysis_df = pd.DataFrame({
        'feature': column_names,
        'data_type': data_types,
        'nunique_values': unique_counts
    })
    
    return analysis_df

def display_dataframe_info(df):
    # Print the shape of the DataFrame
    print(f"DataFrame shape: {df.shape} (rows, columns)")
    
    # Print a separator line
    print("-" * 50)
    
    # Print the first five rows
    print("First 5 rows of the DataFrame:")
    display(df.head())


def calculate_nan_percentage_of_grouped_features(df, yaml_path=None, yaml_string=None):
    """
    Calculate the percentage of missing values for features grouped by categories
    defined in a YAML file.
    
    Parameters:
    df (pandas.DataFrame): The input dataframe
    yaml_path (str, optional): Path to the YAML file with feature definitions
    yaml_string (str, optional): String containing YAML content
    
    Returns:
    pandas.DataFrame: DataFrame with feature names and their missing value percentages
    """
    # Load feature categories from YAML
    if yaml_path:
        with open(yaml_path, 'r') as file:
            yaml_data = yaml.safe_load(file)
    elif yaml_string:
        yaml_data = yaml.safe_load(yaml_string)
    else:
        raise ValueError("Either yaml_path or yaml_string must be provided")
    
    # Extract feature categories from the new structure
    feature_categories = {}
    
    # Handle the new nested structure with fairness category
    if 'dataset' in yaml_data and 'fairness' in yaml_data['dataset']:
        fairness_data = yaml_data['dataset']['fairness']
        for category in ['sensitive', 'covariate', 'treatment', 'target', 'other']:
            if category in fairness_data and 'features' in fairness_data[category]:
                feature_categories[category.capitalize()] = fairness_data[category]['features']
    
    # Total number of rows
    total_rows = len(df)
    
    # Calculate missing values count for each column
    missing_counts = df.isnull().sum()
    
    # Calculate percentage of missing values
    missing_percentages = (missing_counts / total_rows) * 100
    
    # Create a DataFrame with results
    missing_stats = pd.DataFrame({
        'Feature': missing_counts.index,
        'Missing_Count': missing_counts.values,
        'Missing_Percentage': missing_percentages.values
    }).sort_values('Missing_Percentage', ascending=False)
    
    # Create a new column for feature category
    def get_category(feature):
        for category, features in feature_categories.items():
            if feature in features:
                return category
        return 'Uncategorized'
    
    missing_stats['Category'] = missing_stats['Feature'].apply(get_category)
    
    # Filter out 'Uncategorized' category features if requested
    # By default, include only the categorized features
    missing_stats = missing_stats[missing_stats['Category'] != 'Uncategorized']
    
    # Reorder columns to put Category first
    missing_stats = missing_stats[['Category', 'Feature', 'Missing_Count', 'Missing_Percentage']]
    
    # Sort by Category and Missing_Percentage
    missing_stats = missing_stats.sort_values(['Category', 'Missing_Percentage'], ascending=[True, False])
    
    return missing_stats