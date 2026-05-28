-- 코드를 입력하세요
-- REVIEW_ID의 리뷰를 조회하는 것.
-- a.MEMBER_NAME, b.REVIEW_TEXT, b.REVIEW_DATE
-- MEMBER_ID로 하고, group by MEMBER_ID 

with top_reviewer as (SELECT count(REVIEW_ID) as REVIEW_COUNT, MEMBER_ID
from REST_REVIEW
group by MEMBER_ID
order by REVIEW_COUNT desc limit 1)

select a.MEMBER_NAME, b.REVIEW_TEXT, b.REVIEW_DATE
from MEMBER_PROFILE as a join REST_REVIEW as b on a.MEMBER_ID = b.MEMBER_ID
where a.MEMBER_ID = (select MEMBER_ID FROM top_reviewer)
order by b.REVIEW_DATE, b.REVIEW_TEXT
