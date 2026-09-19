
USE quick_commerce;

-- 1. KPI summary
SELECT
    COUNT(*) AS total_orders,
    SUM(status='Delivered') AS delivered_orders,
    SUM(status='Cancelled') AS cancelled_orders,
    ROUND(100.0 * SUM(status='Cancelled') / COUNT(*), 2) AS cancellation_rate_pct,
    ROUND(SUM(CASE WHEN status='Delivered' THEN oi.line_total ELSE 0 END), 2) AS delivered_revenue
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id;

-- 2. Fast-moving products
SELECT p.product_id, p.product_name,
       SUM(oi.quantity) AS units_sold,
       ROUND(SUM(oi.line_total),2) AS revenue
FROM order_items oi
JOIN orders o ON oi.order_id=o.order_id
JOIN products p ON oi.product_id=p.product_id
WHERE o.status='Delivered'
GROUP BY p.product_id, p.product_name
ORDER BY units_sold DESC
LIMIT 10;

-- 3. Low-stock products by store
SELECT s.store_name, p.product_name, i.stock_qty, i.reorder_level,
       (i.reorder_level-i.stock_qty) AS units_below_reorder
FROM inventory i
JOIN stores s ON i.store_id=s.store_id
JOIN products p ON i.product_id=p.product_id
WHERE i.stock_qty <= i.reorder_level
ORDER BY units_below_reorder DESC, s.store_name;

-- 4. Store performance
SELECT s.store_name,
       COUNT(DISTINCT o.order_id) AS total_orders,
       SUM(CASE WHEN o.status='Delivered' THEN 1 ELSE 0 END) AS delivered_orders,
       SUM(CASE WHEN o.status='Cancelled' THEN 1 ELSE 0 END) AS cancelled_orders,
       ROUND(100.0 * SUM(CASE WHEN o.status='Cancelled' THEN 1 ELSE 0 END)
             / COUNT(DISTINCT o.order_id),2) AS cancellation_rate_pct,
       ROUND(SUM(CASE WHEN o.status='Delivered' THEN oi.line_total ELSE 0 END),2) AS revenue
FROM stores s
LEFT JOIN orders o ON s.store_id=o.store_id
LEFT JOIN order_items oi ON o.order_id=oi.order_id
GROUP BY s.store_id, s.store_name
ORDER BY revenue DESC;

-- 5. Category performance
SELECT c.category_name,
       SUM(oi.quantity) AS units_sold,
       ROUND(SUM(oi.line_total),2) AS revenue
FROM order_items oi
JOIN orders o ON oi.order_id=o.order_id
JOIN products p ON oi.product_id=p.product_id
JOIN categories c ON p.category_id=c.category_id
WHERE o.status='Delivered'
GROUP BY c.category_id, c.category_name
ORDER BY revenue DESC;

-- 6. Peak ordering hours
SELECT HOUR(order_datetime) AS order_hour,
       COUNT(*) AS order_count
FROM orders
GROUP BY HOUR(order_datetime)
ORDER BY order_count DESC;

-- 7. Pending orders
SELECT o.order_id, s.store_name, o.order_datetime, o.status
FROM orders o
JOIN stores s ON o.store_id=s.store_id
WHERE o.status IN ('Pending','Processing')
ORDER BY o.order_datetime;

-- 8. Products with zero delivered sales
SELECT p.product_id, p.product_name
FROM products p
LEFT JOIN order_items oi ON p.product_id=oi.product_id
LEFT JOIN orders o ON oi.order_id=o.order_id AND o.status='Delivered'
GROUP BY p.product_id, p.product_name
HAVING COUNT(o.order_id)=0;

-- 9. Top 3 products per category using a window function
WITH product_sales AS (
    SELECT c.category_name, p.product_name,
           SUM(oi.quantity) AS units_sold,
           SUM(oi.line_total) AS revenue
    FROM order_items oi
    JOIN orders o ON oi.order_id=o.order_id
    JOIN products p ON oi.product_id=p.product_id
    JOIN categories c ON p.category_id=c.category_id
    WHERE o.status='Delivered'
    GROUP BY c.category_name, p.product_name
),
ranked AS (
    SELECT *,
           DENSE_RANK() OVER (PARTITION BY category_name ORDER BY units_sold DESC) AS rnk
    FROM product_sales
)
SELECT * FROM ranked WHERE rnk <= 3 ORDER BY category_name, rnk;

-- 10. Daily sales trend
SELECT DATE(o.order_datetime) AS order_date,
       COUNT(DISTINCT o.order_id) AS orders,
       ROUND(SUM(CASE WHEN o.status='Delivered' THEN oi.line_total ELSE 0 END),2) AS revenue
FROM orders o
JOIN order_items oi ON o.order_id=oi.order_id
GROUP BY DATE(o.order_datetime)
ORDER BY order_date;
