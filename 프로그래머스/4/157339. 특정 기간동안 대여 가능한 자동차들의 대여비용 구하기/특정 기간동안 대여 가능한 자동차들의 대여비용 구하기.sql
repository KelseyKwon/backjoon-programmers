-- 코드를 입력하세요
-- CAR_TYPE = '세단', 'SUV'
-- 2022-11-01 2022-11-30 까지 없음
-- 25000 * DISCOUNT_RATE  * 30 이 50만원 이상 200만원 미만 (=FEE)

-- FEE desc, CAR_TYPE asc, CAR_ID desc
# with sedan_suv_car as (SELECT *
# FROM CAR_RENTAL_COMPANY_CAR as a join CAR_RENTAL_COMPANY_RENTAL_HISTORY as b
# on a.CAR_ID = b.CAR_ID
# where a.CAR_TYPE in ('세단', 'SUV')),
# rental_able_car as (select *
# from CAR_RENTAL_COMPANY_RENTAL_HISTORY
# where END_DATE < '2022-11-01' or START_DATE > '2022-11-30'
# )
# select k.CAR_ID, k.CAR_TYPE, FEE
# from sedan_suv_car as k 
# join rental_able_car as j on k.CAR_ID = j.CAR_ID
# case when k.CAR_TYPE = '세단' then (k.DAILY_FEE * 0.9 * 30) as FEE
# when k.CAR_TYPE = 'SUV' when (k.DAILY_FEE * 0.92 * 30) as FEE
# where FEE >= 500000 and FEE < 2000000
# order by FEE desc, k.CAR_TYPE asc, k.CAR_ID desc

# WITH sedan_suv_car AS (
#     SELECT DISTINCT
#         a.CAR_ID,
#         a.CAR_TYPE,
#         a.DAILY_FEE
#     FROM CAR_RENTAL_COMPANY_CAR AS a
#     JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS b 
#         ON a.CAR_ID = b.CAR_ID
#     WHERE a.CAR_TYPE IN ('세단', 'SUV')
# ),
# rental_able_car AS (
#     SELECT DISTINCT CAR_ID
#     FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
#     WHERE END_DATE < '2022-11-01' OR START_DATE > '2022-11-30'
# )
# SELECT
#     k.CAR_ID,
#     k.CAR_TYPE,
#     CASE 
#         WHEN k.CAR_TYPE = '세단' THEN k.DAILY_FEE * 0.9 * 30
#         WHEN k.CAR_TYPE = 'SUV' THEN k.DAILY_FEE * 0.92 * 30
#     END AS FEE
# FROM sedan_suv_car AS k
# JOIN rental_able_car AS j ON k.CAR_ID = j.CAR_ID
# GROUP BY k.CAR_ID, k.CAR_TYPE, k.DAILY_FEE

SELECT c.CAR_ID, c.CAR_TYPE, FLOOR(c.DAILY_FEE * (100 - d.DISCOUNT_RATE) / 100 * 30) AS FEE
FROM CAR_RENTAL_COMPANY_CAR c
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN d
ON c.CAR_TYPE = d.CAR_TYPE 
AND d.DURATION_TYPE = '30일 이상'
WHERE c.CAR_TYPE IN ('세단', 'SUV')
AND CAR_ID NOT IN (
    SELECT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE NOT (END_DATE < '2022-11-01' OR START_DATE > '2022-11-30')
) 
AND FLOOR(c.DAILY_FEE * (100 - d.DISCOUNT_RATE) / 100 * 30) BETWEEN 500000 AND 1999999
ORDER BY FEE DESC, CAR_TYPE ASC, CAR_ID DESC;