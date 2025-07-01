-- 코드를 입력하세요
-- 우유 & 요거트를 동시에 구입한 장바구니의 아이디
WITH milk_group AS (
  SELECT CART_ID
  FROM CART_PRODUCTS
  WHERE NAME = 'Milk'
),
yogurt_group AS (
  SELECT CART_ID
  FROM CART_PRODUCTS
  WHERE NAME = 'Yogurt'
)
SELECT CART_ID
FROM milk_group
INTERSECT
SELECT CART_ID
FROM yogurt_group;
