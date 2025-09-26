# Write your MySQL query statement below
# 처음 로그인한 다음날 또 로그인한 사람의 비율을 구하라. round(, 2)
# group by player_id를 하고, 그리고 아니다 -> where 

with first_login as (
    select player_id, min(event_date) as first_date
    from activity
    group by player_id
),
next_day as (
    select f.player_id
    from first_login f
    join Activity a
    on a.player_id = f.player_id
    and a.event_date = DATE_ADD(f.first_date, INTERVAL 1 DAY)
)
select round(count(DISTINCT n.player_id) / count(DISTINCT f.player_id), 2) as fraction
from first_login f
left join next_day n on n.player_id = f.player_id