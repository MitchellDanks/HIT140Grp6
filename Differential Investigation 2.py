#Descriptive Investigation 2
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt
import statistics as stats
import numpy as np

#Read Relevant Datasets
df1 = pd.read_csv('dataset1.csv')
df3 = pd.read_csv('dataset3.csv')

#Merge Relevant Datasets 
df = df1.merge(df3, on="ID")

#Distribution of Well-Being Scores Across Respondents

#-------------------------------------------------------------------------------------

#Relaxed

print("\nRelaxed Information - All Respondents")
Relx = df['Relx'].values
Relx_mean = stats.mean(Relx)
Relx_median = stats.median(Relx)
Relx_mode = stats.mode(Relx)
Relx_std = st.tstd(Relx)
Relx_IQR25 = int(np.percentile(Relx,25))
Relx_IQR75 = int(np.percentile(Relx,75))
Relx_IQR = Relx_IQR75 - Relx_IQR25
Relx_Variance = Relx_IQR + (Relx_IQR/2)
Relx_Variance_Lower = Relx_IQR25 - Relx_Variance
Relx_Variance_Upper = Relx_IQR75 + Relx_Variance
print("Mean: %.2f \nMedian: %.2f \nMode: %.2f \nStd: %.2f\n25th percentile value: %.2f\n75th percentile value: %.2f\nInterquartile Range: %.2f\nThe Variance: %.2f\nOutliers lay outside: %.2f and %.2f" %(Relx_mean, Relx_median, Relx_mode, Relx_std,Relx_IQR25, Relx_IQR75, Relx_IQR, Relx_Variance, Relx_Variance_Lower,Relx_Variance_Upper))
print('\n')

