CREATE PROCEDURE placesOfInterest()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT country,  
        sum(CASE WHEN leisure_activity_type='Adventure park' 
                    THEN number_of_places 
                    ELSE 0
                    END) AS adventure_park, 
        sum(CASE WHEN leisure_activity_type='Golf' 
                    THEN number_of_places
                    ELSE 0 
                    END) AS goft,
        sum(CASE WHEN leisure_activity_type='River cruise' 
                    then number_of_places
                    ELSE 0 
                    end) AS river_cruise,
        sum(CASE WHEN leisure_activity_type='Kart racing' 
                THEN number_of_places
                ELSE 0
                END) AS kart_racing
    
    FROM countryActivities
    GROUP BY country
    ORDER BY country;
        
END
