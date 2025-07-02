## Project Overview
This project analyzes Seattle Airbnb listings, combining listings, calendar, and reviews data to explore pricing patterns and predict nightly rates. The goal is to help Airbnb hosts estimate competitive prices and understand what drives their earnings.

---

## Features
- **Data Pipeline**
  - Ingest raw CSVs from Inside Airbnb
  - Clean and merge listings, calendar, and reviews
  - Store processed data in SQLite and CSVs

- **Exploratory Data Analysis**
  - Price distribution by neighborhood
  - Occupancy heatmaps by weekday and month
  - Seasonal price trends
  - Sentiment trends from guest reviews

- **Feature Engineering**
  - One-hot encoding for room types and neighborhoods
  - Sentiment scores for review texts
  - Weekend flag
  - Minimum nights required
  - Number of reviews

- **Modeling**
  - Baseline Linear Regression (R² ≈ 0.85)
  - Random Forest Regressor (R² ≈ 0.91, RMSE ≈ $32)

- **Visualizations**
  - Predicted vs. actual prices
  - Feature importances
  - Residual plots to spot outliers

---
