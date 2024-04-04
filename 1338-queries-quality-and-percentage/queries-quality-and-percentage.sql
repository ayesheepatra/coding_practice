# Write your MySQL query statement below
SELECT query_name, round(avg(rating/position),2) as quality, round((sum(if(rating<3,1,0))/count(*))*100,2) as poor_query_percentage
FROM Queries
WHERE query_name is not null
GROUP BY query_name