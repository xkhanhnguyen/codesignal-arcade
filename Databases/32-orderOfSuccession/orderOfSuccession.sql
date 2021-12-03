CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT IF( gender='F' , concat('Queen', ' ', name),
          concat('King',' ',  name)
         ) AS name
         FROM Successors
    ORDER BY birthday;
    
END



-- CREATE PROCEDURE solution()
-- BEGIN
--     Select CONCAT(CASE 
--                   WHEN gender = "F"
--                   THEN "Queen "
--                   ELSE "King " END,name)
--                     AS name
--     FROM Successors
--     ORDER BY birthday;
-- END