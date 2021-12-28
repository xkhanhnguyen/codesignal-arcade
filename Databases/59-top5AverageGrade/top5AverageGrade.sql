CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT ROUND(AVG(grade),2) as average_grade
    FROM (SELECT grade from students ORDER by grade DESC LIMIT 5) top5;
    -- ERROR 1248 (42000): Every derived table must have its own alias
    --  need to name an alia -- top5
END