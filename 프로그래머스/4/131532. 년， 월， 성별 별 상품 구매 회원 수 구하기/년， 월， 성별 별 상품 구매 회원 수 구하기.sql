-- 코드를 입력하세요
-- group by YEAR(SALES_DATE), MONTh(SALES_DATE), GENDER, count(USER_ID)
-- GENDER is not null
-- year, month, gender을 기준으로 asc
SELECT YEAR(b.SALES_DATE) as YEAR, MONTH(B.SALES_DATE) as MONTH, a.GENDER, count(distinct a.USER_ID) as USERS
from USER_INFO a
join ONLINE_SALE b on a.USER_ID = b.USER_ID
where a.GENDER is not null
group by YEAR(b.SALES_DATE), MONTH(B.SALES_DATE), a.GENDER