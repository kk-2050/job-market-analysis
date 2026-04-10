import pandas as pd
import sqlite3

# Load data
df = pd.read_csv('C:/Users/kaori/job-market-project/postings.csv')
print("Original data:", df.shape)

# Keep only relevant columns
columns_to_keep = [
    'job_id', 'company_name', 'title', 'location',
    'max_salary', 'min_salary', 'med_salary',
    'formatted_experience_level', 'formatted_work_type',
    'skills_desc', 'work_type'
]
df = df[columns_to_keep]
print("After column selection:", df.shape)

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Fill missing values
df['max_salary'] = df['max_salary'].fillna(0)
df['min_salary'] = df['min_salary'].fillna(0)
df['med_salary'] = df['med_salary'].fillna(0)
df['skills_desc'] = df['skills_desc'].fillna('Not specified')
df['formatted_experience_level'] = df['formatted_experience_level'].fillna('Not specified')

# Save cleaned CSV
df.to_csv('C:/Users/kaori/job-market-project/postings_clean.csv', index=False)
print("\nCleaned CSV saved!")

# Save to SQLite database
conn = sqlite3.connect('C:/Users/kaori/job-market-project/job_market.db')
df.to_sql('job_postings', conn, if_exists='replace', index=False)
conn.close()
print("SQLite database saved!")