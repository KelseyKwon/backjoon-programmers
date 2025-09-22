-- 코드를 입력하세요
-- ANIMAL_INS에서는 SEX_UPON_INTAKE이 Intact였지만, ANIMAL_OUTS에서는 SEX_UPON_OUTCOME이 Spayed or Neutered인것. -> 
-- ANIMAL_ID, ANIMAL_TYPE, NAME, 
SELECT a.ANIMAL_ID, a.ANIMAL_TYPE, a.NAME
from ANIMAL_INS as a
join ANIMAL_OUTS as b on a.ANIMAL_ID = b.ANIMAL_ID
where a.SEX_UPON_INTAKE like "Intact%" and (b.SEX_UPON_OUTCOME like "Spayed%" or b.SEX_UPON_OUTCOME like "Neutered%")
ORDER BY a.ANIMAL_ID;