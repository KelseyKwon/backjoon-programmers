-- APNT_YMD = 2022-04-13 and APNT_CNCL_YN = No
-- MCDP_CD = 'CS'
-- c.APNT_NO, a.PT_NAME a.PT_NO b.MCDP_CD  b.DR_NAME a.APNT_YMD

with no_canceled as (
    select *
    from APPOINTMENT
    where DATE(APNT_YMD) = '2022-04-13' and APNT_CNCL_YN = 'N' and MCDP_CD = 'CS'
)
select c.APNT_NO, a.PT_NAME, a.PT_NO, b.MCDP_CD, b.DR_NAME, c.APNT_YMD
from no_canceled c
join PATIENT a on c.PT_NO = a.PT_NO
join DOCTOR b on c.MDDR_ID = b.DR_ID
order by c.APNT_YMD
