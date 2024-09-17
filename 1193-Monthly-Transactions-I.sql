# Write your MySQL query statement below
select concat(EXTRACT(YEAR from trans_date), '-', LPAD(EXTRACT(MONTH FROM trans_date), 2, '0')) as month, 
        country, 
        count(state) as trans_count, 
        SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) as approved_count, 
        SUM(amount) as trans_total_amount, SUM(CASE WHEN state = 'approved' then amount else 0 end) AS approved_total_amount from Transactions
group by month,country 