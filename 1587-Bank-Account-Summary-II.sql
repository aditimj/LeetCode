# Write your MySQL query statement below
SELECT Users.name, 
        SUM(Transactions.amount) as balance from Users
JOIN Transactions ON
    Users.account = Transactions.account
group by Users.name
having balance > 10000
