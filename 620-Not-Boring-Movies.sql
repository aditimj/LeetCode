# Write your MySQL query statement below
select * from Cinema 
WHERE 
MOD(id,2) <> 0 and description <> 'boring' 
order by rating DESC