-- 코드를 입력하세요
-- (SALES_DATE, OFFLINE_SALE_ID) 에 대해서는 하나의 판매 데이터만
-- PRODUCT_CODE 별 (SALES_AMOUNT * PRICE)의 합계
-- SALES desc, PRODUCT_ID asc
SELECT PRODUCT_CODE , sum(a.PRICE * b.SALES_AMOUNT) as SALES
from PRODUCT a
join OFFLINE_SALE b on a.PRODUCT_ID = b.PRODUCT_ID
group by PRODUCT_CODE
order by SALES desc, a.PRODUCT_CODE asc