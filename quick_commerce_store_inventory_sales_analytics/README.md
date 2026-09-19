# 🛒 Quick Commerce Store Inventory & Sales Analytics

> A MySQL-based data analytics project for analyzing orders, customers, products, inventory, stores, and sales performance in a simulated quick-commerce business.

---

## 📌 Overview

Quick-commerce businesses generate large volumes of transactional and inventory data across multiple stores. This project uses **MySQL and SQL analytics** to transform operational data into meaningful business insights.

The project demonstrates how a relational database can be designed, populated, queried, and analyzed to support real-world business decisions related to inventory, sales, customers, products, and store operations.

### Key Areas Covered

- 📦 Inventory and stock analysis
- 🛍️ Order and sales analysis
- 🏪 Store performance analysis
- 🏷️ Product and category analysis
- 👥 Customer analysis
- 🔄 Reorder identification
- 📊 Business KPI analysis
- 🗄️ Relational database design
- 🔗 Multi-table SQL analytics

---

## 🎯 Business Objectives

The project is designed to answer practical business questions such as:

- Which stores have the highest order volumes?
- Which products require immediate restocking?
- Which products have high demand?
- How many orders are delivered or cancelled?
- How does order activity vary across stores?
- How is inventory distributed across stores?
- Which product categories contribute significantly to business activity?
- Which products may require inventory attention?
- Where are potential inventory and operational bottlenecks?

---

## 🏗️ Database Architecture

The database consists of **7 interconnected relational tables**:

| Table | Description |
|---|---|
| `categories` | Stores product category information |
| `products` | Contains product catalog and pricing information |
| `stores` | Contains store-level information |
| `customers` | Contains customer information |
| `inventory` | Tracks product inventory across stores |
| `orders` | Stores customer order information |
| `order_items` | Stores individual products included in each order |

### Entity Relationship

```text
                         ┌──────────────┐
                         │  categories  │
                         └──────┬───────┘
                                │
                                │
                         ┌──────▼───────┐
                         │   products   │
                         └──────┬───────┘
                                │
                    ┌───────────┴───────────┐
                    │                       │
             ┌──────▼───────┐       ┌──────▼───────┐
             │  inventory   │       │ order_items  │
             └──────┬───────┘       └──────┬───────┘
                    │                       │
             ┌──────▼───────┐       ┌──────▼───────┐
             │    stores    │       │    orders    │
             └──────────────┘       └──────┬───────┘
                                           │
                                    ┌──────▼───────┐
                                    │  customers   │
                                    └──────────────┘
````

The detailed ER structure is available in:

```text
docs/ER_DIAGRAM.txt
```

---

## 📊 Dataset

The project contains the following datasets:

| Dataset           | Records |
| ----------------- | ------: |
| Categories        |       6 |
| Stores            |       6 |
| Products          |      22 |
| Customers         |     150 |
| Inventory Records |     132 |
| Orders            |   1,200 |
| Order Items       |   3,057 |

The dataset represents a multi-store quick-commerce environment with customers, products, orders, inventory, and store-level operations.

---

## 🔍 Analytics Performed

### 📦 1. Inventory Analysis

The inventory analysis focuses on:

* Current stock levels
* Reorder levels
* Low-stock products
* Store-level inventory
* Products requiring replenishment
* Stock availability across stores

Example business question:

> Which products should be considered for immediate replenishment based on current stock and reorder levels?

---

### 🏪 2. Store Performance Analysis

Store-level performance is analyzed using:

* Total orders
* Delivered orders
* Cancelled orders
* Store-level order activity
* Operational order metrics

This provides visibility into order activity and fulfillment patterns across stores.

---

### 🛍️ 3. Product Analysis

Product-level analysis includes:

* Product demand
* Product sales activity
* Pricing
* Inventory availability
* Order frequency
* Product-level performance

---

### 🏷️ 4. Category Analysis

Category-level analysis examines:

* Category demand
* Product distribution
* Category activity
* Inventory availability
* Category-level sales metrics

---

### 👥 5. Customer Analysis

Customer-level analysis includes:

* Customer ordering activity
* Order frequency
* Transaction behavior
* Customer-level metrics

---

## 🧠 SQL Concepts Demonstrated

The project demonstrates practical usage of:

* `SELECT`
* `WHERE`
* `GROUP BY`
* `HAVING`
* `ORDER BY`
* `INNER JOIN`
* `LEFT JOIN`
* Aggregate Functions
* `COUNT()`
* `SUM()`
* `AVG()`
* `MIN()`
* `MAX()`
* `CASE`
* Subqueries
* Conditional Aggregation
* Date-based Analysis
* Inventory Calculations
* Business KPI Calculations

---

## 🛠️ Technology Stack

### Database

* MySQL

### Analytics

* SQL
* Python
* Streamlit

### Development Tools

* MySQL Workbench
* Git
* GitHub

---

## 📁 Project Structure

```text
Quick_Commerce_Store_Inventory_Sales_Analytics/
│
├── README.md
│
├── dashboard/
│   ├── app.py
│   ├── requirements.txt
│   └── .env.example
│
├── data/
│   ├── categories.csv
│   ├── customers.csv
│   ├── inventory.csv
│   ├── order_items.csv
│   ├── orders.csv
│   ├── products.csv
│   └── stores.csv
│
├── docs/
│   └── ER_DIAGRAM.txt
│
└── sql/
    ├── 01_schema_and_seed.sql
    └── 02_analytics_queries.sql
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

