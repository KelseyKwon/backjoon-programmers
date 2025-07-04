-- 코드를 작성해주세요
-- 각 세대별 자식이 없는 개체 수
-- 세대를 출력하는 SQL문
-- 각 세대에 대해 오름차순
WITH RECURSIVE GENERATION AS(
    SELECT ID, 1 AS g_level
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL # 최상위 노드

    UNION ALL

    SELECT e.ID, g.g_level+1 AS g_level
    FROM ECOLI_DATA e
    INNER JOIN GENERATION g
    ON e.PARENT_ID = g.ID
)

SELECT COUNT(*) AS `COUNT`, g_level as GENERATION
FROM GENERATION g
LEFT JOIN ECOLI_DATA e
ON g.ID = e.PARENT_ID
WHERE e.ID IS NULL -- 자식이 없는 개체(join 안 된 행)
GROUP BY GENERATION
ORDER BY GENERATION