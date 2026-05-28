-- 코드를 입력하세요
-- a/c.CAR_TYPE = '트럭' 대여기록 별로 group by HISTORY_ID 
-- order by FEE desc, HISTORY_ID desc
with rental as (
    select 
    b.HISTORY_ID, 
    a.DAILY_FEE, 
    DATEDIFF(b.END_DATE, b.START_DATE) + 1 as rental_days,
    case
        when DATEDIFF(b.END_DATE, b.START_DATE) + 1 >= 90 then '90일 이상'
        when DATEDIFF(b.END_DATE, b.START_DATE) + 1 >= 30 then '30일 이상'
        when DATEDIFF(b.END_DATE, b.START_DATE) + 1 >= 7 then '7일 이상'
        else null
    end as DURATION_TYPE
    from CAR_RENTAL_COMPANY_CAR as a 
    join CAR_RENTAL_COMPANY_RENTAL_HISTORY as b on a.CAR_ID = b.CAR_ID and a.CAR_TYPE = '트럭'
)
select a.HISTORY_ID, (a.rental_days * a.DAILY_FEE * (100-IFNULL(b.DISCOUNT_RATE, 0)) / 100) as FEE
from rental as a left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as b on a.DURATION_TYPE = b.DURATION_TYPE and b.CAR_TYPE = '트럭'
order by FEE desc, a.HISTORY_ID desc;
