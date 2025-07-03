-- 코드를 입력하세요
-- GENDER는 0 or 1 or NULL
-- SALES_DATE, USER_ID, PRODUCT_ID 조합에 대해서는 판매 데이터가 하나만
-- SALES_DATE 년, 월, 성별을 기준을로 오름차순
-- GENdER가 NULL이면 제외하기
with yes_gender as (
select *
from USER_INFO
where GENDER is NOT NULL
)
select YEAR(SALES_DATE) as YEAR, MONTH(SALES_DATE) as MONTH, a.GENDER, count(DISTINCT a.USER_ID) as USERS
from ONLINE_SALE b
join yes_gender a on a.USER_ID = b.USER_ID
group by YEAR(SALES_DATE), MONTH(SALES_DATE), a.GENDER
order by YEAR(SALES_DATE) asc, MONTH(SALES_DATE) asc, GENDER asc