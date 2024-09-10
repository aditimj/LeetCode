# Write your MySQL query statement below
SELECT  Product.product_name, Sales.year, Sales.price from Sales inner JOIN Product on Product.product_id = Sales.product_id;