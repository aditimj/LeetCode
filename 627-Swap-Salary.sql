# Write your MySQL query statement below
update Salary
SET sex = CASE 
        WHEN sex = 'f' then 'm'
        WHEN sex = 'm' then 'f'
END