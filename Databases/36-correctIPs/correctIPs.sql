-- CREATE PROCEDURE solution()
-- BEGIN
-- 	/* Write your SQL here. Terminate each statement with a semicolon. */
--     SELECT id, ip
--     FROM ips
--     WHERE IS_IPV4(ip)
--     AND length(SUBSTRING_INDEX(ip, '.', -2)) > 3
--     ORDER BY id;
-- END

CREATE PROCEDURE solution()
BEGIN
    SELECT * 
        FROM ips 
        WHERE is_ipv4(ip) AND ip NOT IN ("1.1.1.1", "0.0.0.0")
        ORDER BY id;
END