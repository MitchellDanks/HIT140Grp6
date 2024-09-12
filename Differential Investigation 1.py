#Descriptive Investigation 1
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt
import statistics as stats
import numpy as np

#Read Relevant Datasets
df1 = pd.read_csv('dataset1.csv')
df2 = pd.read_csv('dataset2.csv')

#Merge Relevant Datasets 
df = df1.merge(df2, on="ID")

#Create Total Weekly Screentime created by the sum of all device time (Weekend + Weekday)
WeeklyScreentime= ['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']
df['Weekly_Screentime'] = df[WeeklyScreentime].sum(axis=1)


#Create Video Game and Smartphone Weekly Screeentime (Weekly Screentime calculated by adding Weekday and Weekend)
SPSum = ['S_we','S_wk']                                     #SP Acronym for SmartPhone
df['S_Total'] = df[SPSum].sum(axis=1)                  
VGSum = ['G_we','G_wk']                                     #VG Acronym for Video Game 
df['G_Total'] = df[VGSum].sum(axis=1)

xbin_count = [i - 0.5 for i in range(-1, 62)]
bin_count = [i - 0.5 for i in range(-1, 17)]

xticks = [i for i in range(0, 61, 5)]
ticks = [str(i) for i in range(15)]

#-------------------------------------------------------------------------------------

#Dataset Screentime Totals (Histogram)
print("\nDataset Total Screentime Information")
Dataset_Count = len(df)
print("Total count of respondents:", Dataset_Count)
ScrnTtl = df['Weekly_Screentime'].values

ScrnTtl_Max = ScrnTtl.max()
ScrnTtl_Min = ScrnTtl.min()
Dataset_range = ScrnTtl_Max - ScrnTtl_Min
IQR25 = int(np.percentile(ScrnTtl,25))
IQR75 = int(np.percentile(ScrnTtl,75))
Dataset_IQR = IQR75 - IQR25
Dataset_mean = stats.mean(ScrnTtl)
Dataset_median = stats.median(ScrnTtl)
Dataset_mode = stats.mode(ScrnTtl)
Dataset_std = st.tstd(ScrnTtl)
Variance = Dataset_IQR + (Dataset_IQR/2)
Variance_Lower = IQR25 - Variance
Variance_Upper = IQR75 + Variance
print('Lowest Screentime per week: %.2f\nHighest Screentime per week: %.2f\nTotal Range: %.2f\nThe Mean (hrs): %.2f\nThe Median (hrs): %.2f\nThe Mode (hrs): %.2f\n25th percentile value (hrs): %.2f\n75th percentile value (hrs): %.2f\nThe Interquartile Range: %.2f\nThe Variance: %.2f\nOutliers lay outside: %.2f and %.2f\nThe Standard Deviation: %.2f\n'
      %(ScrnTtl_Min, ScrnTtl_Max, Dataset_range,Dataset_mean, Dataset_median,Dataset_mode,IQR25, IQR75, Dataset_IQR, Variance,Variance_Lower, Variance_Upper, Dataset_std))
print('\n')

plt.hist(ScrnTtl, color='purple', edgecolor='black', bins=xbin_count)
plt.title("Dataset Total Screentime Totals")
plt.xticks(xticks, [str(i) for i in range(0, 61, 5)])
plt.xlabel("Screentime (Hrs)")
plt.ylabel("No. of Respondents")
plt.show()

#-------------------------------------------------------------------------------------

#Male Screentime Totals (Histogram)
print("Male Total Screentime Information")
Male_df = df[df['gender']==1]
Male_Count = len(Male_df)
print("Total count of male respondents:", Male_Count)
M_ScrnTtl = Male_df['Weekly_Screentime'].values

M_ScrnTtl_Max = M_ScrnTtl.max()
M_ScrnTtl_Min = M_ScrnTtl.min()
M_range = M_ScrnTtl_Max - M_ScrnTtl_Min
M_IQR25 = int(np.percentile(M_ScrnTtl,25))
M_IQR75 = int(np.percentile(M_ScrnTtl,75))
M_Dataset_IQR = M_IQR75 - M_IQR25
M_Dataset_mean = stats.mean(M_ScrnTtl)
M_Dataset_median = stats.median(M_ScrnTtl)
M_Dataset_mode = stats.mode(M_ScrnTtl)
M_Dataset_std = st.tstd(M_ScrnTtl)
M_Variance = M_Dataset_IQR + (M_Dataset_IQR/2)
M_Variance_Lower = M_IQR25 - M_Variance
M_Variance_Upper = M_IQR75 + M_Variance
print('Lowest Screentime per week: %.2f\nHighest Screentime per week: %.2f\nTotal Range: %.2f\nThe Mean (hrs): %.2f\nThe Median (hrs): %.2f\nThe Mode (hrs): %.2f\n25th percentile value (hrs): %.2f\n75th percentile value (hrs): %.2f\nThe Interquartile Range: %.2f\nThe Variance: %.2f\nOutliers lay outside: %.2f and %.2f\nThe Standard Deviation: %.2f\n'
      %(M_ScrnTtl_Min, M_ScrnTtl_Max, M_range,M_Dataset_mean, M_Dataset_median,M_Dataset_mode,M_IQR25, M_IQR75, M_Dataset_IQR, M_Variance,M_Variance_Lower, M_Variance_Upper, M_Dataset_std))
