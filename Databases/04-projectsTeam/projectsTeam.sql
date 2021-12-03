CREATE PROCEDURE projectsTeam()
BEGIN
	SELECT name from projectLog
    GROUP BY name
    ORDER BY name; 
END