# Write your MySQL query statement below

with temp as (
select Employee.name as Employee, Employee.salary as Salary, Department.name as Department 
from Employee
left join Department on 
Employee.departmentId = Department.id
),
temp2 as (
select 
Department, Salary, Employee,
 dense_rank() over(partition by Department order by salary desc) as ranked
from temp
)
select 
Department,Employee, Salary from temp2
where ranked in(1,2,3)




