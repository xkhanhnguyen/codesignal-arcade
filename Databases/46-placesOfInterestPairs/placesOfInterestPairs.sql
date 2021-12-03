CREATE PROCEDURE solution()
BEGIN
    SELECT 
        a.name as place1,
        b.name as place2
    from sights a, sights b
    where a.name < b.name
        and power (((power((a.x - b.x), 2)) + (power ((a.y - b.y),2))), 0.5) < 5 
    order by place1, place2;
END

