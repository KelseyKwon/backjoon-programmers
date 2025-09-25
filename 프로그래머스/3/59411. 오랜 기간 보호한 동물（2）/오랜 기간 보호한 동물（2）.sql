-- 코드를 입력하세요
-- ANIMAL_INS, ANIMAL_OUT을 left outer join했는데 -> b.DATETIME이 null
-- TIMESTAMPDIFF가 가장 긴거. 
-- order by TIMESTAMPDIFF desc limit 2

SELECT a.ANIMAL_ID, a.NAME
from ANIMAL_INS as a
join ANIMAL_OUTS as b on a.ANIMAL_ID = b.ANIMAL_ID
order by TIMESTAMPDIFF(MINUTE, a.DATETIME, b.DATETIME) desc limit 2
