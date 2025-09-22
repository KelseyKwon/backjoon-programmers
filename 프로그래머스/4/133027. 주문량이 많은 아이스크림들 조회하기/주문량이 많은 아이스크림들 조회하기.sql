-- 코드를 입력하세요
-- 상반기 / 7월
-- foreign key (FIRST_HALF) SHIPMENT_ID가 JULY로부터 나옴
-- 7월에는 같은 맛의 아이스크림이더라도 SHIPMENT_ID가 다른 경우가 있다.
-- a.TOTAL_ORDER + b.TOTAL_ORDER가 큰 순서대로 limit 3을 작성하기
with july_total_order as (
    select FLAVOR, sum(TOTAL_ORDER) as SUM_JULY
    from JULY
group by FLAVOR
)
select a.FLAVOR
from FIRST_HALF as a
join july_total_order as b on a.FLAVOR = b.FLAVOR
order by (a.TOTAL_ORDER + b.SUM_JULY) desc limit 3
