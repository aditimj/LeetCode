# Write your MySQL query statement below
select t1.name from Employee t1
join Employee t2 on 
t1.id = t2.managerId
GROUP BY t1.id, t1.name
HAVING COUNT(t2.managerId) >= 5;