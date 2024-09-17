# Write your MySQL query statement below
select c.customer_id from Customer c
group by c.customer_id
having count(distinct product_key)  = (SELECT COUNT(product_key) FROM Product)