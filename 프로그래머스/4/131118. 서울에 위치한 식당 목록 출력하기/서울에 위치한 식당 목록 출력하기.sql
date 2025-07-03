-- 코드를 입력하세요
-- ADDRESS = '서울' 
-- REST_ID, a.REST_NAME, a.FOOD_TYPE, a.FAVORITES, a.ADDRESS, 
-- group by REST_ID -> sum(REVIEW_SCORE) / count(*)
with in_seoul as (
select *
from REST_INFO
where ADDRESS like '서울%'
)
select a.REST_ID, a.REST_NAME, a.FOOD_TYPE, a.FAVORITES, a.ADDRESS, round(sum(b.REVIEW_SCORE) / count(DISTINCT b.REVIEW_ID), 2) as AVG_SCORE
from in_seoul a
join REST_REVIEW b on a.REST_ID = b.REST_ID
group by a.REST_ID, a.REST_NAME, a.FOOD_TYPE, a.FAVORITES, a.ADDRESS
order by AVG_SCORE desc, a.FAVORITES desc