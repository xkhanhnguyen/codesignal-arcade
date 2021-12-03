CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    select* from phone_numbers
    where phone_number REGEXP '^1-[0-9]{3}-[0-9]{3}-[0-9]{4}$' 
            OR phone_number REGEXP '^\\(1\\)[0-9]{3}-[0-9]{3}-[0-9]{4}$'
    ORDER BY surname;
END

-- REGEXP: regular expression. If the pattern finds a match in the expression, the function returns 1, else it returns 0.