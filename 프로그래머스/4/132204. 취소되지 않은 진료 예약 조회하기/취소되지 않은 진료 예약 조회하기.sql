-- 코드를 입력하세요
-- APNT_YMD = '2022-04-13' and APNT_CNCL_YN = 'N'
-- c.APNT_NO, a.PT_NAME, a.PT_NO, c.MCDP_CD, b.DR_NAME, c.APNT_YMD
-- c.APNT_YMD asc
with not_canceled as (
    select *
    from APPOINTMENT
    where DATE(APNT_YMD) = '2022-04-13' and APNT_CNCL_YN = 'N'
)
select c.APNT_NO, a.PT_NAME, a.PT_NO, c.MCDP_CD, b.DR_NAMe, c.APNT_YMD
from not_canceled c
join PATIENT a on c.PT_NO = a.PT_NO
join DOCTOR b on c.MDDR_ID = b.DR_ID
order by c.APNT_YMD