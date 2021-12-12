CREATE PROCEDURE studentsInClubs()
    SELECT * FROM students
    WHERE EXISTS (
        SELECT clubs.id FROM clubs WHERE 
        students.club_id = clubs.id
    )
    ORDER BY students.id;