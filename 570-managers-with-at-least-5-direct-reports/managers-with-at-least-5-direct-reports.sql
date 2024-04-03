# Write your MySQL query statement below
select name FROM Employee
where id in (select managerId 
    FROM Employee
    group by managerId
    having count(*)>=5)