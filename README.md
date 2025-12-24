# Customer Shopping Behavior Analysis

## Overview

This project analyzes customer shopping behavior to uncover purchasing patterns, customer demographics insights, and business-relevant trends.
The workflow covers data loading and cleaning using Python, exploratory data analysis (EDA), business analysis using SQL in PostgreSQL, and data visualization through an interactive Power BI dashboard.

The goal of this project is to demonstrate an end-to-end data analytics process commonly used in real-world business scenarios.

---

## Dataset

The dataset contains customer-level transaction and behavioral data, including:

* Customer demographics (age, gender, location)
* Product and category information
* Purchase amount and frequency
* Discounts, promotions, and payment methods
* Customer reviews and subscription status

**Format:** CSV
**Size:** ~3,900 records

---

## Tools & Technologies

* **Python** (Pandas, SQLAlchemy) – data loading, cleaning, and feature engineering
* **PostgreSQL** – business analysis using SQL queries
* **Power BI** – data visualization and dashboard creation
* **VS Code** – development environment
* **GitHub** – version control and project documentation

---

## Project Workflow

1. **Data Loading**

   * Loaded raw CSV data into Python using Pandas
   * Used dynamic file paths for portability

2. **Exploratory Data Analysis (EDA)**

   * Checked data structure, data types, and missing values
   * Identified inconsistencies and potential data quality issues

3. **Data Cleaning & Feature Engineering**

   * Handled missing values using median-based imputation
   * Standardized column names for SQL compatibility
   * Created new analytical features such as:

     * Age groups
     * Purchase frequency in days
   * Removed redundant columns after validation

4. **Database Integration**

   * Loaded cleaned data into PostgreSQL using SQLAlchemy
   * Created tables for analytical querying

5. **SQL Analysis**

   * Wrote SQL queries to analyze:

     * Customer purchasing patterns
     * Revenue by category
     * Purchase frequency trends
     * Customer segmentation insights

6. **Data Visualization**

   * Built an interactive Power BI dashboard
   * Visualized key KPIs and trends for business stakeholders

---

## Dashboard

The Power BI dashboard provides insights such as:

* Total sales and average purchase value
* Sales and revenue by product category
* Customer segmentation by age group and gender
* Purchase frequency and payment method trends

The dashboard is designed for clarity, interactivity, and business decision-making.

---

## Key Results & Insights

* Identified high-performing product categories and customer segments
* Revealed purchasing frequency patterns across different age groups
* Highlighted the impact of discounts and promotions on customer behavior
* Provided actionable insights that can support marketing and sales strategies

---

## How to Run This Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/customer_shopping_behavior.git
cd customer_shopping_behavior
```

### 2. Install Dependencies

```bash
pip install pandas sqlalchemy psycopg2
```

### 3. Run the Python Script

```bash
python main.py
```

This will:

* Load and clean the dataset
* Upload the processed data to PostgreSQL

### 4. Run SQL Queries

* Open PostgreSQL (pgAdmin or psql)
* Execute the SQL script provided in the repository

### 5. Open Power BI Dashboard

* Open the `.pbix` file using Power BI Desktop
* Connect to the PostgreSQL database if required

---

## Notes

* Database credentials should be configured securely (e.g., environment variables).
* The dataset is used for educational and portfolio purposes only.

---

📌 *This project demonstrates practical data analytics skills, including data cleaning, SQL analysis, and dashboard storytelling, aligned with real-world business use cases.*
