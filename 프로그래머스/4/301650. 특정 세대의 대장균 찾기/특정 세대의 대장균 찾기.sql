-- 코드를 작성해주세요
SELECT C.ID
from ECOLI_DATA as A 
join ECOLI_DATA as B on B.PARENT_ID = A.ID
join ECOLI_DATA as C on C.PARENT_ID = B.ID
where A.PARENT_ID is null
order by C.ID;