CREATE PROCEDURE booksCatalogs()
BEGIN
	SELECT ExtractValue(xml_doc, '/catalog/book[1]/author') as author
    FROM catalogs
    GROUP BY author
    ORDER BY author;
END
