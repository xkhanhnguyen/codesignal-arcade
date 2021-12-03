CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT
        year(date) as year,
        quarter(date) as quarter,
        SUM(profit) - SUM(loss) as net_profit
    FROM accounting
    group by year, quarter;
        
END

