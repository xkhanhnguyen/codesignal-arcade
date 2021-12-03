CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    select users.id, IFNULL(cities.country, 'unknown') as country
    from users
    left join cities
        on users.city = cities.city
    
    
    GROUP BY id;
END