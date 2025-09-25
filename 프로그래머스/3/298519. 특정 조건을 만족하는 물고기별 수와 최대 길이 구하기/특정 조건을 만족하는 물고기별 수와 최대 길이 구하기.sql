-- 코드를 작성해주세요
-- 10cm 이하이면 LENGTH = NULL
-- 평균 LENGTH >= 33 -> 
-- count (잡은수), max(length) , FISH_TYPE
-- 10cm 이하이면 (NULL) -> 10cm로 취급하기.

WITH turn_to_num AS (
    SELECT ID, FISH_TYPE, IFNULL(LENGTH, 10) AS LENGTH, TIME
    FROM FISH_INFO
)
SELECT 
    COUNT(a.ID) AS FISH_COUNT,
    MAX(a.LENGTH) AS MAX_LENGTH,
    a.FISH_TYPE
FROM turn_to_num AS a
GROUP BY a.FISH_TYPE
HAVING AVG(a.LENGTH) >= 33
ORDER BY a.FISH_TYPE;