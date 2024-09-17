SELECT r.contest_id, round(Count(DISTINCT r.user_id) * 100 / (select count(*) from Users),2) as percentage from Register r
group by r.contest_id
order by 
    percentage desc,
    r.contest_id asc;



-- SELECT 
--     r.contest_id, 
--     ROUND(COUNT(DISTINCT r.user_id) * 100.0 / (SELECT COUNT(*) FROM Users), 2) AS percentage
-- FROM 
--     Register r
-- GROUP BY 
--     r.contest_id
-- ORDER BY 
--     percentage DESC, 
--     r.contest_id ASC;
