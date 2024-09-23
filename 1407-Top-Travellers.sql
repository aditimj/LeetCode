# Write your MySQL query statement below
select Users.name, COALESCE(SUM(Rides.distance),0) as travelled_distance from Users
left join Rides on 
Users.id = Rides.user_id
group by Users.id
order by travelled_distance DESC, Users.name ASC