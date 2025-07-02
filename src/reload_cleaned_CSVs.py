import sqlite3
import pandas as pd

import os
print(os.getcwd())
# load
listings = pd.read_csv("data/processed/listings_cleaned.csv")
calendar = pd.read_csv("data/processed/calendar_cleaned.csv")
reviews = pd.read_csv("data/processed/reviews_cleaned.csv")

# connect
conn = sqlite3.connect("db/seattle_airbnb.db")

# overwrite cleaned tables
listings.to_sql("listings_cleaned", conn, if_exists="replace", index=False)
calendar.to_sql("calendar_cleaned", conn, if_exists="replace", index=False)
reviews.to_sql("reviews_cleaned", conn, if_exists="replace", index=False)

conn.close()
print("✅ Cleaned data loaded back into SQLite")
