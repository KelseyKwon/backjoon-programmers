-- 코드를 입력하세요
-- Milk & Yogurt가 모두 있는 장바구니 알아보기
-- 
(SELECT CART_ID
from CART_PRODUCTS
where NAME = 'Yogurt')
intersect
(
select CART_ID
    from CART_PRODUCTS
    where NAME = 'Milk'
)