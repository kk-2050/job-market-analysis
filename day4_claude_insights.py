import anthropic
import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect('C:/Users/kaori/job-market-project/job_market.db')

# Load summary data from SQL
query = """
    SELECT formatted_experience_level,
           COUNT(*) as job_count,
           ROUND(AVG(max_salary), 0) as avg_max_salary
    FROM job_postings
    WHERE max_salary > 0
    GROUP BY formatted_experience_level
    ORDER BY job_count DESC
"""
df = pd.read_sql_query(query, conn)
conn.close()

# Convert data to text for Claude
data_summary = df.to_string(index=False)

# Claude API setup
# NOTE: Replace 'YOUR_API_KEY_HERE' with your actual API key when available
client = anthropic.Anthropic(api_key="YOUR_API_KEY_HERE")

# Send data to Claude for insight generation
message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": f"""You are a job market analyst. 
Analyze the following job market data and provide 3 key insights 
that would be useful for a job seeker:

{data_summary}

Please provide:
1. Key trend observed
2. Salary insight
3. Recommendation for job seekers
"""
        }
    ]
)

# Print and save the insights
insights = message.content[0].text
print("=== AI-Generated Job Market Insights ===")
print(insights)

# Save insights to file
with open('C:/Users/kaori/job-market-project/ai_insights.txt', 'w', encoding='utf-8') as f:
    f.write(insights)

print("\nInsights saved to ai_insights.txt!")