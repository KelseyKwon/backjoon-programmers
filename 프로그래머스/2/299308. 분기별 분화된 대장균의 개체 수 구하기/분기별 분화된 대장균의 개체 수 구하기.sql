-- 코드를 작성해주세요
-- 
with quarter_info as(select ID, 
CASE 
WHEN MONTH(DIFFERENTIATION_DATE) >= 1 and MONTH(DIFFERENTIATION_DATE) <= 3 then 1
when MONTH(DIFFERENTIATION_DATE) >= 4 and MONTH(DIFFERENTIATION_DATE) <= 6 then 2
when MONTH(DIFFERENTIATION_DATE) >= 7 and MONTH(DIFFERENTIATION_DATE) <= 9 then 3
when MONTH(DIFFERENTIATION_DATE) >= 10 and MONTH(DIFFERENTIATION_DATE) <= 12 then 4
end as QUARTER
from ECOLI_DATA)

select concat(b.QUARTER, 'Q') as QUARTER, count(distinct a.ID) as ECOLI_COUNT
from ECOLI_DATA as a
join quarter_info as b on a.ID = b.ID
group by b.QUARTER
order by b.QUARTER