print('\n')

plt.hist(M_ScrnTtl, color='blue', edgecolor='black', bins=xbin_count)
plt.title("Male - Total Screentime Totals")
plt.xticks(xticks, [str(i) for i in range(0, 61, 5)])
plt.xlabel("Screentime (Hrs)")
plt.ylabel("No. of Respondents")
plt.show()

#-------------------------------------------------------------------------------------

#Female Screentime Totals (Histogram)
print("Female Total Screentime Information" )
Female_df= df[df['gender']==0]
Female_Count = len(Female_df)
print("Total count of female respondents:", Female_Count)
F_ScrnTtl = Female_df['Weekly_Screentime'].values

F_ScrnTtl_Max = F_ScrnTtl.max()
F_ScrnTtl_Min = F_ScrnTtl.min()
F_range = F_ScrnTtl_Max - F_ScrnTtl_Min
F_IQR25 = int(np.percentile(F_ScrnTtl,25))
F_IQR75 = int(np.percentile(F_ScrnTtl,75))
F_Dataset_IQR = F_IQR75 - F_IQR25
F_Dataset_mean = stats.mean(F_ScrnTtl)
F_Dataset_median = stats.median(F_ScrnTtl)
F_Dataset_mode = stats.mode(F_ScrnTtl)
F_Dataset_std = st.tstd(F_ScrnTtl)
F_Variance = F_Dataset_IQR + (F_Dataset_IQR/2)
F_Variance_Lower = F_IQR25 - F_Variance
F_Variance_Upper = F_IQR75 + F_Variance
print('Lowest Screentime per week: %.2f\nHighest Screentime per week: %.2f\nTotal Range: %.2f\nThe Mean (hrs): %.2f\nThe Median (hrs): %.2f\nThe Mode (hrs): %.2f\n25th percentile value (hrs): %.2f\n75th percentile value (hrs): %.2f\nThe Interquartile Range: %.2f\nThe Variance: %.2f\nOutliers lay outside: %.2f and %.2f\nThe Standard Deviation: %.2f\n'
      %(F_ScrnTtl_Min, F_ScrnTtl_Max, F_range,F_Dataset_mean, F_Dataset_median,F_Dataset_mode,F_IQR25, F_IQR75, F_Dataset_IQR, F_Variance,F_Variance_Lower, F_Variance_Upper, F_Dataset_std))
print('\n')

plt.hist(F_ScrnTtl, color='pink', edgecolor='black', bins=xbin_count)
plt.title("Female - Total Screentime Totals")
plt.xticks(xticks, [str(i) for i in range(0, 61, 5)])
plt.xlabel("Screentime (Hrs)")
plt.ylabel("No. of Respondents")
plt.show()

#-------------------------------------------------------------------------------------

#Male Video Game Screentime Totals (Histogram)
print("\nMale Video Game Total Screentime Information")
Male_df = df[df['gender']==1]
ScrnTtl_VG_M= Male_df['G_Total'].values

