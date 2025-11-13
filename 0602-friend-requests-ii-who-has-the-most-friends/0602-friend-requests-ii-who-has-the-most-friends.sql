# Write your MySQL query statement below
# most friends number -> only one person should be in result.
# generate two table -> # of requester_id, # of accepter_id
-- with req_nums as (
-- select requester_id, sum(requester_id) as req_num
-- from RequestAccepted as a
-- group by requester_id), 
-- acp_nums as (
--     select accepter_id, sum(accepter_id) as acp_num
--     from RequestAccepted as b
--     group by accepter_id
-- )
-- select a.requester_id as id, sum(a.req_num + b.acp_num) as num
-- from req_nums as a 
-- join acp_nums as b on a.requester_id = b.accepter_id
-- order by num limit 1

select id, count(*) as num
from (
    select requester_id as id from RequestAccepted
    union all
    select accepter_id as id from RequestAccepted
) as all_friends
group by id
order by num desc
limit 1
