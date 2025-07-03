-- 코드를 입력하세요
-- 7월 TOTAL_ORDER + 상반기 TOTAL_ORDER가 큰 순서대로 맛
-- 상위 3개의 맛 (limit)
SELECT a.FLAVOR
from FIRST_HALF a
join JULY b on a.FLAVOR = b.FLAVOR
group by a.FLAVOR
order by sum(a.TOTAL_ORDER) + sum(b.TOTAL_ORDER) desc
limit 3
