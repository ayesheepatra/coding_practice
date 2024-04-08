# Write your MySQL query statement below
SELECT contest_id, round((count(distinct user_id)/(select count(*) from Users))*100,2) as percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC