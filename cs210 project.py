#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd

# Load the step count data file
file_path = 'step_daily_trendsaat17.csv'
step_data = pd.read_csv(file_path)

# Convert the 'day_time' column from timestamp to a readable date format
step_data['date'] = pd.to_datetime(step_data['day_time'], unit='ms')

# Extracting date without the time for easier comparison
step_data['date'] = step_data['date'].dt.date

# Grouping the data by date and summing up the step counts for each day
daily_steps = step_data.groupby('date')['count'].sum().reset_index()

# Displaying the first few rows of the processed data
daily_steps.head()


# In[23]:


from scipy.stats import ttest_ind

# List of exam dates provided earlier
exam_dates = [
    "2023-11-16", "2023-11-17", "2023-11-18", "2023-11-23",
    "2023-11-30", "2023-12-01", "2023-12-12", "2023-12-19",
    "2023-12-20", "2023-12-21", "2024-01-05", "2024-01-06",
    "2024-01-09", "2024-01-11", "2024-01-15", "2024-01-17",
    "2024-01-18", "2024-01-19"
]

exam_dates = [datetime.date.fromisoformat(date) for date in exam_dates]

# Labeling each day as an exam day or a non-exam day
daily_steps['is_exam_day'] = daily_steps['date'].isin(exam_dates)

# Separating the data into exam days and non-exam days
exam_day_steps = daily_steps[daily_steps['is_exam_day']]['count']
non_exam_day_steps = daily_steps[~daily_steps['is_exam_day']]['count']

# Conducting a T-test to compare the means of the two groups
t_stat, p_value = ttest_ind(exam_day_steps, non_exam_day_steps, equal_var=False)

t_stat, p_value
# Creating comments for T-statistic and P-value

t_stat_comment = "T-statistic: The negative value ({:.4f}) indicates that the average step count on exam days tends to be lower than on non-exam days.".format(t_stat)
p_value_comment = "P-value: The p-value ({:.4f}) is greater than the conventional threshold of 0.05. This means that the difference in average step counts between exam and non-exam days is not statistically significant at the 5% significance level.".format(p_value)

t_stat_comment, p_value_comment



# In[46]:


import seaborn as sns
import matplotlib.pyplot as plt
import datetime
from scipy import stats

# Assuming daily_steps is your DataFrame with relevant columns

# Convert 'date' column to datetime if it's not already
daily_steps['date'] = pd.to_datetime(daily_steps['date'])

# Filtering the step data for these specific exam dates
filtered_exam_days_steps = daily_steps[daily_steps['date'].isin(updated_exam_dates)]

# Visualizing the step count data for these specific exam dates
plt.figure(figsize=(15, 6))
sns.scatterplot(x='date', y='count', data=filtered_exam_days_steps, color='red', alpha=0.6)

# Adding a regression line for exam days
x_exam_days = np.arange(len(filtered_exam_days_steps))
slope_exam, intercept_exam, r_value_exam, p_value_exam, std_err_exam = stats.linregress(x_exam_days, filtered_exam_days_steps['count'])
plt.plot(filtered_exam_days_steps['date'], intercept_exam + slope_exam * x_exam_days, color='blue', label='Regression Line (Exam Days)')

plt.xlabel('Date')
plt.ylabel('Step Count')
plt.title('Daily Step Counts on Exam Days with Regression Line')
plt.xticks(rotation=45)
plt.legend()

# Show the plot
plt.show()


# In[43]:


import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from datetime import datetime, timedelta

# Assuming daily_steps['date'] is of type datetime64[ns]
daily_steps['date'] = pd.to_datetime(daily_steps['date'])

# Sorting the step count data for non-exam days by date
non_exam_days_steps = daily_steps[~daily_steps['date'].isin(updated_exam_dates)]
non_exam_days_steps = non_exam_days_steps.sort_values(by='date')

# Line plot for step counts on non-exam days
plt.figure(figsize=(15, 6))
sns.lineplot(x='date', y='count', data=non_exam_days_steps, color='green', marker='o')

