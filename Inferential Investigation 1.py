import pandas as pd
import numpy as np
import scipy.stats as st

# Load datasets
df1 = pd.read_csv('selected_males.csv')
df2 = pd.read_csv('selected_females.csv')

# Calculate total sample size
msamplesize = df1['ID'].nunique()
fsamplesize = df2['ID'].nunique()

# Calculate sum of chosen emotions
maleemotionsum = df1[['Goodme', 'Conf']].sum().sum()  
femaleemotionsum = df2[['Goodme', 'Conf']].sum().sum()  

# Calculate mean
malemean = maleemotionsum/msamplesize
femalemean = femaleemotionsum/fsamplesize

# Calculate standard distribution
male_std_goodme = df1['Goodme'].std()
male_std_conf = df1['Conf'].std()

female_std_goodme = df2['Goodme'].std()
female_std_conf = df2['Conf'].std()

# Variances
male_var_goodme = df1['Goodme'].var()
male_var_conf = df1['Conf'].var()

female_var_goodme = df2['Goodme'].var()
female_var_conf = df2['Conf'].var()

# Combined variance (assuming independent columns)
male_combined_var = male_var_goodme + male_var_conf
female_combined_var = female_var_goodme + female_var_conf

# Combined standard deviation
male_combined_std = np.sqrt(male_combined_var)
female_combined_std = np.sqrt(female_combined_var)

print("\nMean values:")
print(f"Male mean: {malemean:.4f}")
print(f"Female mean: {femalemean:.4f}")
 
print("\nStandard deviation values:")
print(f"Male combined std: {male_combined_std:.4f}")
print(f"Female combined std: {female_combined_std:.4f}")

# Two sample t-test
# note the argument equal_var=False, which assumes that two populations do not have equal variance
t_stats, p_val = st.ttest_ind_from_stats(malemean, male_combined_std, msamplesize, femalemean, female_combined_std, fsamplesize, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.2f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.4f" % p_val)

print("\n Conclusion:")
if p_val < 0.05:
    print("\t We reject the null hypothesis.")
else:
    print("\t We accept the null hypothesis.")
    

    
