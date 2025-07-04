-- 코드를 입력하세요
-- PLACES에서 HOST_ID별로 묶고, count가 2 이상이면 HEAVY USER.
with more_than_two as (
select HOST_ID, count(distinct ID) as PLACES_COUNT
FROM PLACES
group by HOST_ID
)
select ID, NAME, HOST_ID
from places
where HOST_ID in (
    select HOST_ID
    from more_than_two
    where PLACES_COUNT >= 2
)
order by ID asc