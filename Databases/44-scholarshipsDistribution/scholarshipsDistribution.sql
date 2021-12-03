CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    select candidate_id as student_id
    from candidates
    left join detentions 
        on  candidates.candidate_id = detentions.student_id
        where detentions.detention_date is NULL 
        and detentions.student_id is NULL;
END


