-- 코드를 입력하세요
-- JULY 테이블과 상반기 총 주문량을 더한 값이 큰 순서대로 상위 3개만 (limit) 조회
-- FIRST_HALF : FLAVOR, JULY : SHIPMENT_ID
-- 7월 아이스크림 총 주문량 + 상반기 아이스크림 총 주문량이 큰 순으로
SELECT a.FLAVOR
from JULY as a join FIRST_HALF as b on a.FLAVOR = b.FLAVOR
group by a.FLAVOR
order by SUM(a.TOTAL_ORDER + b.TOTAL_ORDER) desc
limit 3