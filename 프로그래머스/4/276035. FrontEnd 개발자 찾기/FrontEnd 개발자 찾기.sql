-- 코드를 작성해주세요
-- SKILCODES에서 CATEGORY = Front ENd인 Code들이 포함되어 있으면, 
-- 16 = BIN(16)이 SKILLCODE BIN(...)에 있으면
select ID, EMAIL, FIRST_NAME, LAST_NAME
from DEVELOPERS where SKILL_CODE & (
    select sum(CODE) from SKILLCODES where CATEGORY = 'Front End'
) > 0
order by ID asc