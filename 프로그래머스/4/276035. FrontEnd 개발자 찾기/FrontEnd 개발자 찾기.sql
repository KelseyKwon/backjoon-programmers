-- 코드를 작성해주세요
-- FrontEnd 스킬을 가진 개발자의 정보 조회
-- b.ID, b.EMAIL, b.FIRST_NAME, b.LAST_NAME
with front_end_code as (select sum(CODE)
from SKILLCODES
group by CATEGORY
having CATEGORY = 'Front End')
select d.ID, d.EMAIL, d.FIRST_NAME, d.LAST_NAME
from DEVELOPERS as d
where d.SKILL_CODE & (select sum(CODE)
from SKILLCODES
group by CATEGORY
having CATEGORY = 'Front End') > 0
order by d.ID asc