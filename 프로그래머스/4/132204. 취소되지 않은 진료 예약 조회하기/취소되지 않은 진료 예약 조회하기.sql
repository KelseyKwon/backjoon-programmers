-- 코드를 입력하세요
-- APNT_YMD = 2022-04-13 APNT_CNCL_YN = 'N' 
-- c.APNT_NO, a.PT_NAME, a.PT_NO, b.MCDP_CD, b.DR_NAME, c.APNT_YMD
-- APNT_YMD asc
SELECT a.APNT_NO, b.PT_NAME, b.PT_NO, c.MCDP_CD, c.DR_NAME, a.APNT_YMD
from APPOINTMENT as a
join PATIENT as b on a.PT_NO = b.PT_NO and a.APNT_CNCL_YN = 'N'
join DOCTOR as c on a.MDDR_ID = c.DR_ID
where DATE_FORMAT(a.APNT_YMD, '%Y-%m-%d') = '2022-04-13'
order by a.APNT_YMD