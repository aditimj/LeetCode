# Write your MySQL query statement below
select Visits.customer_id, count(Visits.visit_id) as count_no_trans from Visits 
left join Transactions on 
Transactions.visit_id = Visits.visit_id  
where Transactions.visit_id is null 
GROUP BY Visits.customer_id;