import numpy as np
import pandas as pd

# 1. Load dataset
df = pd.read_csv("netflix_titles.csv")

# 2. Handle missing values
df["director"] = df["director"].fillna("Unknown Director")
df["cast"] = df["cast"].fillna("Unknown Cast")
df["country"] = df["country"].fillna("Unknown Country")
df["rating"] = df["rating"].fillna("Unknown Rating")

# 3. Clean and parse date_added
df["date_added"] = df["date_added"].str.strip()
df["date_added"] = pd.to_datetime(
    df["date_added"], format="mixed", errors="coerce"
)
df["year_added"] = df["date_added"].dt.year

# 4. Create timeline category for the 'Before & After 2010s' chart
df["era"] = np.where(df["release_year"] > 2010, ">2010", "<=2010")

# 5. Extract primary (first) country & primary genre for simple chart mapping
df["primary_country"] = (
    df["country"].apply(lambda x: x.split(",")[0].strip())
    if "country" in df
    else "Unknown"
)
df["primary_genre"] = (
    df["listed_in"].apply(lambda x: x.split(",")[0].strip())
    if "listed_in" in df
    else "Unknown"
)

# 6. Save clean dataset for Tableau
df.to_csv("netflix_cleaned.csv", index=False)
print("Data cleaned and exported to 'netflix_cleaned.csv'")