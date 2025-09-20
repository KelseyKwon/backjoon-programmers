-- 코드를 입력하세요
-- GENDER : NULL or 0 (MALE), 1 (FEMALE)
-- (날짜, 회원 ID, 상품 ID)는 하나의 판매 데이터만
-- JOIN = '2021', ONLINE_SALE에 있고 / JOIN = '2021'을 group by 년, SALES_DATE의 month로 출력하기.
-- 두번째 자리에서 반올림
-- YEAR(SALES_DATE) asc, MONTH(SALES_DATE) desc
-- 
with joined_2021 as (
    select DISTINCT USER_ID
    from USER_INFO
    where YEAR(JOINED) = '2021'
), total_2021 as (
select count(*) as total_user
from joined_2021
)
SELECT 
YEAR(b.SALES_DATE) as YEAR, 
MONTH(b.SALES_DATE) as MONTH, 
count(DISTINCT b.USER_ID) as PURCHASED_USERS, 
ROUND(count(DISTINCT b.USER_ID) * 1.0 / t.total_user, 1) as PURCHASED_RATIO
from joined_2021 as a
join ONLINE_SALE as b on a.USER_ID = b.USER_ID
cross join total_2021 as t
group by YEAR(b.SALES_DATE), MONTH(b.SALES_DATE)
order by YEAR(b.SALES_DATE) asc, MONTH(b.SALES_DATE) asc