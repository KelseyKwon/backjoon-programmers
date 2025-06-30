-- 코드를 입력하세요
-- 입양간 기록 기록, 보호소에 들어온 기록이 없는 것.
SELECT a.ANIMAL_ID, a.NAME
from ANIMAL_OUTS as a left outer join ANIMAL_INS as b
on a.ANIMAL_ID = b.ANIMAL_ID
where b.INTAKE_CONDITION is null
