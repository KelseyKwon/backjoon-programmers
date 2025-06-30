-- 코드를 작성해주세요
-- YEAR, YEAR_DEV, ID
-- 가장 큰 대장균 크기 - 각 대장균 크기
-- 연도에 대해 오름차순 / 대장균 크기 편차 오름차순
WITH MAX_SIZE_TABLE as (SELECT YEAR(DIFFERENTIATION_DATE) as YEAR, max(SIZE_OF_COLONY) as MAX_SIZE
                        FROM ECOLI_DATA
                        GROUP BY YEAR(DIFFERENTIATION_DATE)
)
select b.YEAR, (MAX_SIZE - SIZE_OF_COLONY) as YEAR_DEV, a.ID
from ECOLI_DATA as a join MAX_SIZE_TABLE as b on YEAR(a.DIFFERENTIATION_DATE) = b.YEAR
order by b.YEAR asc, YEAR_DEV asc
