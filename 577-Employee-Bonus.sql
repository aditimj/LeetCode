# Write your MySQL query statement below
select Employee.name, Bonus.bonus from Employee LEFT JOIN Bonus  on Employee.empId = Bonus.empId  where bonus < 1000 OR Bonus.bonus IS NULL
 
