CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT dep_name FROM departments
    WHERE NOT EXISTS ( 
        SELECT department FROM employees
        WHERE departments.Id = employees.department
    );
END

