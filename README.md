CS210 Final Project 
Berke Basri CAN 30687
## Overview
This project aims to analyze the relationship between myexam dates and daily step counts over the last three months. The hypothesis is that step counts tend to decrease on exam days due to increased study time and reduced physical activity.

## Data
- The daily step count data was collected using a step counter device or application.
- Exam dates were collected using a google developer API from my calender
## Methodology
1. Data Preparation:
   - Cleaned and formatted the data.
   - Filtered data for the last three months.
   - Identified exam days based on provided timestamps.

2. Data Analysis:
   - Compared average step counts on exam days and non-exam days.
   - Conducted a t-test to assess the statistical significance of differences.

3. Data Visualization:
   - Plotted daily step counts on non-exam days.
   - Fitted a regression line to visualize trends.
   - Customized x-axis labels to show months starting from November 2023.

## Findings
- On average, step counts were lower on exam days compared to non-exam days.
- However, the difference was not statistically significant at the 5% significance level (p-value > 0.05).

## Usage
- You can reproduce this analysis by following the code provided.
- Modify the data and hypotheses to suit your own research questions.

## Dependencies
- Python
- Pandas
- Matplotlib
- Seaborn
- Scipy

## Acknowledgments
- Data collected and provided by [Berke Basri CAN].
- Inspired by similar studies on the relationship between academic stress and physical activity.

## Contact
For any questions or feedback, please contact [berkebasrican@gmail.com].
