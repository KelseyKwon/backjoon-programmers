-- 코드를 작성해주세요
-- GRADE별 개발자 정보 조회
-- A : FRONT END & Python(Backend) -> JavaScript, React, Vue, Python
-- B : jus C# -> C#
-- c : 그 외 Front END 개발자. -> JavaScript, React, Vue
-- DEVELOPERS.SKILL_CODE and (각요구 스킬 더한 것들을 OR한게) = 각 요구 스킬 OR 한거면 OK
-- 4개 더한거
-- 1개 더한거
-- 3개 더한거

# with A_SKILL as (
#     select sum(CODE) as a_sum
#     from SKILLCODES
#     where CATEGORY = 'Front End' or NAME = 'Python'
#     # group by CATEGORY, NAME
# ), B_SKILL as (
#     select CODE as b_sum
#     from SKILLCODES
#     # group by NAME
#     where NAME = 'C#'
# ), C_SKILL as(
#     select sum(CODE) as c_sum
#     from SKILLCODES
#     # group by CATEGORY
#     where CATEGORY = 'Front End'
# )
# SELECT 
# case
#     when (d.SKILL_CODE & a.a_sum) = a.a_sum then 'A'
#     when (d.SKILL_CODE & b.b_sum) = b.b_sum then 'B'
#     when (d.SKILL_CODE & c.c_sum) = c.c_sum then 'C'
# end as GRADE,
# d.ID,
# d.EMAIL
# from DEVELOPERS as d join A_SKILL as a join B_SKILL as b join C_SKILL as c
# WHERE
#   -- CASE 결과가 NULL이 아닌 애들만
#   (D.SKILL_CODE & A.A_SUM) = A.A_SUM
#   OR (D.SKILL_CODE & B.B_SUM) = B.B_SUM
#   OR (D.SKILL_CODE & C.C_SUM) = C.C_SUM
# ORDER BY GRADE, D.ID;

with get_grade as (
select
case
    when (d.SKILL_CODE & (select sum(CODE) from SKILLCODES where CATEGORY = 'Front End') > 0 and d.SKILL_CODE & (select sum(CODE) from SKILLCODES where NAME = 'Python') > 0) then 'A'
    when (d.SKILL_CODE & (select sum(CODE) from SKILLCODES where NAME = 'C#') > 0) then 'B'
    when (d.SKILL_CODE & (select sum(CODE) from SKILLCODES where CATEGORY = 'Front End') > 0) then 'C'
    else null
end as GRADE,
d.ID,
d.EMAIL
from DEVELOPERS d
)
select *
from get_grade
where GRADE is not null
order by GRADE asc, ID asc