ScrnTtl_Max_VG_M = ScrnTtl_VG_M.max()
ScrnTtl_Min_VG_M = ScrnTtl_VG_M .min()
Dataset_range_VG_M  = ScrnTtl_Max_VG_M  - ScrnTtl_Min_VG_M 
IQR25_VG_M  = int(np.percentile(ScrnTtl_VG_M ,25))
IQR75_VG_M  = int(np.percentile(ScrnTtl_VG_M ,75))
Dataset_IQR_VG_M  = IQR75_VG_M  - IQR25_VG_M 
Dataset_mean_VG_M  = stats.mean(ScrnTtl_VG_M )
Dataset_median_VG_M  = stats.median(ScrnTtl_VG_M )
Dataset_mode_VG_M  = stats.mode(ScrnTtl_VG_M )
Dataset_std_VG_M  = st.tstd(ScrnTtl_VG_M )
Variance_VG_M  = Dataset_IQR_VG_M  + (Dataset_IQR_VG_M /2)
Variance_Lower_VG_M  = IQR25_VG_M  - Variance_VG_M 
Variance_Upper_VG_M  = IQR75_VG_M  + Variance_VG_M 
print('Lowest Screentime per week: %.2f\nHighest Screentime per week: %.2f\nTotal Range: %.2f\nThe Mean (hrs): %.2f\nThe Median (hrs): %.2f\nThe Mode (hrs): %.2f\n25th percentile value (hrs): %.2f\n75th percentile value (hrs): %.2f\nThe Interquartile Range: %.2f\nThe Variance: %.2f\nOutliers lay outside: %.2f and %.2f\nThe Standard Deviation: %.2f\n'
      %(ScrnTtl_Min_VG_M , ScrnTtl_Max_VG_M , Dataset_range_VG_M ,Dataset_mean_VG_M , Dataset_median_VG_M ,Dataset_mode_VG_M ,IQR25_VG_M , IQR75_VG_M , Dataset_IQR_VG_M , Variance_VG_M ,Variance_Lower_VG_M , Variance_Upper_VG_M , Dataset_std_VG_M ))
print('\n')

plt.hist(ScrnTtl_VG_M , color='blue', edgecolor='black', bins=bin_count)
plt.title("Male - Video Game Screentime Totals")
plt.xticks(range(15), ticks)
plt.xlabel("Screentime (Hrs)")
plt.ylabel("No. of Respondents")
plt.show()

#-------------------------------------------------------------------------------------

#Female Video Game Screentime Totals (Histogram)
print("\nFemale Video Game Total Screentime Information")
Female_df= df[df['gender']==0]
ScrnTtl_VG_F = Female_df['G_Total'].values

ScrnTtl_Max_VG_F = ScrnTtl_VG_F.max()
ScrnTtl_Min_VG_F = ScrnTtl_VG_F.min()
Dataset_range_VG_F = ScrnTtl_Max_VG_F - ScrnTtl_Min_VG_F
IQR25_VG_F = int(np.percentile(ScrnTtl_VG_F,25))
IQR75_VG_F = int(np.percentile(ScrnTtl_VG_F,75))
Dataset_IQR_VG_F = IQR75_VG_F - IQR25_VG_F
Dataset_mean_VG_F = stats.mean(ScrnTtl_VG_F)
Dataset_median_VG_F = stats.median(ScrnTtl_VG_F)
Dataset_mode_VG_F = stats.mode(ScrnTtl_VG_F)
Dataset_std_VG_F = st.tstd(ScrnTtl_VG_F)
Variance_VG_F = Dataset_IQR_VG_F + (Dataset_IQR_VG_F/2)
Variance_Lower_VG_F = IQR25_VG_F - Variance_VG_F
Variance_Upper_VG_F = IQR75_VG_F + Variance_VG_F
print('Lowest Screentime per week: %.2f\nHighest Screentime per week: %.2f\nTotal Range: %.2f\nThe Mean (hrs): %.2f\nThe Median (hrs): %.2f\nThe Mode (hrs): %.2f\n25th percentile value (hrs): %.2f\n75th percentile value (hrs): %.2f\nThe Interquartile Range: %.2f\nThe Variance: %.2f\nOutliers lay outside: %.2f and %.2f\nThe Standard Deviation: %.2f\n'
      %(ScrnTtl_Min_VG_F, ScrnTtl_Max_VG_F, Dataset_range_VG_F,Dataset_mean_VG_F, Dataset_median_VG_F,Dataset_mode_VG_F,IQR25_VG_F, IQR75_VG_F, Dataset_IQR_VG_F, Variance_VG_F,Variance_Lower_VG_F, Variance_Upper_VG_F, Dataset_std_VG_F))
print('\n')

plt.hist(ScrnTtl_VG_F, color='pink', edgecolor='black', bins=bin_count)
plt.title("Female - Video Game Screentime Totals")
plt.xticks(range(15), ticks)
plt.xlabel("Screentime (Hrs)")
plt.ylabel("No. of Respondents")
plt.show()
#-------------------------------------------------------------------------------------

#Male Smartphone Screentime Totals (Histogram)
print("\nMale Smartphone Total Screentime Information")
ScrnTtl_SP_M = Male_df['S_Total'].values

