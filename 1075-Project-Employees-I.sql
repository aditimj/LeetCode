# Write your MySQL query statement below
SELECT Project.project_id, round(SUM(Employee.experience_years) / COUNT(Project.project_id) , 2) as  average_years FROM Project
join Employee on Project.employee_id = Employee.employee_id group by Project.project_id