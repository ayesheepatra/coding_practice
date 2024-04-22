# Write your MySQL query statement below
SELECT distinct l2.num as ConsecutiveNums
FROM Logs l1 JOIN Logs l2 
JOIN Logs l3 
WHERE l2.id=l1.id+1 AND l2.id=l3.id-1
AND l1.num=l2.num and l2.num=l3.num
#group by l2.num
#having count(*)>=3
