-- 코드를 입력하세요
-- CAR_TYPE = '트럭'
-- HISTORY_ID별로 대여금액을 구하새ㅓ
-- HISTORY_ID, FEE
-- FEE desc, HISTORY_ID desc
# WITH rental_day AS (
#     SELECT HISTORY_ID, CAR_ID, DATEDIFF(END_DATE, START_DATE) + 1 AS total_rental_day
#     FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# ),
# rental_truck_day AS (
#     SELECT 
#         a.HISTORY_ID,
#         a.total_rental_day AS total_day,
#         b.DAILY_FEE * a.total_rental_day AS total_fee
#     FROM rental_day a
#     JOIN CAR_RENTAL_COMPANY_CAR b ON a.CAR_ID = b.CAR_ID
#     WHERE b.CAR_TYPE = '트럭'
# )
# SELECT 
#     HISTORY_ID,
#     FLOOR(
#         CASE 
#             WHEN total_day >= 90 THEN total_fee * 0.9
#             WHEN total_day >= 30 THEN total_fee * 0.93
#             WHEN total_day >= 7 THEN total_fee * 0.95
#             ELSE total_fee
#         END
#     ) AS FEE
# FROM rental_truck_day
# ORDER BY FEE DESC, HISTORY_ID DESC;


with rental as (
select a.HISTORY_ID, 
    b.DAILY_FEE,
    b.CAR_TYPE,
    DATEDIFF(a.END_DATE, a.START_DATE) + 1 as days,
    case
        when DATEDIFF(END_DATE, START_DATE) + 1 >= 90 then '90일 이상'
        when DATEDIFF(END_DATE, START_DATE) + 1 >= 30 then '30일 이상'
        when DATEDIFF(END_DATE, START_DATE) + 1 >= 7 then '7일 이상'
        else '없음'
    end as DURATION_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY as a
join CAR_RENTAL_COMPANY_CAR as b on a.CAR_ID = b.CAR_ID and b.CAR_TYPE = '트럭'
)
select HISTORY_ID, FLOOR((100 - IFNULL(b.DISCOUNT_RATE, 0)) / 100 * a.DAILY_FEE * a.days) as FEE
from rental as a
left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as b on a.DURATION_TYPE = b.DURATION_TYPE and a.CAR_TYPE = b.CAR_TYPE
order by FEE desc, a.HISTORY_ID desc