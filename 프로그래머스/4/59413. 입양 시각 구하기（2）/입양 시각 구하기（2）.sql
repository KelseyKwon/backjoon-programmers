-- 코드를 입력하세요
-- 몇시에 가장 입양이 활발하게 일어나는지
-- 0시부터 23시까지 입양이 몇 건이나 발생했는지 조회
-- 시간대 순으로 정렬
# select HOUR(DATETIME) as HOUR, 
# case
#     when count(DISTINCT ANIMAL_ID) = 0 then 0
#     else count(DISTINCT ANIMAL_ID)
# end as COUNT
# from ANIMAL_OUTS
# group by HOUR(now)
# order by HOUR(DATETIME) asc

WITH RECURSIVE TIMETABLE (HOUR) AS (
    SELECT 0
    UNION
    SELECT HOUR + 1 FROM TIMETABLE WHERE HOUR < 23
)
select a.HOUR, count(DISTINCT ANIMAL_ID) as COUNT
from TIMETABLE as a
left join ANIMAL_OUTS as b on a.HOUR = HOUR(b.DATETIME)
group by a.HOUR
order by a.HOUR