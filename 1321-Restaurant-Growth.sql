# Write your MySQL query statement below
select visited_on, 
    (
      select SUM(amount) from Customer
        where 
        visited_on between DATE_SUB(c.visited_on, INTERVAL 6 DAY) and c.visited_on
    ) as amount,
    round((
        select SUM(amount)/ 7 from customer
        where 
        visited_on between DATE_SUB(c.visited_on, interval 6 day) and c.visited_on
    ),2) as average_amount

FROM Customer c
where visited_on >= 
    ( Select Date_add(min(visited_on), interval 6 day)
    from Customer)
group by visited_on
order by visited_on