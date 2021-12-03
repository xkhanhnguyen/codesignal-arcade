CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT  
        round(sum(
            power (((power((a.x - b.x), 2)) + (power ((a.y - b.y),2))), 0.5)
        ), 9) as total 
    FROM cities a, cities b
    where a.Id = b.Id + 1
    order by a.Id, b.Id;
    
END


