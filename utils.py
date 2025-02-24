import pandas as pd
import numpy as np

def calculate_missing_values_percentage(df):
    """
    Calculate the percentage of missing values for each feature in the dataset
    
    Parameters:
    df (pandas.DataFrame): The input dataframe
    
    Returns:
    pandas.DataFrame: DataFrame with feature names and their missing value percentages
    """
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
    
    # Group features by their categories
    feature_categories = {
        'Sensitive': ['sex', 'race', 'age', 'age_cat'],
        'Covariate': ['dob', 'juv_fel_count', 'juv_misd_count', 'juv_other_count', 
                     'priors_count', 'priors_count.1', 'name', 'c_offense_date',
                     'r_offense_date', 'vr_offense_date', 'days_b_screening_arrest',
                     'c_days_from_compas'],
        'Treatment': ['decile_score', 'decile_score.1', 'v_decile_score', 'score_text',
                     'v_score_text', 'type_of_assessment', 'v_type_of_assessment',
                     'c_charge_degree', 'c_charge_desc', 'r_charge_degree', 'r_charge_desc',
                     'vr_charge_degree', 'vr_charge_desc'],
        'Target': ['is_recid', 'two_year_recid']
    }
    
    # Create a new column for feature category
    def get_category(feature):
        for category, features in feature_categories.items():
            if feature in features:
                return category
        return 'Other'
    
    missing_stats['Category'] = missing_stats['Feature'].apply(get_category)
    
    # Filter out 'Other' category features that aren't in our specified categories
    missing_stats = missing_stats[missing_stats['Category'] != 'Other']
    
    # Reorder columns to put Category first
    missing_stats = missing_stats[['Category', 'Feature', 'Missing_Count', 'Missing_Percentage']]
    
    # Sort by Category and Missing_Percentage
    missing_stats = missing_stats.sort_values(['Category', 'Missing_Percentage'], ascending=[True, False])
    
    return missing_stats
