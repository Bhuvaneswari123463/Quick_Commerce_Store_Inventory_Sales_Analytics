# Quick-Commerce Store Inventory & Sales Analytics

## Objective
A Blinkit-style operational analytics project that uses MySQL and SQL to help a store manager understand:
- stock availability
- fast-moving products
- pending/cancelled orders
- store-wise sales
- category performance
- peak ordering hours
- replenishment needs

## Tech Stack
- MySQL
- SQL (JOIN, GROUP BY, HAVING, CTE, subqueries, window functions)
- Python
- Pandas
- Streamlit

## Database
Tables:
`stores`, `categories`, `products`, `customers`, `inventory`, `orders`, `order_items`

## Run it

### 1. Create database and load sample data
Open MySQL Workbench and run:
`sql/01_schema_and_seed.sql`

### 2. Practice the analytics
Run:
`sql/02_analytics_queries.sql`

### 3. Start dashboard
```bash
cd dashboard
pip install -r requirements.txt
copy .env.example .env
```
Edit `.env` with your MySQL password.

Then:
```bash
streamlit run app.py
```

## Interview Story
"I built a quick-commerce operational analytics platform using MySQL. I modeled stores, products, inventory and orders as relational tables and wrote SQL queries to identify fast-moving products, low-stock SKUs, cancellation rates, store performance and peak order hours. I then exposed those metrics in a Streamlit dashboard so a store manager can use the data for operational decisions."

## Important SQL concepts to prepare
- INNER JOIN / LEFT JOIN
- GROUP BY / HAVING
- CASE WHEN
- CTEs
- Window functions
- Aggregate functions
- Date and time functions
- Indexing
- Primary/foreign keys
- Normalization
