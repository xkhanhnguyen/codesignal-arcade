CREATE PROCEDURE coursesDistribution()
BEGIN
    ALTER TABLE groupcourses ADD FOREIGN KEY (course_id)
    REFERENCES courses(id) ON DELETE CASCADE;
    
--     Cascade will work when we delete something on table courses. Any record on table groupcourses that has reference to table courses will be deleted automatically.

-- But when we try to delete on table groupcourses only the table itself is affected and not on the courses

    ALTER TABLE groupexams ADD FOREIGN KEY (course_id)
    REFERENCES courses(id) ON DELETE CASCADE;

    DELETE FROM courses WHERE name LIKE '%-toremove';


    SELECT group_id, course_id
      FROM groupcourses
     UNION
    SELECT group_id, course_id
      FROM groupexams
     ORDER BY group_id, course_id;
END
