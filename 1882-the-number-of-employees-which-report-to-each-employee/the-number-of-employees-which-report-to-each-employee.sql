# Write your MySQL query statement below
SELECT e.employee_id as employee_id, e.name as name, count(m.employee_id) as reports_count, round(avg(m.age),0) as average_age
FROM Employees e inner join Employees m ON e.employee_id=m.reports_to
GROUP BY m.reports_to
HAVING count(m.employee_id)>0
ORDER BY e.employee_id