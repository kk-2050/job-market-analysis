# Load libraries
library(dplyr)
library(ggplot2)

# Load data
df <- read.csv("C:/Users/kaori/job-market-project/postings_clean.csv")

# Remove rows where max_salary is 0
df_salary <- df %>%
  filter(max_salary > 0)

# ---- Plot 1: Job Count by Experience Level ----
job_count <- df %>%
  filter(formatted_experience_level != "Not specified") %>%
  group_by(formatted_experience_level) %>%
  summarise(job_count = n()) %>%
  arrange(desc(job_count))

ggplot(job_count, aes(x = reorder(formatted_experience_level, job_count), 
                      y = job_count, fill = formatted_experience_level)) +
  geom_bar(stat = "identity") +
  coord_flip() +
  labs(title = "Job Count by Experience Level",
       x = "Experience Level",
       y = "Number of Jobs") +
  theme_minimal() +
  theme(legend.position = "none")

ggsave("C:/Users/kaori/job-market-project/r_plot1_job_count.png", 
       width = 8, height = 5)

# ---- Plot 2: Avg Salary by Experience Level ----
salary_summary <- df_salary %>%
  filter(formatted_experience_level != "Not specified") %>%
  group_by(formatted_experience_level) %>%
  summarise(avg_max_salary = mean(max_salary)) %>%
  arrange(desc(avg_max_salary))

ggplot(salary_summary, aes(x = reorder(formatted_experience_level, avg_max_salary), 
                           y = avg_max_salary, fill = formatted_experience_level)) +
  geom_bar(stat = "identity") +
  coord_flip() +
  labs(title = "Average Max Salary by Experience Level",
       x = "Experience Level",
       y = "Average Max Salary (USD)") +
  theme_minimal() +
  theme(legend.position = "none") +
  scale_y_continuous(labels = scales::comma)

ggsave("C:/Users/kaori/job-market-project/r_plot2_salary.png", 
       width = 8, height = 5)

print("Plots saved successfully!")

# ---- Plot 3: Top 10 Locations by Job Count ----
top_locations <- df %>%
  group_by(location) %>%
  summarise(job_count = n()) %>%
  arrange(desc(job_count)) %>%
  slice(2:11)  # Skip "United States" as it's too broad

ggplot(top_locations, aes(x = reorder(location, job_count), 
                          y = job_count, fill = location)) +
  geom_bar(stat = "identity") +
  coord_flip() +
  labs(title = "Top 10 Cities by Job Count",
       x = "Location",
       y = "Number of Jobs") +
  theme_minimal() +
  theme(legend.position = "none")

ggsave("C:/Users/kaori/job-market-project/r_plot3_locations.png", 
       width = 8, height = 5)

# ---- Plot 4: Work Type Distribution ----
work_type <- df %>%
  group_by(formatted_work_type) %>%
  summarise(job_count = n()) %>%
  arrange(desc(job_count))

ggplot(work_type, aes(x = reorder(formatted_work_type, job_count), 
                      y = job_count, fill = formatted_work_type)) +
  geom_bar(stat = "identity") +
  coord_flip() +
  labs(title = "Job Count by Work Type",
       x = "Work Type",
       y = "Number of Jobs") +
  theme_minimal() +
  theme(legend.position = "none")

ggsave("C:/Users/kaori/job-market-project/r_plot4_work_type.png", 
       width = 8, height = 5)

print("All 4 plots saved successfully!")