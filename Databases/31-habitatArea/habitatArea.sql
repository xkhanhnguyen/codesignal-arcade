CREATE PROCEDURE habitatArea()
BEGIN
    SELECT ST_AREA(
            ST_ConvexHull(
                ST_GeomFromText(
                    CONCAT('MULTIPOINT(', GROUP_CONCAT(x, ' ', y),')')
                ) 
            )
    ) as area
    FROM places;

END
