-- 코드를 입력하세요
SELECT P.PRODUCT_CODE,SUM(P.PRICE*OS.SALES_AMOUNT) AS SALES
FROM PRODUCT P
RIGHT JOIN OFFLINE_SALE OS ON P.PRODUCT_ID = OS.PRODUCT_ID
GROUP BY P.PRODUCT_ID
ORDER BY SALES DESC,P.PRODUCT_CODE ASC;
