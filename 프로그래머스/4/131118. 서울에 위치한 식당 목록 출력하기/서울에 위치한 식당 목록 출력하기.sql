-- 코드를 입력하세요
-- ADDRESS LIKE "서울%" -> a.REST_ID, a.REST_NAME, a.FOOD_TYPE, a.FAVORITES, a.ADDRESS, avg(b.REVIEW_SCORE) -> group by a.REST_ID round(avg(b.REVIEW_SCORE), 2)
-- order by SCORE desc, FAVORITES desc
SELECT a.REST_ID, a.REST_NAME, a.FOOD_TYPE, a.FAVORITES, a.ADDRESS, round(avg(b.REVIEW_SCORE), 2) as SCORE
from REST_INFO as a
join REST_REVIEW as b on a.REST_ID = b.REST_ID
where a.ADDRESS like "서울%"
group by a.REST_ID, a.REST_NAME, a.FOOD_TYPE, a.FAVORITES, a.ADDRESS
order by SCORE desc, FAVORITES desc