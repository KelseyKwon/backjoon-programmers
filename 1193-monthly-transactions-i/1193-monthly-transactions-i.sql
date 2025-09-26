# Write your MySQL query statement below
# (each month, country) -> # of transactions & total amount, # of approved transactions % total_amount

select DATE_FORMAT(trans_date, "%Y-%m") as MONTH, country, 
count(distinct id) as trans_count,
sum(
    case 
        when state = 'approved' then 1 
        else 0
    end
    ) as approved_count,
sum(amount) as trans_total_amount,
sum(CASE WHEN STATE = 'approved' then amount else 0 end) as approved_total_amount
from Transactions
group by DATE_FORMAT(trans_date, "%Y-%m"), country
order by month, country
