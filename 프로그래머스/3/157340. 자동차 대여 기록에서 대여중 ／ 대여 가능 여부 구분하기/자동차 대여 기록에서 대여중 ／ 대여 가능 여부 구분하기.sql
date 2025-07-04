-- 코드를 입력하세요
-- START_DATE, END_DATE 사이에 '2022-10-16'이 있으면 대여중
-- 대여 가능
select CAR_ID, 
case
    when CAR_ID in (
    SELECT CAR_ID
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
where DATE(START_DATE) <= '2022-10-16' and DATE(END_DATE) >= '2022-10-16'
    ) then '대여중'
    else '대여 가능'
end as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by CAR_ID
order by CAR_ID desc
