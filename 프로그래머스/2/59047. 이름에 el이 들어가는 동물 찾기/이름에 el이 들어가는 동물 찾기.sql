-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
from ANIMAL_INS
where NAME is not null 
and lower(NAME) like '%el%'
and ANIMAL_TYPE = "Dog"
order by NAME;