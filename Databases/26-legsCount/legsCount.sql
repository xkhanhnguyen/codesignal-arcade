DROP PROCEDURE IF EXISTS legsCount;
CREATE PROCEDURE legsCount()
    SELECT sum(
    CASE
        WHEN type = 'dog' THEN 4
        WHEN type = 'cat' THEN 4
        ELSE 2
    END)  as summary_legs
    FROM creatures
    ORDER BY id;