-- Write your SQL query here
select username,
    session_count,
    case 
    when session_count >= 50 then 'Power'
    when session_count >= 10 then 'Casual'
    else 'Dormant'
    END as activity_level,
    case
    when platform in ('ios','android') then 'Mobile'
    when platform in ('web','desktop') then 'Desktop'
    else 'Other'
    end as platform_type 
from user_sessions 
order by 
case activity_level 
    when 'Power' then 1
    WHEN 'Casual'  THEN 2
    ELSE 3
    END,
    username asc;