# Write your MySQL query statement below
# at leat three times consecutively
# find all numbers that appear at leat three times conse
# in any order
select distinct a.num as ConsecutiveNums
from Logs as a
join Logs as b on b.id = a.id+1 and a.num = b.num
join Logs as c on c.id = b.id+1 and b.num = c.num