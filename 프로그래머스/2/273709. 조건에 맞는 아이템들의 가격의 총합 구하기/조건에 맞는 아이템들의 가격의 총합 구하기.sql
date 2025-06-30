-- 코드를 작성해주세요

select sum(PRICE) as TOTAL_PRICE
FROM ITEM_INFO
where RARITY = 'LEGEND'
