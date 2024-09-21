# Write your MySQL query statement below
with counter as (
select customer_number, count(customer_number) as counter from Orders
group by customer_number
order by counter desc
limit 1
)
select Orders.customer_number from Orders
join counter on
counter.customer_number = Orders.customer_number
group by customer_number
