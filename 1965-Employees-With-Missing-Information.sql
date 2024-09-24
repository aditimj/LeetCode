# Write your MySQL query statement below
SELECT employee_id from (
select Employees.employee_id from Employees
LEFT JOIN  Salaries ON
Salaries.employee_id = Employees.employee_id
WHERE Salaries.employee_id IS NULL

UNION

select Salaries.employee_id from Salaries
LEFT JOIN  Employees ON
Employees.employee_id = Salaries.employee_id
WHERE Employees.employee_id IS NULL

) as combined
order by employee_id

