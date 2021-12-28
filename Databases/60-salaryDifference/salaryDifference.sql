CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SET @max_salary = (SELECT MAX(salary) FROM employees);
    SET @min_salary = (SELECT MIN(salary) FROM employees);
    SET @total_max = (SELECT @max_salary * 
                    COUNT(*) FROM employees WHERE salary = @max_salary);
    SET @total_min = (SELECT @min_salary * 
                    COUNT(*) FROM employees WHERE salary = @min_salary);
    SELECT IFNULL(@total_max - @total_min, 0) as salary_diff;
    
END