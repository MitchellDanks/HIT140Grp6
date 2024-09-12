import pandas as pd
import numpy as np
from scipy import stats
 
# Read the CSV files
females_df = pd.read_csv('selected_females.csv')
males_df = pd.read_csv('selected_males.csv')
 
# Combine the dataframes
combined_df = pd.concat([females_df, males_df])
 
# Calculate the combined score of Goodme and Confidence
combined_df['combined_score'] = combined_df['Goodme'] + combined_df['Conf']
 
# Separate males and females
females = combined_df[combined_df['gender'] == 0]['combined_score']
males = combined_df[combined_df['gender'] == 1]['combined_score']
 
# Function to calculate confidence interval
# data represents the combined scores of 'Goodme' and 'Confidence' for either the female group or the male group.
def calculate_ci(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    std_error = stats.sem(data)
   
    if n >= 30:
        # Use z-score for n >= 30
        z_score = stats.norm.ppf((1 + confidence) / 2)
        margin_of_error = z_score * std_error
        ci_lower = mean - margin_of_error
        ci_upper = mean + margin_of_error
        print(f"Using z-score (n >= 30)")
    else:
        # Use t-score for n < 30
        t_score = stats.t.ppf((1 + confidence) / 2, df=n-1) #df = degrees of freedom
        margin_of_error = t_score * std_error
        ci_lower = mean - margin_of_error
        ci_upper = mean + margin_of_error
        print(f"Using t-score (n < 30)")
   
    return mean, (ci_lower, ci_upper)
 
# Calculate confidence intervals for females and males
female_mean, female_ci = calculate_ci(females)
male_mean, male_ci = calculate_ci(males)
 
# Print results
print("\nFemales:")
print(f"Mean: {female_mean:.2f}")
print(f"95% Confidence Interval: ({female_ci[0]:.2f}, {female_ci[1]:.2f})")
 
print("\nMales:")
print(f"Mean: {male_mean:.2f}")
print(f"95% Confidence Interval: ({male_ci[0]:.2f}, {male_ci[1]:.2f})")