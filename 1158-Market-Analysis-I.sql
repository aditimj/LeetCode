# Write your MySQL query statement below
select Users.user_id as buyer_id, 
    Users.join_date, 
    count(Orders.order_date) as orders_in_2019
from Users
left join Orders on
    Users.user_id = Orders.buyer_id and 
    Orders.order_date between '2019-01-01' and '2019-12-31'
group by Users.user_id