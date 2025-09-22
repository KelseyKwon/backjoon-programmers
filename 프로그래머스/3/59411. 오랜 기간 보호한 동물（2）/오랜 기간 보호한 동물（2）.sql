-- 코드를 입력하세요
-- ANIMAL_OUTS에 있는 animal 중, ANIMAL_OUTS의 DATETIME - ANIMAL_INS의 DATETIME이 가장 긴 동물 두 마리의 a/b.ANIMAL_ID, a/b.NAME
SELECT a.ANIMAL_ID, a.NAME
from ANIMAL_OUTS as a
inner join ANIMAL_INS as b on a.ANIMAL_ID = b.ANIMAL_ID
order by (a.DATETIME - b.DATETIME) desc limit 2