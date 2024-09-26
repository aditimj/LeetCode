# Write your MySQL query statement below
select id, CASE
        WHEN p_id is null then \Root\
        WHEN id in (Select p_id from Tree) then \Inner\ 
        ELSE \Leaf\ END as type 
from Tree group by id