-- 코드를 작성해주세요
select ID, (
    select count(*)
    from ECOLI_DATA as a
    where ECOLI_DATA.ID = a.PARENT_ID
) as CHILD_COUNT
from ECOLI_DATA
