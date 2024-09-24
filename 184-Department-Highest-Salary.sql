SELECT Department.name AS Department,
       Employee.name AS Employee,
       Employee.salary AS Salary FROM Employee JOIN Department ON Employee.departmentId = Department.id WHERE Employee.salary = (SELECT MAX(salary) FROM Employee AS e WHERE e.departmentId = Employee.departmentId);
