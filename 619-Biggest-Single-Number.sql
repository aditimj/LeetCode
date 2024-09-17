# Write your MySQL query statement below
select max(num) as num
FROM
(
    select num from MyNumbers
    group by num
    having count(*) = 1
) as sn