#Relaxed - All Respondents Histogram
bin_width = 1
mbin_count= ([0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
plt.hist(Relx, color='purple', edgecolor='black', bins=mbin_count)
plt.title("I have been feeling Relaxed - All Respondents")
plt.xticks([1, 2, 3, 4, 5])
plt.xlabel("I have been feeling Relaxed")
plt.ylabel("No. of Respondents")
plt.show()

print("\nRelaxed Information - Male Respondents")
Male_df = df[df['gender']==1]
M_Relx = Male_df['Relx'].values

M_Relx_mean = stats.mean(M_Relx)
M_Relx_median = stats.median(M_Relx)
M_Relx_mode = stats.mode(M_Relx)
M_Relx_std = st.tstd(M_Relx)
M_Relx_IQR25 = int(np.percentile(M_Relx,25))
M_Relx_IQR75 = int(np.percentile(M_Relx,75))
M_Relx_IQR = M_Relx_IQR75 - M_Relx_IQR25
M_Relx_Variance = M_Relx_IQR + (M_Relx_IQR/2)
M_Relx_Variance_Lower = M_Relx_IQR25 - M_Relx_Variance
M_Relx_Variance_Upper = M_Relx_IQR75 + M_Relx_Variance
print("Mean: %.2f \nMedian: %.2f \nMode: %.2f \nStd: %.2f\n25th percentile value: %.2f\n75th percentile value: %.2f\nInterquartile Range: %.2f\nThe Variance: %.2f\nOutliers lay outside: %.2f and %.2f" %(M_Relx_mean, M_Relx_median, M_Relx_mode, M_Relx_std,M_Relx_IQR25, M_Relx_IQR75, M_Relx_IQR, M_Relx_Variance, M_Relx_Variance_Lower,M_Relx_Variance_Upper))
print('\n')

#Relaxed - Male Respondents Histogram
bin_width = 1
mbin_count= ([0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
plt.hist(M_Relx, color='blue', edgecolor='black', bins=mbin_count)
plt.title("I have been feeling Relaxed - Male Respondents")
plt.xticks([1, 2, 3, 4, 5])
plt.xlabel("I have been feeling Relaxed")
plt.ylabel("No. of Respondents")
plt.show()

print("\nRelaxed Information - Female Respondents")
Female_df = df[df['gender']==0]
F_Relx = Female_df['Relx'].values

F_Relx_mean = stats.mean(F_Relx)
F_Relx_median = stats.median(F_Relx)
F_Relx_mode = stats.mode(F_Relx)
F_Relx_std = st.tstd(F_Relx)
F_Relx_IQR25 = int(np.percentile(F_Relx,25))
F_Relx_IQR75 = int(np.percentile(F_Relx,75))
F_Relx_IQR = F_Relx_IQR75 - F_Relx_IQR25
F_Relx_Variance = F_Relx_IQR + (F_Relx_IQR/2)
F_Relx_Variance_Lower = F_Relx_IQR25 - F_Relx_Variance
F_Relx_Variance_Upper = F_Relx_IQR75 + F_Relx_Variance
print("Mean: %.2f \nMedian: %.2f \nMode: %.2f \nStd: %.2f\n25th percentile value: %.2f\n75th percentile value: %.2f\nInterquartile Range: %.2f\nThe Variance: %.2f\nOutliers lay outside: %.2f and %.2f" %(F_Relx_mean, F_Relx_median, F_Relx_mode, F_Relx_std,F_Relx_IQR25,F_Relx_IQR75, F_Relx_IQR, F_Relx_Variance, F_Relx_Variance_Lower,F_Relx_Variance_Upper))
print('\n')

#Relaxed - Female Respondnets Histogram
bin_width = 1
mbin_count= ([0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
plt.hist(F_Relx, color='pink', edgecolor='black', bins=mbin_count)
plt.title("I have been feeling Relaxed - Female Respondents")
plt.xticks([1, 2, 3, 4, 5])
plt.xlabel("I have been feeling Relaxed")
plt.ylabel("No. of Respondents")
plt.show()


#-------------------------------------------------------------------------------------

#Goodme

print("\nFeeling good about myself Information - All Respondents")
Goodme = df['Goodme'].values
Goodme_mean = stats.mean(Goodme)
Goodme_median = stats.median(Goodme)
Goodme_mode = stats.mode(Goodme)
Goodme_std = st.tstd(Goodme)
Goodme_IQR25 = int(np.percentile(Goodme,25))
Goodme_IQR75 = int(np.percentile(Goodme,75))
Goodme_IQR = Goodme_IQR75 - Goodme_IQR25
Goodme_Variance = Goodme_IQR + (Goodme_IQR/2)
Goodme_Variance_Lower = Goodme_IQR25 - Goodme_Variance
Goodme_Variance_Upper = Goodme_IQR75 + Goodme_Variance
print("Mean: %.2f \nMedian: %.2f \nMode: %.2f \nStd: %.2f\n25th percentile value: %.2f\n75th percentile value: %.2f\nInterquartile Range: %.2f\nThe Variance: %.2f\n Outliers lay outside: %.2f and %.2f" %(Goodme_mean, Goodme_median, Goodme_mode, Goodme_std,Goodme_IQR25, Goodme_IQR75, Goodme_IQR, Goodme_Variance, Goodme_Variance_Lower,Goodme_Variance_Upper))
print('\n')

#Goodme - All Respondents Histogram
bin_width = 1
mbin_count= ([0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
plt.hist(Goodme, color='Purple', edgecolor='black', bins=mbin_count)
plt.title("I have been feeling good about myself - All Respondents")
plt.xticks([1, 2, 3, 4, 5])
plt.xlabel("I have been feeling good about myself")
plt.ylabel("No. of Respondents")
plt.show()

print("\nFeeling good about myself Information - Male Respondents")
M_Goodme = Male_df['Goodme'].values

M_Goodme_mean = stats.mean(M_Goodme)
M_Goodme_median = stats.median(M_Goodme)
M_Goodme_mode = stats.mode(M_Goodme)
M_Goodme_std = st.tstd(M_Goodme)
M_Goodme_IQR25 = int(np.percentile(M_Goodme,25))
M_Goodme_IQR75 = int(np.percentile(M_Goodme,75))
M_Goodme_IQR = M_Goodme_IQR75 - M_Goodme_IQR25
M_Goodme_Variance = M_Goodme_IQR + (M_Goodme_IQR/2)
M_Goodme_Variance_Lower = M_Goodme_IQR25 - M_Goodme_Variance
M_Goodme_Variance_Upper = M_Goodme_IQR75 + M_Goodme_Variance
print("Mean: %.2f \nMedian: %.2f \nMode: %.2f \nStd: %.2f\n25th percentile value: %.2f\n75th percentile value: %.2f\nInterquartile Range: %.2f\nThe Variance: %.2f\n Outliers lay outside: %.2f and %.2f" %(M_Goodme_mean, M_Goodme_median, M_Goodme_mode, M_Goodme_std,M_Goodme_IQR25, M_Goodme_IQR75, M_Goodme_IQR, M_Goodme_Variance, M_Goodme_Variance_Lower,M_Goodme_Variance_Upper))
print('\n')

#Goodme - Male Respondents Histogram
bin_width = 1
mbin_count= ([0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
plt.hist(M_Goodme, color='blue', edgecolor='black', bins=mbin_count)
plt.title("I have been feeling good about myself - Male Respondents")
plt.xticks([1, 2, 3, 4, 5])
plt.xlabel("I have been feeling good about myself")
plt.ylabel("No. of Respondents")
plt.show()

print("\nFeeling good about myself Information - Female Respondents")
F_Goodme = Female_df['Goodme'].values
F_Goodme_mean = stats.mean(F_Goodme)
F_Goodme_median = stats.median(F_Goodme)
F_Goodme_mode = stats.mode(F_Goodme)
F_Goodme_std = st.tstd(F_Goodme)
F_Goodme_IQR25 = int(np.percentile(F_Goodme,25))
F_Goodme_IQR75 = int(np.percentile(F_Goodme,75))
F_Goodme_IQR = F_Goodme_IQR75 - F_Goodme_IQR25
F_Goodme_Variance = F_Goodme_IQR + (F_Goodme_IQR/2)
F_Goodme_Variance_Lower = F_Goodme_IQR25 - F_Goodme_Variance
F_Goodme_Variance_Upper = F_Goodme_IQR75 + F_Goodme_Variance
print("Mean: %.2f \nMedian: %.2f \nMode: %.2f \nStd: %.2f\n25th percentile value: %.2f\n75th percentile value: %.2f\nInterquartile Range: %.2f\nThe Variance: %.2f\n Outliers lay outside: %.2f and %.2f" %(F_Goodme_mean, F_Goodme_median, F_Goodme_mode, F_Goodme_std,F_Goodme_IQR25, F_Goodme_IQR75, F_Goodme_IQR, F_Goodme_Variance, F_Goodme_Variance_Lower,F_Goodme_Variance_Upper))
print('\n')

#Goodme - Female Respondents Histogram
bin_width = 1
mbin_count= ([0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
plt.hist(F_Goodme, color='pink', edgecolor='black', bins=mbin_count)
plt.title("I have been feeling good about myself - Female Respondents")
plt.xticks([1, 2, 3, 4, 5])
plt.xlabel("I have been feeling good about myself")
plt.ylabel("No. of Respondents")
plt.show()

#-------------------------------------------------------------------------------------

#Confident

print("Confident Information - All Respondents")
Conf = df['Conf'].values
Conf_mean = stats.mean(Conf)
Conf_median = stats.median(Conf)
Conf_mode = stats.mode(Conf)
Conf_std = st.tstd(Conf)
Conf_IQR25 = int(np.percentile(Conf,25))
Conf_IQR75 = int(np.percentile(Conf,75))
Conf_IQR = Conf_IQR75 - Conf_IQR25
Conf_Variance = Conf_IQR + (Conf_IQR/2)
Conf_Variance_Lower = Conf_IQR25 - Conf_Variance
Conf_Variance_Upper = Conf_IQR75 + Conf_Variance
print("Mean: %.2f \nMedian: %.2f \nMode: %.2f \nStd: %.2f\n25th percentile value: %.2f\n75th percentile value: %.2f\nInterquartile Range: %.2f\nThe Variance: %.2f\n Outliers lay outside: %.2f and %.2f" %(Conf_mean, Conf_median, Conf_mode, Conf_std,Conf_IQR25, Conf_IQR75, Conf_IQR, Conf_Variance, Conf_Variance_Lower,Conf_Variance_Upper))
print('\n')

#Confident - All Respondents Histogram
bin_width = 1
mbin_count= ([0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
plt.hist(Conf, color='purple', edgecolor='black', bins=mbin_count)
plt.title("I have been feeling Confident - All Respondents")
plt.xticks([1, 2, 3, 4, 5])
plt.xlabel("I have been feeling Confident")
plt.ylabel("No. of Respondents")
plt.show()

print("Confident Information - Male Respondents")
M_Conf = Male_df['Conf'].values
M_Conf_mean = stats.mean(M_Conf)
M_Conf_median = stats.median(M_Conf)
M_Conf_mode = stats.mode(M_Conf)
M_Conf_std = st.tstd(M_Conf)
M_Conf_IQR25 = int(np.percentile(M_Conf,25))
M_Conf_IQR75 = int(np.percentile(M_Conf,75))
M_Conf_IQR = M_Conf_IQR75 - M_Conf_IQR25
M_Conf_Variance = M_Conf_IQR + (M_Conf_IQR/2)
M_Conf_Variance_Lower = M_Conf_IQR25 - M_Conf_Variance
M_Conf_Variance_Upper = M_Conf_IQR75 + M_Conf_Variance
print("Mean: %.2f \nMedian: %.2f \nMode: %.2f \nStd: %.2f\n25th percentile value: %.2f\n75th percentile value: %.2f\nInterquartile Range: %.2f\nThe Variance: %.2f\n Outliers lay outside: %.2f and %.2f" %(M_Conf_mean, M_Conf_median, M_Conf_mode,M_Conf_std,M_Conf_IQR25, M_Conf_IQR75, M_Conf_IQR, M_Conf_Variance, M_Conf_Variance_Lower,M_Conf_Variance_Upper))
print('\n')

#Confident - Male Respondents Histogram
bin_width = 1
mbin_count= ([0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
plt.hist(M_Conf, color='blue', edgecolor='black', bins=mbin_count)
plt.title("I have been feeling Confident - Male Respondents")
plt.xticks([1, 2, 3, 4, 5])
plt.xlabel("I have been feeling Confident")
plt.ylabel("No. of Respondents")
plt.show()

print("Confident Information - All Respondents")
F_Conf = Female_df['Conf'].values
F_Conf_mean = stats.mean(F_Conf)
F_Conf_median = stats.median(F_Conf)
F_Conf_mode = stats.mode(F_Conf)
F_Conf_std = st.tstd(F_Conf)
F_Conf_IQR25 = int(np.percentile(F_Conf,25))
F_Conf_IQR75 = int(np.percentile(F_Conf,75))
F_Conf_IQR = F_Conf_IQR75 - F_Conf_IQR25
F_Conf_Variance = F_Conf_IQR + (F_Conf_IQR/2)
F_Conf_Variance_Lower = F_Conf_IQR25 - F_Conf_Variance
F_Conf_Variance_Upper = F_Conf_IQR75 + F_Conf_Variance
print("Mean: %.2f \nMedian: %.2f \nMode: %.2f \nStd: %.2f\n25th percentile value: %.2f\n75th percentile value: %.2f\nInterquartile Range: %.2f\nThe Variance: %.2f\n Outliers lay outside: %.2f and %.2f" %(F_Conf_mean, F_Conf_median, F_Conf_mode, F_Conf_std,Conf_IQR25, F_Conf_IQR75, F_Conf_IQR, F_Conf_Variance, F_Conf_Variance_Lower,F_Conf_Variance_Upper))
print('\n')

#Confident - Female Respondents Histogram
bin_width = 1
mbin_count= ([0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
plt.hist(F_Conf, color='pink', edgecolor='black', bins=mbin_count)
plt.title("I have been feeling Confident - Female Respondents")
plt.xticks([1, 2, 3, 4, 5])
plt.xlabel("I have been feeling Confident")
plt.ylabel("No. of Respondents")
plt.show()

#-------------------------------------------------------------------------------------

#Cheerful

print("Cheerful Information - All Respondents")
Cheer = df['Cheer'].values
Cheer_mean = stats.mean(Cheer)
Cheer_median = stats.median(Cheer)
Cheer_mode = stats.mode(Cheer)
Cheer_std = st.tstd(Cheer)
Cheer_IQR25 = int(np.percentile(Cheer,25))
Cheer_IQR75 = int(np.percentile(Cheer,75))
Cheer_IQR = Cheer_IQR75 - Cheer_IQR25
Cheer_Variance = Cheer_IQR + (Cheer_IQR/2)
Cheer_Variance_Lower = Cheer_IQR25 - Cheer_Variance
Cheer_Variance_Upper = Cheer_IQR75 + Cheer_Variance
print("Mean: %.2f \nMedian: %.2f \nMode: %.2f \nStd: %.2f\n25th percentile value: %.2f\n75th percentile value: %.2f\nInterquartile Range: %.2f\nThe Variance: %.2f\n Outliers lay outside: %.2f and %.2f" %(Cheer_mean, Cheer_median, Cheer_mode, Cheer_std,Cheer_IQR25, Cheer_IQR75, Cheer_IQR, Cheer_Variance, Cheer_Variance_Lower,Cheer_Variance_Upper))
print('\n')

#Cheerful - All Respondents Histogram
bin_width = 1
mbin_count= ([0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
plt.hist(Cheer, color='purple', edgecolor='black', bins=mbin_count)
plt.title("I have been feeling Cheerful - All Respondents")
plt.xticks([1, 2, 3, 4, 5])
plt.xlabel("I have been feeling Cheerful")
plt.ylabel("No. of Respondents")
plt.show()

print("Cheerful Information - Male Respondents")
M_Cheer = Male_df['Cheer'].values
M_Cheer_mean = stats.mean(M_Cheer)
M_Cheer_median = stats.median(M_Cheer)
M_Cheer_mode = stats.mode(M_Cheer)
M_Cheer_std = st.tstd(M_Cheer)
M_Cheer_IQR25 = int(np.percentile(M_Cheer,25))
M_Cheer_IQR75 = int(np.percentile(M_Cheer,75))
M_Cheer_IQR = M_Cheer_IQR75 - M_Cheer_IQR25
M_Cheer_Variance = M_Cheer_IQR + (M_Cheer_IQR/2)
M_Cheer_Variance_Lower = M_Cheer_IQR25 - M_Cheer_Variance
M_Cheer_Variance_Upper = M_Cheer_IQR75 + M_Cheer_Variance
print("Mean: %.2f \nMedian: %.2f \nMode: %.2f \nStd: %.2f\n25th percentile value: %.2f\n75th percentile value: %.2f\nInterquartile Range: %.2f\nThe Variance: %.2f\n Outliers lay outside: %.2f and %.2f" %(M_Cheer_mean, M_Cheer_median, M_Cheer_mode, M_Cheer_std,Cheer_IQR25, M_Cheer_IQR75, M_Cheer_IQR, M_Cheer_Variance, M_Cheer_Variance_Lower,M_Cheer_Variance_Upper))
print('\n')

#Cheerful - Male Respondents Histogram
bin_width = 1
mbin_count= ([0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
plt.hist(M_Cheer, color='blue', edgecolor='black', bins=mbin_count)
plt.title("I have been feeling Cheerful - Male Respondents")
plt.xticks([1, 2, 3, 4, 5])
plt.xlabel("I have been feeling Cheerful")
plt.ylabel("No. of Respondents")
plt.show()

print("Cheerful Information - Female Respondents")
F_Cheer = Female_df['Cheer'].values
F_Cheer_mean = stats.mean(F_Cheer)
F_Cheer_median = stats.median(F_Cheer)
F_Cheer_mode = stats.mode(F_Cheer)
F_Cheer_std = st.tstd(F_Cheer)
F_Cheer_IQR25 = int(np.percentile(F_Cheer,25))
F_Cheer_IQR75 = int(np.percentile(F_Cheer,75))
F_Cheer_IQR = F_Cheer_IQR75 - F_Cheer_IQR25
F_Cheer_Variance = F_Cheer_IQR + (F_Cheer_IQR/2)
F_Cheer_Variance_Lower = F_Cheer_IQR25 - F_Cheer_Variance
F_Cheer_Variance_Upper = F_Cheer_IQR75 + F_Cheer_Variance
print("Mean: %.2f \nMedian: %.2f \nMode: %.2f \nStd: %.2f\n25th percentile value: %.2f\n75th percentile value: %.2f\nInterquartile Range: %.2f\nThe Variance: %.2f\n Outliers lay outside: %.2f and %.2f" %(F_Cheer_mean, F_Cheer_median, F_Cheer_mode, F_Cheer_std,F_Cheer_IQR25, F_Cheer_IQR75, F_Cheer_IQR, F_Cheer_Variance, F_Cheer_Variance_Lower,F_Cheer_Variance_Upper))
print('\n')

#Cheerful - Female Respondents Histogram
bin_width = 1
mbin_count= ([0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
plt.hist(F_Cheer, color='pink', edgecolor='black', bins=mbin_count)
plt.title("I have been feeling Cheerful - Female Respondents")
plt.xticks([1, 2, 3, 4, 5])
plt.xlabel("I have been feeling Cheerful")
plt.ylabel("No. of Respondents")
plt.show()