ScrnTtl_Max_SP_M  = ScrnTtl_SP_M .max()
ScrnTtl_Min_SP_M  = ScrnTtl_SP_M .min()
Dataset_range_SP_M  = ScrnTtl_Max_SP_M  - ScrnTtl_Min_SP_M 
IQR25_SP_M  = int(np.percentile(ScrnTtl_SP_M ,25))
IQR75_SP_M  = int(np.percentile(ScrnTtl_SP_M ,75))
Dataset_IQR_SP_M  = IQR75_SP_M  - IQR25_SP_M 
Dataset_mean_SP_M  = stats.mean(ScrnTtl_SP_M )
Dataset_median_SP_M  = stats.median(ScrnTtl_SP_M )
Dataset_mode_SP_M  = stats.mode(ScrnTtl_SP_M )
Dataset_std_SP_M  = st.tstd(ScrnTtl_SP_M )
Variance_SP_M  = Dataset_IQR_SP_M  + (Dataset_IQR_SP_M /2)
Variance_Lower_SP_M  = IQR25_SP_M  - Variance_SP_M 
Variance_Upper_SP_M  = IQR75_SP_M  + Variance_SP_M 
print('Lowest Screentime per week: %.2f\nHighest Screentime per week: %.2f\nTotal Range: %.2f\nThe Mean (hrs): %.2f\nThe Median (hrs): %.2f\nThe Mode (hrs): %.2f\n25th percentile value (hrs): %.2f\n75th percentile value (hrs): %.2f\nThe Interquartile Range: %.2f\nThe Variance: %.2f\nOutliers lay outside: %.2f and %.2f\nThe Standard Deviation: %.2f\n'
      %(ScrnTtl_Min_SP_M , ScrnTtl_Max_SP_M , Dataset_range_SP_M ,Dataset_mean_SP_M , Dataset_median_SP_M ,Dataset_mode_SP_M ,IQR25_SP_M , IQR75_SP_M , Dataset_IQR_SP_M , Variance_SP_M ,Variance_Lower_SP_M , Variance_Upper_SP_M , Dataset_std_SP_M ))
print('\n')

plt.hist(ScrnTtl_SP_M, color='blue', edgecolor='black', bins=bin_count)
plt.title("Male - Smartphone Screentime Totals")
plt.xticks(range(15), ticks)
plt.xlabel("Screentime (Hrs)")
plt.ylabel("No. of Respondents")
plt.show()

#-------------------------------------------------------------------------------------

#Female Smartphone Screentime Totals (Histogram)
print("\nFemale Smartphone Total Screentime Information")
ScrnTtl_SP_F = Female_df['S_Total'].values

ScrnTtl_Max_SP_F  = ScrnTtl_SP_F .max()
ScrnTtl_Min_SP_F  = ScrnTtl_SP_F .min()
Dataset_range_SP_F  = ScrnTtl_Max_SP_F  - ScrnTtl_Min_SP_F 
IQR25_SP_F  = int(np.percentile(ScrnTtl_SP_F ,25))
IQR75_SP_F  = int(np.percentile(ScrnTtl_SP_F ,75))
Dataset_IQR_SP_F  = IQR75_SP_F  - IQR25_SP_F 
Dataset_mean_SP_F  = stats.mean(ScrnTtl_SP_F )
Dataset_median_SP_F  = stats.median(ScrnTtl_SP_F )
Dataset_mode_SP_F  = stats.mode(ScrnTtl_SP_F )
Dataset_std_SP_F  = st.tstd(ScrnTtl_SP_F )
Variance_SP_F  = Dataset_IQR_SP_F  + (Dataset_IQR_SP_F /2)
Variance_Lower_SP_F  = IQR25_SP_F  - Variance_SP_F 
Variance_Upper_SP_F  = IQR75_SP_F  + Variance_SP_F 
print('Lowest Screentime per week: %.2f\nHighest Screentime per week: %.2f\nTotal Range: %.2f\nThe Mean (hrs): %.2f\nThe Median (hrs): %.2f\nThe Mode (hrs): %.2f\n25th percentile value (hrs): %.2f\n75th percentile value (hrs): %.2f\nThe Interquartile Range: %.2f\nThe Variance: %.2f\nOutliers lay outside: %.2f and %.2f\nThe Standard Deviation: %.2f\n'
      %(ScrnTtl_Min_SP_F , ScrnTtl_Max_SP_F , Dataset_range_SP_F ,Dataset_mean_SP_F , Dataset_median_SP_F ,Dataset_mode_SP_F ,IQR25_SP_F , IQR75_SP_F , Dataset_IQR_SP_F , Variance_SP_F ,Variance_Lower_SP_F , Variance_Upper_SP_F , Dataset_std_SP_F ))
print('\n')

plt.hist(ScrnTtl_SP_F, color='pink', edgecolor='black', bins=bin_count)
plt.title("Female - Smartphone Screentime Totals")
plt.xticks(range(15), ticks)
plt.xlabel("Screentime (Hrs)")
plt.ylabel("No. of Respondents")
plt.show()