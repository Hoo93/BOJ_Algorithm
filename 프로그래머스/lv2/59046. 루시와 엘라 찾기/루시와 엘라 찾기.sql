SELECT ANIMAL_ID,NAME,SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME REGEXP '^(LUCY|ELLA|PICKLE|ROGAN|SABRINA|MITTY)$'
ORDER BY ANIMAL_ID ASC;