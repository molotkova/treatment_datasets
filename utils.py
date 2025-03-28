import pandas as pd
import numpy as np
import yaml


def create_yaml_structure(df, fairness_dict, structural_dict, name):
    """
    Creates a YAML-compatible dictionary structure for a dataset with fairness and structural information,
    using feature indexes instead of names. Features not in the provided dictionaries are ignored with warnings.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The dataframe containing the dataset
    fairness_dict : dict
        Dictionary with keys 'sensitive', 'covariate', 'treatment', 'target' 
        and lists of feature names as values
    structural_dict : dict
        Dictionary with keys 'categorical', 'numerical' and lists of feature names as values
    
    Returns:
    --------
    dict
        A nested dictionary structure suitable for YAML export, with feature indexes
    """
    # Create a mapping from feature names to their column indexes
    feature_to_index = {name: idx for idx, name in enumerate(df.columns)}
    
    # Collect feature names in each taxonomy
    fairness_features = set()
    for features_list in fairness_dict.values():
        fairness_features.update(features_list)
    
    structural_features = set()
    for features_list in structural_dict.values():
        structural_features.update(features_list)
    
    # Identify features excluded from each taxonomy
    features_excluded_from_fairness = [feat for feat in df.columns if feat not in fairness_features]
    features_excluded_from_structural = [feat for feat in df.columns if feat not in structural_features]
    
    # Identify features not in either taxonomy
    features_completely_ignored = [feat for feat in df.columns if feat not in fairness_features and feat not in structural_features]
    
    # Print appropriate warnings
    if features_excluded_from_structural and not all(f in fairness_features for f in features_excluded_from_structural):
        print(f"Warning: The following features of dataframe are not in the dictionary and will be excluded from structural taxonomy in YAML: {features_excluded_from_structural}")
    
    if features_excluded_from_fairness and not all(f in structural_features for f in features_excluded_from_fairness):
        print(f"Warning: The following features of dataframe are not in the dictionary and will be excluded from fairness taxonomy in YAML: {features_excluded_from_fairness}")
    
    if features_completely_ignored:
        print(f"Warning: The following features of dataframe are not in any of the dictionaries and will be completely ignored in YAML: {features_completely_ignored}")
    
    # Initialize the YAML structure
    yaml_structure = {
        "dataset": {
            "name": name,  
            "n_samples": len(df),
            "structural": {
                "numerical": {
                    "num": 0,
                    "features": []
                },
                "categorical": {
                    "num": 0,
                    "features": []
                }
            },
            "fairness": {
                "sensitive": {
                    "num": 0,
                    "features": []
                },
                "covariate": {
                    "num": 0,
                    "features": []
                },
                "treatment": {
                    "num": 0,
                    "features": []
                },
                "target": {
                    "num": 0,
                    "features": []
                }
            }
        }
    }
    
    # Fill the structural section with indices
    for structure_type, features in structural_dict.items():
        # Filter to only include features that exist in the dataframe and convert to indices
        valid_indices = [feature_to_index[feat] for feat in features if feat in df.columns]
        yaml_structure["dataset"]["structural"][structure_type]["features"] = valid_indices
        yaml_structure["dataset"]["structural"][structure_type]["num"] = len(valid_indices)
    
    # Fill the fairness section with indices
    for fairness_type, features in fairness_dict.items():
        # Filter to only include features that exist in the dataframe and convert to indices
        valid_features = [feat for feat in features if feat in df.columns]
        valid_indices = [feature_to_index[feat] for feat in valid_features]
        yaml_structure["dataset"]["fairness"][fairness_type]["features"] = valid_indices
        yaml_structure["dataset"]["fairness"][fairness_type]["num"] = len(valid_indices)
    
    return yaml_structure


