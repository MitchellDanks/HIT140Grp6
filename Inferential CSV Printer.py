import pandas as pd

# Load Datasets
df1 = pd.read_csv('dataset1.csv')
df2 = pd.read_csv('dataset2.csv')
df3 = pd.read_csv('dataset3.csv')

# Sample Size
n = 30

# Calculate the sum of the specified columns in df2
df2['sum'] = df2[['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']].sum(axis=1)

# Filter df2 to only include rows where the sum is 20 or more
df2_filtered = df2[df2['sum'] >= 20]

# Merge the datasets on ID
merged_df = df1.merge(df2_filtered, on='ID').merge(df3, on='ID')

# Separate IDs based on gender
males_df = merged_df[merged_df['gender'] == 1]
females_df = merged_df[merged_df['gender'] == 0]

# Randomly select male and female IDs
selected_males = males_df.sample(n, random_state=None)['ID'].tolist()
selected_females = females_df.sample(n, random_state=None)['ID'].tolist()

# Filter the merged DataFrame to only include the selected IDs
selected_males_df = merged_df[merged_df['ID'].isin(selected_males)]
selected_females_df = merged_df[merged_df['ID'].isin(selected_females)]

# Save the selected rows to new CSV files
selected_males_df.to_csv('selected_males.csv', index=False)
selected_females_df.to_csv('selected_females.csv', index=False)

print('Selected males and females have been saved to "selected_males.csv" and "selected_females.csv".')