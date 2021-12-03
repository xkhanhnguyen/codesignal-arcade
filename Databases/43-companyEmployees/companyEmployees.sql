CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    select * from departments, employees
    Order by dep_name, emp_name;
END