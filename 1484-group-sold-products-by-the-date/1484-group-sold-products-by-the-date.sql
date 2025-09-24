# Write your MySQL query statement below
# 각 날짜에 팔린 다른 물품들을 찾고 이름을 내놔라.
# 사전순으로 정렬
# order by sell_date
# group by sell_date, group_concat(product order by product separator ',')
# num_sold는 count(*)
select sell_date, count(distinct product) as num_sold, 
group_concat(distinct product order by product separator ',') as products
from Activities
group by sell_date
