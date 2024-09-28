-- Write your PostgreSQL query statement below
WITH temp as((SELECT u.name as name, COUNT(mr.rating) as rating FROM Users u LEFT JOIN MovieRating mr ON u.user_id = mr.user_id
GROUP BY u.name ORDER BY rating DESC, u.name LIMIT 1)
UNION ALL
(SELECT  m.title as name,AVG(mr.rating) as rating FROM Movies m LEFT JOIN MovieRating mr ON m.movie_id = mr.movie_id
WHERE mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY m.title ORDER BY rating DESC, m.title LIMIT 1))

SELECT name as results FROM temp