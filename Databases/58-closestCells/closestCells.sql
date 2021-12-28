CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT 
        a.id id1,
        (
            SELECT id FROM positions b
            WHERE a.id != b.id
            ORDER BY power(a.x - b.x, 2) + power(a.y - b.y,2)
            LIMIT 1
        ) id2
    FROM positions a;
    -- ORDER BY
    --     a.id;
END