-- 코드를 입력하세요
-- 들어올때 SEX_UPON_INTAKE가 INTACT, 나갈떄 SEX_UPON_OUTCOME이 neutered or spayed인거.
SELECT a.ANIMAL_ID, a.ANIMAL_TYPE, a.NAME
from ANIMAL_INS as a join ANIMAL_OUTS as b
on a.ANIMAL_ID = b.ANIMAL_ID
where a.SEX_UPON_INTAKE like 'Intact%' and (b.SEX_UPON_OUTCOME like 'Neutered%' or b.SEX_UPON_OUTCOME like 'Spayed%')