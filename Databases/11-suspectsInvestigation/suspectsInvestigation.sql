CREATE PROCEDURE suspectsInvestigation()
BEGIN
	SELECT id, name, surname FROM Suspect
    WEHRE height <= 170 
            AND name LIKE "B%" 
            AND surname LIKE "Gre%_n"
            AND CHARACTER_LENGTH(surname) = 5
    ORDER BY id ASC;
END