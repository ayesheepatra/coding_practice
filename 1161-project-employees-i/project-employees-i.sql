# Write your MySQL query statement below
SELECT p.project_id, round(avg(experience_years),2) as average_years
FROM Employee e JOIN Project p ON e.employee_id=p.employee_id
#WHERE p.project_id IS NOT NULL
GROUP BY p.project_id