-- 코드를 입력하세요
SELECT II.INGREDIENT_TYPE,SUM(FH.TOTAL_ORDER) FROM FIRST_HALF FH,ICECREAM_INFO II
WHERE II.FLAVOR = FH.FLAVOR
GROUP BY II.INGREDIENT_TYPE
ORDER BY SUM(FH.TOTAL_ORDER);