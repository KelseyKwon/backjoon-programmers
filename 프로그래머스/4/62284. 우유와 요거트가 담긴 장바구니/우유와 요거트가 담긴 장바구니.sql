-- 코드를 입력하세요
-- Name에 Milk 와 YOgurt가 둘다 있는지 알아보기
-- 둘다 동시에 구입한 장바구니 아이디 조회하는 SQL
-- CART_ID asc
(select CART_ID
from CART_PRODUCTS
where NAME = 'Milk')
intersect
(select CART_ID
from cART_PRODUCTS
where NAME = 'Yogurt')
order by CART_ID asc