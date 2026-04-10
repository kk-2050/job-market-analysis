import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect('C:/Users/kaori/job-market-project/job_market.db')

# Query 1: Top 10 companies with most job postings
print("=== Top 10 Companies by Job Postings ===")
query1 = """
    SELECT company_name, COUNT(*) as job_count
    FROM job_postings
    WHERE company_name IS NOT NULL
    GROUP BY company_name
    ORDER BY job_count DESC
    LIMIT 10
"""
df1 = pd.read_sql_query(query1, conn)
print(df1)

# Query 2: Job count by experience level
print("\n=== Job Count by Experience Level ===")
query2 = """
    SELECT formatted_experience_level, COUNT(*) as job_count
    FROM job_postings
    GROUP BY formatted_experience_level
    ORDER BY job_count DESC
"""
df2 = pd.read_sql_query(query2, conn)
print(df2)

# Query 3: Average salary by experience level
print("\n=== Average Salary by Experience Level ===")
query3 = """
    SELECT formatted_experience_level,
           ROUND(AVG(max_salary), 0) as avg_max_salary,
           ROUND(AVG(min_salary), 0) as avg_min_salary
    FROM job_postings
    WHERE max_salary > 0
    GROUP BY formatted_experience_level
    ORDER BY avg_max_salary DESC
"""
df3 = pd.read_sql_query(query3, conn)
print(df3)

# Query 4: Top 10 locations
print("\n=== Top 10 Locations ===")
query4 = """
    SELECT location, COUNT(*) as job_count
    FROM job_postings
    GROUP BY location
    ORDER BY job_count DESC
    LIMIT 10
"""
df4 = pd.read_sql_query(query4, conn)
print(df4)

# Save all results to CSV
df1.to_csv('C:/Users/kaori/job-market-project/result_top_companies.csv', index=False)
df2.to_csv('C:/Users/kaori/job-market-project/result_experience_level.csv', index=False)
df3.to_csv('C:/Users/kaori/job-market-project/result_salary.csv', index=False)
df4.to_csv('C:/Users/kaori/job-market-project/result_locations.csv', index=False)

print("\nAll results saved to CSV!")
conn.close()