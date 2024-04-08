# Write your MySQL query statement below
SELECT p.product_id, IFNULL(round(sum(u.units*p.price)/sum(u.units),2),0) as average_price
FROM Prices p LEFT JOIN UnitsSold u on p.product_id=u.product_id AND
u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY product_id