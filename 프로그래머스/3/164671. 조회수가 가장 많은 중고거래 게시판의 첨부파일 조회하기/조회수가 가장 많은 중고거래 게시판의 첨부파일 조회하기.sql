-- 코드를 입력하세요
-- VIEWS가 가장 높은 BOARD에 대한 FILE을 조회하는 것.
-- concat이야.
-- /home/grep/src/, BOARD_ID , /, FILE_ID, FILE_NAME, FILE_EXT
SELECT concat("/home/grep/src/", b.BOARD_ID, "/", b.FILE_ID, b.FILE_NAME, b.FILE_EXT) as FILE_PATH
from USED_GOODS_BOARD as a
join USED_GOODS_FILE as b on a.BOARD_ID = b.BOARD_ID
where a.VIEWS = (select max(VIEWS) from USED_GOODS_BOARD)
order by b.FILE_ID desc