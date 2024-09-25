SELECT 
    all_categories.category, 
    COALESCE(COUNT(categorized_accounts.account_id), 0) AS accounts_count
FROM (
    SELECT 
        CASE 
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'
            ELSE 'High Salary'
        END AS category,
        account_id
    FROM Accounts
) AS categorized_accounts
RIGHT JOIN (
    SELECT 'Low Salary' AS category
    UNION ALL
    SELECT 'Average Salary'
    UNION ALL
    SELECT 'High Salary'
) AS all_categories ON categorized_accounts.category = all_categories.category GROUP BY all_categories.category;
