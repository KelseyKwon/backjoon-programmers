-- 코드를 입력하세요
-- ANIMAL_OUTS에 존재하는데, ANIMAL_INS에 없는 테이블
-- order by ANIMAL_ID ANIMAL_OUTS.NAME
SELECT b.ANIMAL_ID, b.NAME
from ANIMAL_OUTS b 
left outer join ANIMAL_INS a on a.ANIMAL_ID = b.ANIMAL_ID
where a.ANIMAL_ID is null
order by b.ANIMAL_ID