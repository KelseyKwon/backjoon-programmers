-- 코드를 작성해주세요
-- 길이가 10 이하면 => LENGTH = NULL IFNULL(LENGTH, 10)
-- group by FISH_TYPE -> LENGTH가 가장 큰 물고기의 a.ID, b.FISH_NAME, a.LENGTH
with deleted_null as (
    select ID, FISH_TYPE, IFNULL(LENGTH, 10) as LENGTH, TIME
from FISH_INFO as a
)
select a.ID, b.FISH_NAME, a.LENGTH
from deleted_null as a
join FISH_NAME_INFO as b on a.FISH_TYPE = b.FISH_TYPE
where (a.FISH_TYPE, a.LENGTH) in (select FISH_TYPE, max(LENGTH) from deleted_null group by FISH_TYPE)
order by a.ID asc