# Adding a regression line
slope, intercept, r_value, p_value, std_err = stats.linregress(np.arange(len(non_exam_days_steps)), non_exam_days_steps['count'])
plt.plot(non_exam_days_steps['date'], intercept + slope*np.arange(len(non_exam_days_steps)), color='blue', label='Regression Line')

plt.xlabel('Date')
plt.ylabel('Step Count')
plt.title('Daily Step Counts on Non-Exam Days with Regression Line')
plt.legend()

# Set custom ticks and labels on the x-axis for days with step counts starting from November 1, 2023
start_date = datetime(2023, 11, 1)
step_count_dates = non_exam_days_steps['date'].sort_values().unique()
plt.xticks(step_count_dates, [(start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(len(step_count_dates))], rotation=45)

# Ensure proper layout
plt.tight_layout()

# Show the plot
plt.show()


# In[44]:


import pandas as pd
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming daily_steps is your DataFrame with relevant columns
# Assuming updated_exam_dates is a list of exam dates

# Convert 'date' column to datetime if it's not already
daily_steps['date'] = pd.to_datetime(daily_steps['date'])

# Create a binary variable indicating whether it's an exam day or not
daily_steps['is_exam_day'] = daily_steps['date'].isin(updated_exam_dates).astype(int)

# Calculate the correlation matrix
correlation_matrix = daily_steps[['count', 'is_exam_day']].corr()

# Plot the heatmap for the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
plt.title('Correlation Heatmap: Step Count vs Exam Days')
plt.show()

# Create a confusion matrix
conf_matrix = confusion_matrix(daily_steps['is_exam_day'], (daily_steps['count'] > daily_steps['count'].mean()).astype(int))

# Plot the confusion matrix using seaborn heatmap
plt.figure(figsize=(4, 3))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Predicted Label')
plt.ylabel('Actual Label')
plt.title('Confusion Matrix: Step Count vs Exam Days')
plt.show()


# In[47]:


import seaborn as sns
import matplotlib.pyplot as plt
import datetime
from scipy import stats

# Assuming daily_steps is your DataFrame with relevant columns

# Convert 'date' column to datetime if it's not already
daily_steps['date'] = pd.to_datetime(daily_steps['date'])

# Creating a binary variable indicating whether it's an exam day or not
daily_steps['is_exam_day'] = daily_steps['date'].isin(updated_exam_dates).astype(int)

# Separating data for exam and non-exam days
exam_days_data = daily_steps[daily_steps['is_exam_day'] == 1]
non_exam_days_data = daily_steps[daily_steps['is_exam_day'] == 0]

# Visualizing the step count data for both exam and non-exam days
plt.figure(figsize=(15, 6))
sns.scatterplot(x='date', y='count', data=non_exam_days_data, color='green', alpha=0.6, label='Non-Exam Days')
sns.scatterplot(x='date', y='count', data=exam_days_data, color='red', alpha=0.6, label='Exam Days')

# Adding regression lines for both exam and non-exam days
x_non_exam_days = np.arange(len(non_exam_days_data))
slope_non_exam, intercept_non_exam, _, _, _ = stats.linregress(x_non_exam_days, non_exam_days_data['count'])
plt.plot(non_exam_days_data['date'], intercept_non_exam + slope_non_exam * x_non_exam_days, color='blue', label='Regression Line (Non-Exam Days)')

x_exam_days = np.arange(len(exam_days_data))
slope_exam, intercept_exam, _, _, _ = stats.linregress(x_exam_days, exam_days_data['count'])
plt.plot(exam_days_data['date'], intercept_exam + slope_exam * x_exam_days, color='purple', label='Regression Line (Exam Days)')

plt.xlabel('Date')
plt.ylabel('Step Count')
plt.title('Daily Step Counts with Regression Lines for Exam and Non-Exam Days')
plt.xticks(rotation=45)
plt.legend()

# Show the plot
plt.show()


# In[ ]:




