# Write your MySQL query statement below
SELECT DISTINCT num as ConsecutiveNums 
from 
(
    select num,
    LAG(num) OVER (ORDER BY id) as prev,
    LEAD(num) OVER (ORDER BY id) as next
    FROM Logs
) as temp 
where num = prev and num = next