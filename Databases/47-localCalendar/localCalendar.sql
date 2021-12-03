CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    select event_id, 
    (
        case when settings.hours = 24
            then DATE_FORMAT(
                events.date + INTERVAL settings.timeshift MINUTE, "%Y-%m-%d %H:%i"  )
        when settings.hours = 12
            then DATE_FORMAT(
                events.date + INTERVAL settings.timeshift MINUTE, "%Y-%m-%d %h:%i %p" )
        end 
    ) as formatted_date 
    from events
    left join settings
        on events.user_id = settings.user_id
    
    order by event_id;
    
    
END