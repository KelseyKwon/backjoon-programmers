-- 코드를 입력하세요
-- SALES_DATE = 2022-01
-- AUTHOR_ID별, CATEGORY별 매출액 TOTALSALES = c.BOOK_SALES * a.PRICE
-- AUTHOR_ID, AUTHOR_NAME, a.CATEGORY, SALES
-- AUTHOR_ID asc, CATEGORY desc
with january_book as (
    select BOOK_ID, sum(SALES) as SALES_SUM
    from BOOK_SALES 
    where YEAR(SALES_DATE) = '2022' and MONTH(SALES_DATE) = '01'
    group by BOOK_ID
)
select a.AUTHOR_ID, b.AUTHOR_NAME, a.CATEGORY, sum(c.SALES_SUM * a.PRICE) as TOTAL_SALES
from january_book c
join BOOK a on c.BOOK_ID = a.BOOK_ID
join AUTHOR b on a.AUTHOR_ID = b.AUTHOR_ID
group by a.AUTHOR_ID, b.AUTHOR_NAME, a.CATEGORY
order by a.AUTHOR_ID asc, a.CATEGORY desc