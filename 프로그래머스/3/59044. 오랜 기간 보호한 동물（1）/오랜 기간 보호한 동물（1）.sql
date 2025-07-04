-- 코드를 입력하세요
-- 입양 못보낸 것 (ANIMAL_INS에는 있으나 ANIMAL_OUTS에는 없음)
-- 가장 오래 보호소에 있었던 (DATETIME이 가장 먼저 시작)
-- 3마리의 이름과 보호 시작일
# SELECT a.NAME, a.DATETIME
# from ANIMAL_INS as a left join ANIMAL_OUTS as b 
# on a.ANIMAL_ID = b.ANIMAL_ID
# where b.ANIMAL_ID is null
# order by DATETIME asc
# limit 3
SELECT a.NAME, a.DATETIME
from ANIMAL_INS as a left join ANIMAL_OUTS as b 
on a.ANIMAL_ID = b.ANIMAL_ID
where b.ANIMAL_ID is null
order by DATETIME asc
limit 3