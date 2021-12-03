
CREATE PROCEDURE expressionsVerification()
BEGIN
    SELECT * FROM expressions
    WHERE operation = '+' and a + b = c
        or operation = '-' and a - b = c
        or operation = '*' and a * b = c
        or operation = '/' and a / b = c;
	
END