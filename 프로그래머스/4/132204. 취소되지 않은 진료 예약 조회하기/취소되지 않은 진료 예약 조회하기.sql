-- 코드를 입력하세요
-- = YES BUT NOT APNY_CNCL_YMD가 2022-04-13이 안된, or APNY_CNCL_YN이 NO인거
-- MCDP_CD = CS
-- APNY_NO, PT_NAME, PT_NO, MCDP_NO, DR_NAME, APNY_YMD
-- APNY_TMD asc
# with CS_NOT_CANCELED as (
#     select *
#     from APPOINTMENT
#     where MCDP_CD = 'CS' and (
#         APNT_CNCL_YN = 'N' or
#         (APNT_CNCL_YN = 'Y' and not APNT_CNCL_YMD = '2022-04-13')
#         )
# )
# -- 이거랑 PATIENT을 join하고 
#     -- 이거랑 DOCTOR을 join하고 
#     -- 이거의 APNY_NO, PATIENT의 Pt_NAME, 저거의 PT_NO, 이거의 MCDP_CD 
# select a.APNT_NO, b.PT_NAME, b.PT_NO, a.MCDP_CD, c.DR_NAME, DATE(a.APNT_CNCL_YMD)
# from CS_NOT_CANCELED as a
# join PATIENT as b on a.PT_NO = b.PT_NO
# join DOCTOR as c on a.MDDR_ID = c.DR_ID
# order by APNT_YMD asc

# WITH CS_NOT_CANCELED AS (
#     SELECT *
#     FROM APPOINTMENT
#     WHERE MCDP_CD = 'CS'
#       AND DATE(APNT_YMD) = '2022-04-13'
#       AND (
#         APNT_CNCL_YN = 'N'
#         OR (APNT_CNCL_YN = 'Y' AND APNT_CNCL_YMD <> '2022-04-13')
#       )
# )
# SELECT 
#     a.APNT_NO, 
#     b.PT_NAME, 
#     b.PT_NO, 
#     a.MCDP_CD, 
#     c.DR_NAME, 
#     a.APNT_YMD
# FROM CS_NOT_CANCELED a
# JOIN PATIENT b ON a.PT_NO = b.PT_NO
# JOIN DOCTOR c ON a.MDDR_ID = c.DR_ID
# ORDER BY a.APNT_YMD ASC;

SELECT A.APNT_NO,  C.PT_NAME, A.PT_NO, A.MCDP_CD,B.DR_NAME, A.APNT_YMD 
FROM APPOINTMENT A 
JOIN DOCTOR B ON A.MDDR_ID = B.DR_ID
JOIN PATIENT C ON A.PT_NO = C.PT_NO
WHERE A.MCDP_CD = 'CS' AND A.APNT_CNCL_YN = 'N' AND YEAR(A.APNT_YMD) = 2022 AND MONTH(A.APNT_YMD) = 4 AND DAY(A.APNT_YMD) = 13
ORDER BY A.APNT_YMD