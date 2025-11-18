# Write your MySQL query statement below
# in one year -> multiple sales
# forst year / product has been sold / find all sales
# product_id, first_year, quantity. price

# group by product_id -> min(year) -> select product

select product_id, year as first_year, quantity, price
from Sales as a
where (product_id, year) in (select product_id, min(year)
from Sales 
group by product_id)