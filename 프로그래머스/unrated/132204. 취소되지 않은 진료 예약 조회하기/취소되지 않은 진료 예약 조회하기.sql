-- 코드를 입력하세요
SELECT A.APNT_NO,P.PT_NAME,P.PT_NO,D.MCDP_CD,D.DR_NAME,A.APNT_YMD
FROM PATIENT P,DOCTOR D,APPOINTMENT A
WHERE P.PT_NO = A.PT_NO AND D.DR_ID = A.MDDR_ID AND
    A.APNT_YMD LIKE '%2022-04-13%'AND A.APNT_CNCL_YN NOT LIKE 'Y%' AND
    A.MCDP_CD LIKE 'CS%'
ORDER BY A.APNT_YMD ASC;