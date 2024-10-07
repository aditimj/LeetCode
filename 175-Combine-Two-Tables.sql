# Write your MySQL query statement below
SELECT Person.firstName, Person.lastName, Address.city, Address.state 
FROM Person
Left join Address on
Person.personID = Address.personID