* MySQL
* MySQL Workbench
* Python 3.x
* Git

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Bhuvaneswari123463/Quick_Commerce_Store_Inventory_Sales_Analytics.git
```

Navigate into the project:

```bash
cd Quick_Commerce_Store_Inventory_Sales_Analytics
```

---

### 2️⃣ Create the Database

Open **MySQL Workbench**.

Execute:

```text
sql/01_schema_and_seed.sql
```

This script:

* Creates the database
* Creates the required tables
* Defines relationships
* Loads the project data

---

### 3️⃣ Run Analytics Queries

Open:

```text
sql/02_analytics_queries.sql
```

Execute the queries in MySQL Workbench to reproduce the analytics.

---

## 📈 Business KPIs

The project supports analysis of several important business KPIs:

| KPI                  | Description                                 |
| -------------------- | ------------------------------------------- |
| Total Orders         | Measures overall transaction volume         |
| Delivered Orders     | Measures successful fulfillment             |
| Cancelled Orders     | Tracks unsuccessful orders                  |
| Stock Availability   | Measures inventory readiness                |
| Reorder Requirements | Identifies products requiring replenishment |
| Product Demand       | Identifies frequently ordered products      |
| Store Order Volume   | Measures activity across stores             |
| Category Activity    | Measures category-level performance         |

---

## 💼 Business Applications

The analysis can support business teams in areas such as:

### Inventory Management

Identify products with low inventory and potential replenishment requirements.

### Store Operations

Monitor order activity and fulfillment patterns across different stores.

### Product Management

Understand product demand and inventory availability.

### Sales Analytics

Analyze order activity and transactional patterns.

### Demand Planning

Use historical transaction and inventory data as a foundation for future demand forecasting.

### Business Intelligence

Convert raw operational data into structured business metrics and actionable insights.

---

## 📊 Dashboard

The project also contains a dashboard component built using:

* Python
* Streamlit
* MySQL

Dashboard files:

```text
dashboard/
├── app.py
├── requirements.txt
└── .env.example
```

The dashboard architecture can be extended to provide interactive visualizations for:

* Store performance
* Inventory status
* Product demand
* Order trends
* Business KPIs

---

## 🔐 Environment Configuration

Sensitive credentials should not be committed to the repository.

The project includes:

```text
dashboard/.env.example
```

Create your own `.env` file locally using the example configuration.

```text
Do not commit passwords, API keys, database credentials, or other secrets to GitHub.
```

---

## 🔮 Future Enhancements

The project can be extended with:

* 📊 Interactive analytics dashboard
* 📈 Revenue forecasting
* 🤖 Demand forecasting
* 👥 Customer segmentation
* 🛍️ Product recommendation system
* 📦 Inventory demand prediction
* 🚨 Automated low-stock alerts
* 🏪 Advanced store performance dashboards
* 📅 Time-series sales analysis
* ☁️ Cloud database deployment
* 🔄 Automated ETL pipelines

---

## 📚 Learning Outcomes

This project demonstrates practical experience in:

* Relational database design
* SQL database creation
* Data loading and validation
* Multi-table joins
* Data aggregation
* Conditional analysis
* Business KPI development
* Inventory analytics
* Sales analytics
* Store performance analysis
* Customer analytics
* Translating business questions into SQL queries
* Structuring an analytics project for GitHub

---

## 🎓 Project Skills Demonstrated

```text
SQL
MySQL
Database Design
Relational Databases
Data Analytics
Business Intelligence
Inventory Analytics
Sales Analytics
Customer Analytics
Data Modeling
ETL Concepts
Python
Streamlit
Git
GitHub
```

---

## 👩‍💻 Author

### Bhuvaneswari

B.Tech Computer Science & Engineering

GitHub:
[https://github.com/Bhuvaneswari123463](https://github.com/Bhuvaneswari123463)

---

## ⭐ Project Focus

**MySQL • SQL • Data Analytics • Business Intelligence • Inventory Analytics • Sales Analytics • Relational Database Design**

---

## 📄 License

This project is intended for educational, portfolio, and demonstration purposes.

```

**This is the complete version**. Paste the entire block into your GitHub `README.md` editor and commit it.
```