def reorder_columns_by_dict(df, feature_dict):
    """
    Reorders the columns of a dataframe based on the order of values in a dictionary.
    Columns not found in the dictionary will be ignored.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The dataframe to reorder
    feature_dict : dict
        Dictionary where values are lists of column names
    
    Returns:
    --------
    pandas.DataFrame
        Dataframe with columns reordered according to the feature_dict
    """
    # Flatten the dictionary values into a single ordered list
    ordered_columns = []
    for category in feature_dict.values():
        ordered_columns.extend(category)
    
    # Check if all columns in ordered_columns exist in df
    missing_columns = [col for col in ordered_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Columns not found in dataframe: {missing_columns}")
    
    # Identify columns in df that are not in ordered_columns
    extra_columns = [col for col in df.columns if col not in ordered_columns]
    if extra_columns:
        print(f"Warning: The following columns of dataframe were not in the dictionary and will be ignored: {extra_columns}")
    
    # Return the dataframe with only the columns that are in the dictionary, in the specified order
    # Filter out columns that don't exist in the dataframe
    valid_columns = [col for col in ordered_columns if col in df.columns]
    
    return df[valid_columns]

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
    df.replace('?', pd.NA, inplace=True)
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


def get_numerical_features(df, yaml_path=None, yaml_string=None):
    """
    Get numerical features from a YAML file.
    
    Parameters:
    yaml_path (str, optional): Path to the YAML file with feature definitions
    yaml_string (str, optional): String containing YAML content
    
    Returns:
    list: List of numerical feature names
    """
    # Load feature categories from YAML
    if yaml_path:
        with open(yaml_path, 'r') as file:
            yaml_data = yaml.safe_load(file)
    elif yaml_string:
        yaml_data = yaml.safe_load(yaml_string)
    else:
        raise ValueError("Either yaml_path or yaml_string must be provided")
    
    # Extract numerical features from the new structure
    numerical_features = []
    if 'dataset' in yaml_data and 'structural' in yaml_data['dataset']:
        structural_data = yaml_data['dataset']['structural']
        if 'numerical' in structural_data and 'features' in structural_data['numerical']:
            numerical_features = structural_data['numerical']['features']
    
    # Filter out numerical features that do not exist in the DataFrame
    numerical_features = [feature for feature in numerical_features if feature in df.columns]
    
    return numerical_features


def get_categorical_features(df, yaml_path=None, yaml_string=None):
    """
    Get categorical features from a YAML file.
    
    Parameters:
    yaml_path (str, optional): Path to the YAML file with feature definitions
    yaml_string (str, optional): String containing YAML content
    
    Returns:
    list: List of categorical feature names
    """
    # Load feature categories from YAML
    if yaml_path:
        with open(yaml_path, 'r') as file:
            yaml_data = yaml.safe_load(file)
    elif yaml_string:
        yaml_data = yaml.safe_load(yaml_string)
    else:
        raise ValueError("Either yaml_path or yaml_string must be provided")
    
    # Extract categorical features from the new structure
    categorical_features = []
    if 'dataset' in yaml_data and 'structural' in yaml_data['dataset']:
        structural_data = yaml_data['dataset']['structural']
        if 'categorical' in structural_data and 'features' in structural_data['categorical']:
            categorical_features = structural_data['categorical']['features']
    
    # Filter out categorical features that do not exist in the DataFrame
    categorical_features = [feature for feature in categorical_features if feature in df.columns]
    
    return categorical_features

def get_sensitive_features(yaml_path=None, yaml_string=None):
    """
    Get sensitive features from a YAML file.
    
    Parameters:
    yaml_path (str, optional): Path to the YAML file with feature definitions
    yaml_string (str, optional): String containing YAML content
    
    Returns:
    list: List of sensitive feature names
    """
    # Load feature categories from YAML
    if yaml_path:
        with open(yaml_path, 'r') as file:
            yaml_data = yaml.safe_load(file)
    elif yaml_string:
        yaml_data = yaml.safe_load(yaml_string)
    else:
        raise ValueError("Either yaml_path or yaml_string must be provided")
    
    # Extract sensitive features from the new structure
    sensitive_features = []
    if 'dataset' in yaml_data and 'fairness' in yaml_data['dataset']:
        fairness_data = yaml_data['dataset']['fairness']
        if 'sensitive' in fairness_data and 'features' in fairness_data['sensitive']:
            sensitive_features = fairness_data['sensitive']['features']
    
    return sensitive_features

def get_covariate_features(yaml_path=None, yaml_string=None):
    """
    Get covariate features from a YAML file.
    
    Parameters:
    yaml_path (str, optional): Path to the YAML file with feature definitions
    yaml_string (str, optional): String containing YAML content
    
    Returns:
    list: List of covariate feature names
    """
    # Load feature categories from YAML
    if yaml_path:
        with open(yaml_path, 'r') as file:
            yaml_data = yaml.safe_load(file)
    elif yaml_string:
        yaml_data = yaml.safe_load(yaml_string)
    else:
        raise ValueError("Either yaml_path or yaml_string must be provided")
    
    # Extract covariate features from the new structure
    covariate_features = []
    if 'dataset' in yaml_data and 'fairness' in yaml_data['dataset']:
        fairness_data = yaml_data['dataset']['fairness']
        if 'covariate' in fairness_data and 'features' in fairness_data['covariate']:
            covariate_features = fairness_data['covariate']['features']
    
    return covariate_features

def get_treatment_features(yaml_path=None, yaml_string=None):
    """
    Get treatment features from a YAML file.
    
    Parameters:
    yaml_path (str, optional): Path to the YAML file with feature definitions
    yaml_string (str, optional): String containing YAML content
    
    Returns:
    list: List of treatment feature names
    """
    # Load feature categories from YAML
    if yaml_path:
        with open(yaml_path, 'r') as file:
            yaml_data = yaml.safe_load(file)
    elif yaml_string:
        yaml_data = yaml.safe_load(yaml_string)
    else:
        raise ValueError("Either yaml_path or yaml_string must be provided")
    
    # Extract treatment features from the new structure
    treatment_features = []
    if 'dataset' in yaml_data and 'fairness' in yaml_data['dataset']:
        fairness_data = yaml_data['dataset']['fairness']
        if 'treatment' in fairness_data and 'features' in fairness_data['treatment']:
            treatment_features = fairness_data['treatment']['features']
    
    return treatment_features

def get_target_features(yaml_path=None, yaml_string=None):
    """
    Get target features from a YAML file.
    
    Parameters:
    yaml_path (str, optional): Path to the YAML file with feature definitions
    yaml_string (str, optional): String containing YAML content
    
    Returns:
    list: List of target feature names
    """
    # Load feature categories from YAML
    if yaml_path:
        with open(yaml_path, 'r') as file:
            yaml_data = yaml.safe_load(file)
    elif yaml_string:
        yaml_data = yaml.safe_load(yaml_string)
    else:
        raise ValueError("Either yaml_path or yaml_string must be provided")
    
    # Extract target features from the new structure
    target_features = []
    if 'dataset' in yaml_data and 'fairness' in yaml_data['dataset']:
        fairness_data = yaml_data['dataset']['fairness']
        if 'target' in fairness_data and 'features' in fairness_data['target']:
            target_features = fairness_data['target']['features']
    
    return target_features


def map_icd9_category(code):
    """
    Maps an ICD-9 diagnosis code to a broader category.
    For more information on ICD-9 codes, see: https://en.wikipedia.org/wiki/List_of_ICD-9_codes
    """
    if pd.isna(code) or code == "?":
        return "Unknown"
    
    try:
        code = str(code)
        if "." in code:
            code = code.split(".")[0]  # Remove decimal part
        code = int(code)  # Convert to integer
    except ValueError:
        return "Other"
    
    if 1 <= code <= 139:
        return "Infectious Diseases"
    elif 140 <= code <= 239:
        return "Neoplasms (Cancer)"
    elif code == 250:
        return "Diabetes"
    elif 240 <= code <= 279:
        return "Endocrine, Metabolic, and Nutritional Diseases"
    elif 280 <= code <= 289:
        return "Blood Diseases"
    elif 290 <= code <= 319:
        return "Mental Disorders"
    elif 320 <= code <= 389:
        return "Nervous System Disorders"
    elif 390 <= code <= 459:
        return "Circulatory System Diseases"
    elif 460 <= code <= 519:
        return "Respiratory Diseases"
    elif 520 <= code <= 579:
        return "Digestive System Diseases"
    elif 580 <= code <= 629:
        return "Genitourinary Diseases"
    elif 630 <= code <= 679:
        return "Pregnancy-related Conditions"
    elif 680 <= code <= 709:
        return "Skin Diseases"
    elif 710 <= code <= 739:
        return "Musculoskeletal Disorders"
    elif 740 <= code <= 759:
        return "Congenital Anomalies"
    elif 760 <= code <= 779:
        return "Perinatal Conditions"
    elif 780 <= code <= 799:
        return "Symptoms, Signs, and Ill-defined Conditions"
    elif 800 <= code <= 999:
        return "Injury and Poisoning"
    else:
        return "Other"
    
    
def order_columns(df, yaml_path=None, yaml_string=None):

    if yaml_path:
        with open(yaml_path, 'r') as file:
            yaml_data = yaml.safe_load(file)
    elif yaml_string:
        yaml_data = yaml.safe_load(yaml_string)
    else:
        raise ValueError("Either yaml_path or yaml_string must be provided")
    
    ordered_features = []
    if 'dataset' in yaml_data and 'fairness' in yaml_data['dataset']:
        fairness_data = yaml_data['dataset']['fairness']
        if 'sensitive' in fairness_data and 'features' in fairness_data['sensitive']: 
            ordered_features += [feature for feature in fairness_data['sensitive']['features'] if feature in df.columns]
        if 'covariate' in fairness_data and 'features' in fairness_data['covariate']:    
            ordered_features += [feature for feature in fairness_data['covariate']['features'] if feature in df.columns]
        if 'treatment' in fairness_data and 'features' in fairness_data['treatment']:
            ordered_features += [feature for feature in fairness_data['treatment']['features'] if feature in df.columns]
        if 'target' in fairness_data and 'features' in fairness_data['target']:    
            ordered_features += [feature for feature in fairness_data['target']['features'] if feature in df.columns]
        if 'other' in fairness_data and 'features' in fairness_data['other']:    
            ordered_features += [feature for feature in fairness_data['other']['features'] if feature in df.columns]

    return ordered_features


def maintain_order_columns(df, original_order, categorical_features):
    new_columns = []
    for col in original_order:
        if col in categorical_features:
            new_columns.extend([c for c in df.columns if c.startswith(col + '_')])
        else:
            new_columns.append(col)

    return df[new_columns]