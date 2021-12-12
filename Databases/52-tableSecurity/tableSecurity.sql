CREATE PROCEDURE tableSecurity()
BEGIN
    CREATE OR REPLACE VIEW emp
    AS SELECT id, name, YEAR(date_joined) as date_joined, '-' as salary FROM employees;

    SELECT id, name, date_joined, salary
    FROM emp
    ORDER BY id;
END

-- These keywords serve to create or replace the existing View. 
-- When we run the create or the replace view statement, 
-- MySQL checks whether it exists in the database. 
-- If the View exists, it changes the View definition using 
-- the query specified after the AS keyword.