-- 코드를 입력하세요
-- CAR_TYPE = '세단' 
-- DATE_FORMAT()
SELECT distinct a.CAR_ID
from CAR_RENTAL_COMPANY_CAR as a
join CAR_RENTAL_COMPANY_RENTAL_HISTORY as b on a.CAR_ID = b.CAR_ID
where MONTH(b.START_DATE) = 10 and a.CAR_TYPE = '세단'
order by CAR_ID desc