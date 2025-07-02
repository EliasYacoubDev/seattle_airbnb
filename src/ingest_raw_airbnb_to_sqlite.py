import sqlite3
import pandas as pd

def ingest_airbnb_data():
    # Step 1: Load raw CSVs
    listings = pd.read_csv("data/raw/listings.csv")
    calendar = pd.read_csv("data/raw/calendar.csv")
    reviews = pd.read_csv("data/raw/reviews.csv")

    # Step 2: Create sqlite connection
    conn = sqlite3.connect("db/seattle_airbnb.db")

    # Step 3: Save each as a table
    listings.to_sql("listings", conn, if_exists="replace", index=False)
    calendar.to_sql("calendar", conn, if_exists="replace", index=False)
    reviews.to_sql("reviews", conn, if_exists="replace", index=False)

    conn.close()
    print("Ingestion complete ✅")

if __name__ == "__main__":
    ingest_airbnb_data()