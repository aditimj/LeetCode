# Write your MySQL query statement below
with new_table as (
   SELECT id,
   student,
   ROW_NUMBER() OVER(ORDER BY id) as row_num,
    COUNT(*) over() as total_rows
    from Seat
)
SELECT id,
    CASE 
        WHEN (row_num % 2 <> 0) AND row_num < total_rows THEN LEAD(student) OVER(ORDER BY row_num)
        WHEN (row_num % 2 = 0) and row_num < total_rows then LAG(student) OVER(ORDER BY row_num)
        WHEN (row_num % 2 = 0) and row_num = total_rows then LAG(student) OVER(ORDER BY row_num)
        ELSE student
    END as student
    from new_table
order by id ASC

