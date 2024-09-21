# Write your MySQL query statement below
select query_name, 
    round(Avg(rating/position),2) as quality, 
    round((count(CASE WHEN rating < 3 then 1 end) / count(query_name)) * 100,2) as poor_query_percentage 
from Queries 
where query_name is not null 
group by query_name