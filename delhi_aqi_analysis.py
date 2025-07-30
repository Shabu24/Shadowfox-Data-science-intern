# delhi_aqi_analysis.py
# Author: Shahabaaz (for urgent AQI analysis project)
# Purpose: Analyze Delhi AQI data, understand pollution patterns, and generate useful insights

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ---------------------------
# Step 1: Load the Dataset
# ---------------------------
print("Loading the AQI dataset...")
df = pd.read_csv("delhiaqi.csv")
df['date'] = pd.to_datetime(df['date'])
print("Data loaded successfully!")

# ---------------------------
# Step 2: Preprocessing
# ---------------------------
print("Processing date and extracting useful information...")
df['date_only'] = df['date'].dt.date

# Extract month and define season
print("Adding month and season columns...")
df['month'] = df['date'].dt.month

def assign_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Summer'
    elif month in [6, 7, 8]:
        return 'Monsoon'
    else:
        return 'Post-Monsoon'

df['season'] = df['month'].apply(assign_season)

# ---------------------------
# Step 3: Calculate Daily Averages
# ---------------------------
print("Calculating daily average pollutant values...")
daily_avg = df.groupby('date_only')[['pm2_5', 'pm10', 'no2', 'so2']].mean().reset_index()

# ---------------------------
# Step 4: Create Output Folder
# ---------------------------
print("Creating folder for output plots...")
os.makedirs("outputs", exist_ok=True)

# ---------------------------
# Step 5: Plot PM2.5 and PM10 Trends
# ---------------------------
print("Generating trend plot for PM2.5 and PM10...")
plt.figure(figsize=(12, 6))
plt.plot(daily_avg['date_only'], daily_avg['pm2_5'], label='PM2.5', color='crimson')
plt.plot(daily_avg['date_only'], daily_avg['pm10'], label='PM10', color='darkorange')
plt.xlabel("Date")
plt.ylabel("Concentration (µg/m³)")
plt.title("Daily PM2.5 and PM10 Trends in Delhi")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/pm_trend.png")
plt.close()

# ---------------------------
# Step 6: Seasonal Boxplots
# ---------------------------
print("Generating seasonal boxplots for PM2.5 and PM10...")
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='season', y='pm2_5', palette='Reds')
plt.title("PM2.5 Levels by Season")
plt.ylabel("PM2.5 (µg/m³)")
plt.savefig("outputs/pm2_5_by_season.png")
plt.close()

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='season', y='pm10', palette='Oranges')
plt.title("PM10 Levels by Season")
plt.ylabel("PM10 (µg/m³)")
plt.savefig("outputs/pm10_by_season.png")
plt.close()

# ---------------------------
# Step 7: Correlation Heatmap
# ---------------------------
print("Creating heatmap to show pollutant correlations...")
pollutants = df[['pm2_5', 'pm10', 'no2', 'so2']]
correlation = pollutants.corr()
plt.figure(figsize=(6, 4))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Between Key Pollutants")
plt.tight_layout()
plt.savefig("outputs/correlation_heatmap.png")
plt.close()

# ---------------------------
# Step 8: Summary Insights
# ---------------------------
print("\n================ SUMMARY INSIGHTS ================")
print("1. Most critical pollutants contributing to AQI: PM2.5 and PM10")
print("2. Season with worst PM2.5 levels:", df.groupby('season')['pm2_5'].mean().idxmax())
print("3. Season with worst PM10 levels:", df.groupby('season')['pm10'].mean().idxmax())
print("4. Correlation between PM2.5 and PM10:", round(correlation.loc['pm2_5', 'pm10'], 2))
print("5. All graphs have been saved in the 'outputs' folder.")
print("==================================================\n")
