-- 코드를 입력하세요
-- CATEGORY = '경제'
with economy_book as (
    select BOOK_ID, AUTHOR_ID, PUBLISHED_DATE
    from BOOK
    where CATEGORY = '경제'
)
SELECT a.BOOK_ID, b.AUTHOR_NAME, DATE_FORMAT(a.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
from economy_book a
join AUTHOR b on a.AUTHOR_ID = b.AUTHOR_ID
order by a.PUBLISHED_DATE asc