
import os
import pandas as pd
import streamlit as st
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Quick-Commerce Analytics", page_icon="🛒", layout="wide")
st.title("🛒 Quick-Commerce Store Inventory & Sales Analytics")
st.caption("Operational dashboard for store managers — sales, orders, inventory and product performance")

@st.cache_resource
def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "quick_commerce")
    )

@st.cache_data(ttl=60)
def query(sql):
    conn = get_connection()
    return pd.read_sql(sql, conn)

kpi = query("""
SELECT
  COUNT(DISTINCT o.order_id) total_orders,
  SUM(o.status='Delivered') delivered_orders,
  SUM(o.status='Cancelled') cancelled_orders,
  ROUND(100.0*SUM(o.status='Cancelled')/COUNT(DISTINCT o.order_id),2) cancellation_rate,
  ROUND(SUM(CASE WHEN o.status='Delivered' THEN oi.line_total ELSE 0 END),2) revenue
FROM orders o JOIN order_items oi ON o.order_id=oi.order_id
""").iloc[0]

c1,c2,c3,c4,c5=st.columns(5)
c1.metric("Total Orders", int(kpi.total_orders))
c2.metric("Delivered", int(kpi.delivered_orders))
c3.metric("Revenue", f"₹{kpi.revenue:,.0f}")
c4.metric("Cancellation Rate", f"{kpi.cancellation_rate:.2f}%")
low = query("SELECT COUNT(*) low_stock FROM inventory WHERE stock_qty <= reorder_level").iloc[0,0]
c5.metric("Low Stock SKUs", int(low))

st.divider()

left,right=st.columns(2)

with left:
    st.subheader("Top Fast-Moving Products")
    top = query("""
    SELECT p.product_name, SUM(oi.quantity) units_sold
    FROM order_items oi JOIN orders o ON oi.order_id=o.order_id
    JOIN products p ON oi.product_id=p.product_id
    WHERE o.status='Delivered'
    GROUP BY p.product_id,p.product_name
    ORDER BY units_sold DESC LIMIT 10
    """).set_index("product_name")
    st.bar_chart(top)

with right:
    st.subheader("Revenue by Category")
    cat = query("""
    SELECT c.category_name, ROUND(SUM(oi.line_total),2) revenue
    FROM order_items oi JOIN orders o ON oi.order_id=o.order_id
    JOIN products p ON oi.product_id=p.product_id
    JOIN categories c ON p.category_id=c.category_id
    WHERE o.status='Delivered'
    GROUP BY c.category_id,c.category_name
    ORDER BY revenue DESC
    """).set_index("category_name")
    st.bar_chart(cat)

st.subheader("Store Performance")
store = query("""
SELECT s.store_name,
 COUNT(DISTINCT o.order_id) total_orders,
 SUM(o.status='Delivered') delivered_orders,
 SUM(o.status='Cancelled') cancelled_orders,
 ROUND(100.0*SUM(o.status='Cancelled')/COUNT(DISTINCT o.order_id),2) cancellation_rate,
 ROUND(SUM(CASE WHEN o.status='Delivered' THEN oi.line_total ELSE 0 END),2) revenue
FROM stores s LEFT JOIN orders o ON s.store_id=o.store_id
LEFT JOIN order_items oi ON o.order_id=oi.order_id
GROUP BY s.store_id,s.store_name ORDER BY revenue DESC
""")
st.dataframe(store, use_container_width=True, hide_index=True)

a,b=st.columns(2)
with a:
    st.subheader("Low-Stock Items")
    low_df=query("""
    SELECT s.store_name,p.product_name,i.stock_qty,i.reorder_level
    FROM inventory i JOIN stores s ON i.store_id=s.store_id
    JOIN products p ON i.product_id=p.product_id
    WHERE i.stock_qty <= i.reorder_level
    ORDER BY i.stock_qty ASC
    LIMIT 20
    """)
    st.dataframe(low_df,use_container_width=True,hide_index=True)
with b:
    st.subheader("Peak Ordering Hours")
    hours=query("""
    SELECT HOUR(order_datetime) order_hour, COUNT(*) order_count
    FROM orders GROUP BY HOUR(order_datetime) ORDER BY order_hour
    """).set_index("order_hour")
    st.line_chart(hours)

st.subheader("Pending / Processing Orders")
pending=query("""
SELECT o.order_id,s.store_name,o.order_datetime,o.status
FROM orders o JOIN stores s ON o.store_id=s.store_id
WHERE o.status IN ('Pending','Processing')
ORDER BY o.order_datetime DESC
LIMIT 20
""")
st.dataframe(pending,use_container_width=True,hide_index=True)
