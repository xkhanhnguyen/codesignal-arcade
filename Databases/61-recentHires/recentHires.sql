CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT name as names FROM
    (
        (SELECT 1 department, name FROM pr_department ORDER BY date_joined DESC LIMIT 5) 
        UNION ALL
        (SELECT 2, name FROM it_department ORDER BY date_joined DESC LIMIT 5)
        UNION ALL
        (SELECT 3, name FROM sales_department ORDER BY date_joined DESC LIMIT 5)
    ) names 
    ORDER BY department, name;
END

