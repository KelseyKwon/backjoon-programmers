# Write your MySQL query statement below
# select the id with temperature is higher than yesterday 
select b.id
from Weather as a
join Weather as b on TIMESTAMPDIFF(day, a.recordDate, b.recordDate) = 1
where b.temperature > a.temperature