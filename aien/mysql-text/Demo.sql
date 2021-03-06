--lab file for MySQL 2 days for AI class           2017.12.14 v1

--ch2 Tools

SELECT * FROM world.country;

use world;

SELECT * FROM country;

cd C:\Program Files\MySQL\MySQL Server 5.7\bin

mysql -u root -p -D world

SELECT * FROM country;


--也可以將 路徑設在環境變數
-- Window鍵+X 開啟選單 / 選 控制台 /  系統及安全性 / 系統  
   /進階系統設定 / 進階 / 環境變數 / 點 path / 編輯 /
   複製 字串 C:\Program Files\MySQL\MySQL Server 5.7\bin; 
     到 內容前面 加分號分隔 , 勿蓋掉原內容
   
--下次開啟命令視窗時就不須切換路徑
--可直接輸入  mysql -u root -p -D world


--輸出結果排版若很亂 可透過 
--點選左上角 命令提示字元視窗  內容 版面配置 視窗大小 寬度 3000  高度 3000 
--取消 勾選 在調整視窗大小時將文字換行
--確定

--MySQL Command Line Tool 指令查詢
--例 查詢  USE 的用法
     mysql>  help  use ;
--其他如 help  select;
         help  insert;
         help  create table

--安裝 Lab (方法二)  

 ex Northwind DB:   
    copy  northwind 目錄到  C:\ProgramData\MySQL\MySQL Server 5.7\Data

   **手動 copy db dir 之 db 無法 drop schema /database ,  仍需手動刪檔

--ch3 create  database

CREATE  SCHEMA  db01;

CREATE  DATABASE db02;


CREATE DATABASE db03  
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


/*
建議以 utf8mb4 取代 utf8
Note that utf8_general_ci is no longer recommended best practice. See the related Q & A:
   https://dba.stackexchange.com/questions/76788/create-a-database-with-charset-utf-8

CREATE  DATABASE db03 
 CHARACTER  SET  utf8 COLLATE  utf8_general_ci ;
*/

--刪除資料庫

drop database  db02;

--ch4 create table

CREATE  TABLE   student                                  
(  id    INT       PRIMARY    KEY,  
   name  CHAR(20) ,
   bdate DATE ,
   tel   CHAR(20)
)  ;

CREATE   TABLE   course                                  
(  id     INT ,
   name   CHAR(20) ,
   score  INT ,
   INDEX  ( id ) ,
   FOREIGN KEY ( id ) REFERENCES  student ( id )
)  ;


CREATE  TABLE   student2                                  
(  id    INT       PRIMARY    KEY,  
   name  CHAR(20) ,
   bdate DATE ,
   tel   CHAR(20)
)  ;

CREATE   TABLE   course2                                  
(  id     INT ,
   name   CHAR(20) ,
   score  INT ,
   INDEX  ( id ) ,
   FOREIGN KEY ( id ) REFERENCES  student2 ( id )
)  ;

--drop table

drop  table course2;
drop  table student2;
 
--ch5 DML
--INSERT
INSERT INTO student VALUES ( 101 ,'李大同','1983-04-28' , '0920555678') ;
INSERT INTO student( id, name )  VALUES( 102, '程幼青' );

--註 ch6 SELECT  *  FROM  student;

--INSERT 2
insert  into  course  values (101, 'Python', 86);
insert  into  course  values (101, 'SQL'   , 88);
insert  into  course  values (101, 'AI'    , 90);
insert  into  course  values (102, 'Python', 90);
insert  into  course  values (102, 'SQL'   , 92);
insert  into  course  values (102, 'AI'    , 94);
insert  into  course  values (199, 'Python', 94);


--Error Code: 1452. Cannot add or update a child row: a foreign key constraint fails (`db01`.`course`, CONSTRAINT `course_ibfk_1` FOREIGN KEY (`id`) REFERENCES `student` (`id`))



--UPDATE
UPDATE  student 
SET tel = '0928555777'
WHERE id = 101 ;

--DELETE1

DELETE FROM course WHERE id = 102;


--DELETE2 失敗
delete from course;

delete from  student;

Error Code: 1175. You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column To disable safe mode, toggle the option...

--原因
MySQL有個叫 SQL_SAFE_UPDATES 的變數，為了資料庫更新操作的安全性，此值預設為ON
在沒有 WHERE 條件的 UPDATE 或 DELETE 動作會拒絕執行，
而且即使是有 WHERE 條件，但沒有 KEY column 的 WHERE 條件也會拒絕執行。

--要關閉 Safe Update Mode 可執行

SET SQL_SAFE_UPDATES=0 ;

--再次 DELETE 全部資料不加 WHERE 可成功
delete from course;

delete from  student;


--查詢目前是那一模式 

mysql> show variables like '%safe_updates%';
+------------------+-------+
| Variable_name    | Value |
+------------------+-------+
| sql_safe_updates | ON    |
+------------------+-------+
 
--要再開啟 Safe Update Mode，就執行 SET SQL_SAFE_UPDATES=1  ;

--新增、修改、刪除 – 常見錯誤

DELETE FROM student WHERE id = 101;


--
Error Code: 1451. Cannot delete or update a parent row: a foreign key constraint fails (`db01`.`course`, CONSTRAINT `course_ibfk_1` FOREIGN KEY (`id`) REFERENCES `student` (`id`))


UPDATE course SET  id = 199
WHERE  id =  101

--
Error Code: 1452. Cannot add or update a child row: a foreign key constraint fails (`db01`.`course`, CONSTRAINT `course_ibfk_1` FOREIGN KEY (`id`) REFERENCES `student` (`id`))


--ch6 Query

SELECT  *       
FROM    employees;

SELECT  employeeid, lastname, firstname, title
FROM    employees

--查表格有那些欄位

SHOW COLUMNS FROM employees;

--ch6-1 Alias 別名

SELECT  firstname AS First, lastname AS Last, employeeid  AS 'Employee ID:' 

FROM    employees
;

--ch6-1 Alias 可不加 AS

SELECT  firstname First, lastname Last, employeeid  "Employee ID:" 

FROM    employees
;


--Literal string 固定字串

SELECT  lastname , ' is a ',  Title

FROM    employees ;


SELECT  firstname as First, lastname as Last, 'ID number is :', employeeid

FROM    employees ;


--註  MySQL 未支援 + 或 || 串聯符號

除非設成  SET @@sql_mode=PIPES_AS_CONCAT;

  -- Save sql_mode settings
  SET @old_sql_mode=@@sql_mode;
 
  -- Enable || for string concatenation
  SET @@sql_mode=PIPES_AS_CONCAT;
 
  SELECT 'The city' || ' is ' || 'Paris';
  # The city is Paris
 
  -- If any expression is NULL, the entire result is NULL
  SELECT 'The city' || ' is ' || NULL;
  # NULL
 
  SET @@sql_mode=@old_sql_mode;

--Distinct 消除重復列

SELECT  country
FROM    suppliers;

--vs

SELECT  DISTINCT country
FROM    suppliers;


--補充 Distinct + sort by country

SELECT   DISTINCT country
FROM     suppliers
ORDER BY country;


--ch6-2 filter: WHERE

SELECT employeeid, lastname, firstname, title
FROM   employees
WHERE  employeeid = 5;

SELECT lastname, city
FROM   employees
WHERE  country = 'USA';

SELECT employeeid, lastname, hiredate

FROM   employees

WHERE  hiredate = '1992-05-01';

--BETWEEN  AND

SELECT productname, unitprice
FROM   products
WHERE  unitprice >= 10 AND 
       unitprice <= 20 ;

--vs

SELECT productname, unitprice
FROM   products
WHERE  unitprice BETWEEN 10 AND 20 ;

--IN

SELECT companyname, country
FROM   suppliers
WHERE  country IN ('Japan', 'Italy') ;

--vs

SELECT companyname, country
FROM   suppliers
WHERE  country  = 'Japan' OR
       country  = 'Italy' ;

--LIKE

SELECT employeeid, firstname

FROM   employees

WHERE  firstname LIKE 'A%';

--NULL

SELECT companyname, fax
FROM   suppliers
WHERE  fax IS NULL ;

--勿用  = NULL

--ch6-2 sort 排序

SELECT    productid, productname, categoryid, unitprice
FROM      products
ORDER BY  unitprice ;

SELECT    productid, productname, categoryid, unitprice
FROM      products
ORDER BY  unitprice DESC;


SELECT   productid, productname, categoryid, unitprice
FROM     products
ORDER BY categoryid, unitprice DESC;

--TOP N,  first N rows

SELECT productid, ProductName , UnitPrice

FROM  products  

ORDER BY unitprice DESC

LIMIT 5 ;

-傳回從 10 筆之後的 5 筆資料

SELECT productid, ProductName , UnitPrice

FROM  products  

ORDER BY unitprice DESC

LIMIT 5 OFFSET 10 ;

or

SELECT productid, ProductName , UnitPrice

FROM  products  

ORDER BY unitprice DESC

LIMIT 10,5 ;


--ch6-3 Single row FUNCTION 單列函數
--String function 字串函數

SELECT  lastname, LOWER(lastname), city, SUBSTRING(city,1,3)

FROM    Employees;

--Numeric function  數字函數
SELECT  ROUND ( 45.926, 2 ),  ROUND ( 45.926, 0 ),  ROUND ( 45.926, -1 )
;

--output
ROUND ( 45.926, 2 ),  ROUND ( 45.926, 0 ),  ROUND ( 45.926, -1 )

45.93	              46	            50


SELECT productid, unitprice, ROUND(unitprice, 1), ROUND(unitprice, -1)

FROM   Products

WHERE  productid in (5, 26, 50, 75)

--output
productid, unitprice, ROUND(unitprice, 1), ROUND(unitprice, -1)

5	   21.3500    21.4	           20
26	   31.2300    31.2	           30
50	   16.2500    16.3	           20
75	    7.7500    7.8	           10

--日期函數 - 現在時間

SELECT CURDATE(), CURTIME(), NOW()

2017-12-15  11:25:43  2017-12-15 11:25:43

--日期函數


SELECT DATE_ADD('2006-03-30', interval 6 month) ;


SELECT DATEDIFF('2009-03-30','2009-01-30'); 


SELECT EXTRACT(YEAR FROM '2009-07-02'); 

SELECT EXTRACT(DAY FROM '2009-07-02'); 


SELECT YEAR('2009-03-30'); 

SELECT MONTH('2009-03-30'); 

SELECT DAY('2009-03-30'); 


--DATE_ADD  現在時間加 n 個單位
SELECT DATE_ADD(CURDATE(), INTERVAL 1 DAY);

SELECT DATE_ADD(CURDATE(), INTERVAL 6 MONTH);

--CAST 語法
cast(expression AS type)
convert(expression, type)
--Valid types are BINARY, CHAR, DATE, DATETIME, SIGNED (INTEGER), and UNSIGNED (INTEGER).

--假如今日為 2017-12-15

SELECT CAST( CURDATE() AS CHAR(20));
   

2017-12-15

SELECT CONVERT( CURDATE(), CHAR(20));

2017-12-15

SELECT CONVERT('test', CHAR(10));
SELECT CAST('test' AS CHAR(10));

--String to Number

SELECT CAST( '3' AS  SIGNED );

SELECT CAST( '3' AS  SIGNED  INTEGER);

--with character set

SELECT CONVERT('test', CHAR CHARACTER SET utf8);
SELECT CAST('test' AS CHAR CHARACTER SET utf8);

--IFNULL 函數

SELECT companyname,  fax,  IFNULL(fax, 'No Fax')
FROM   suppliers


--CASE  語法1
CASE value
WHEN [compare-value] THEN result
[WHEN [compare-value] THEN result ...]
[ELSE result]
END

--or

CASE  語法2
WHEN [condition] THEN result
[WHEN [condition] THEN result ...]
[ELSE result]
END

--CASE函數 
--依 產品分類代碼(CategoryID)  調整 
產品單價(unitprice)


SELECT   productname, categoryid, unitprice,
         
         CASE  categoryid  WHEN 1 THEN  1.10 * unitprice

                           WHEN 2 THEN  1.20 * unitprice
  
                           WHEN 3 THEN  1.30 * unitprice
  
                           ELSE unitprice 

         END     "REVISED_Price"

FROM     products;

--or

SELECT   productname, categoryid, unitprice,

         CASE WHEN categoryid = 1 THEN  1.10 * unitprice

              WHEN categoryid = 2 THEN  1.20 * unitprice

              WHEN categoryid = 3 THEN  1.30 * unitprice

              ELSE unitprice
 
       END     "REVISED_Price"

FROM     products;

--ch7 Group function  ˊ群組函數
--ch7-1  one group

SELECT MAX(unitprice)

FROM   products;


--儘量不要分組時 顯示其他欄位 因只會回傳符合的第一筆

SELECT productid, productname, MIN(unitprice)

FROM   products

WHERE  productid  IN (1,35,39,76);
--WHERE  unitprice = 18;



output
productid, productname, MIN(unitprice)

1	   Chai	        18.0000

--單價 18 的有 4筆

SELECT productid, productname, unitprice

FROM   products

WHERE  productid  IN (1,35,39,76);
--WHERE  unitprice = 18;


output
productid, productname,      MIN(unitprice)

1	   Chai      	     18.0000
35	   Steeleye Stout    18.0000
39	   Chartreuse verte  18.0000
76	   Lakkalikoori	     18.0000

SELECT  COUNT(*),  COUNT( ReportsTo )

FROM    employees;

--origional data

SELECT   Categoryid, productid,  unitprice 
FROM     products

ORDER BY Categoryid;

--ch7-2 GROUP BY 分組

SELECT   Categoryid,  AVG(unitprice)

FROM     products

GROUP BY Categoryid;

--ERROR using WHERE  
--Error Code: 1111. Invalid use of group function

SELECT  CategoryID,  AVG ( unitprice )
 
FROM    Products

WHERE   AVG ( unitprice ) >  30  
GROUP   BY  CategoryID
 ;


--ch7-2 HAVING

SELECT  CategoryID,  AVG ( unitprice )
 
FROM    Products
 
GROUP  BY  CategoryID
 
HAVING  AVG ( unitprice ) >  30 ;


--ch7 advanced: WHERE AND HAVING 併用

SELECT  CategoryID,  AVG ( unitprice )
 
FROM    Products
 
WHERE   CategoryID  >= 5
GROUP  BY  CategoryID
 
HAVING  AVG ( unitprice ) >  30 ;


--CH8 JOIN 合併查詢
--origional data
SELECT customerid, companyname FROM customers where customerid = 'ALFKI';
SELECT customerid, orderid, orderdate FROM orders where customerid= 'ALFKI';

--ch8-1 CROSS JOIN

SELECT companyname, orderid, orderdate 

FROM   customers CROSS JOIN orders  ;


-- Customer 91 筆 乘 Orders 830 筆 91*830 共 75530 種組合


SELECT COUNT(*)
FROM customers; 

 
SELECT COUNT(*)
FROM orders;        
SELECT COUNT(*) FROM customers CROSS JOIN orders  ;
 

--ch8-2 Inner JOIN
--合併查詢 customers --> orders ---> order_details
--關聯             customerid   orderid
--查出 customer 'ALFKI' 所下 orders

SELECT Customers.customerid, CompanyName, Orders.customerid, orderid, orderdate
FROM   Customers JOIN Orders 
ON     Customers.customerid = Orders.customerid;

--JOIN with Table Name  Alias 

SELECT c.customerid, c.companyname, o.customerid, o.orderid, o.orderdate
FROM   customers c JOIN orders  o
ON     c.customerid = o.customerid  ;

--JOIN with extra condiction WHERE

SELECT c.customerid, c.companyname, o.customerid, o.orderid, o.orderdate
FROM   customers c JOIN orders  o
ON     c.customerid = o.customerid
WHERE  c.customerid= 'ALFKI' ;

--ch8-2 Inner JOIN　extra 額外練補充練習
--查出 orders 10643 之  orders_details

SELECT o.customerid, o.orderid, o.orderdate, od.orderid, od.productid, od.quantity
FROM   orders  o JOIN order_details od
ON     o.orderid = od.orderid
WHERE  o.orderid = 10643

--Join 3個 Table: customer 'ALFKI' 所下 ordder 10643 之orders details

SELECT c.customerid, c.companyname, o.customerid, o.orderid, o.orderdate,
       od.orderid, od.productid, od.quantity
FROM   customers c JOIN orders  o
ON     c.customerid = o.customerid
JOIN   order_details od
ON     o.orderid = od.orderid
WHERE  c.customerid= 'ALFKI'AND
       o.orderid = 10643

--ch8-3 OUTER JOIN　832　 　

SELECT c.customerid, c.companyname, o.customerid, o.orderid, o.orderdate
FROM   customers c LEFT OUTER JOIN orders o
ON     c.customerid = o.customerid  ;


--ch8-4 Self JOIN
--原始資料 

select employeeid,lastname, reportsto from employees ;

--Self JOIN 查員工姓名及其主管之姓名
SELECT w.employeeid,w.lastname, w.reportsto, m.employeeid AS mgrid, m.lastname AS mgrname
FROM   employees w  JOIN employees m
ON     w.reportsto = m.employeeid

or

SELECT worker.employeeid, worker.lastname, worker.reportsto, 
       manager.employeeid AS mgrid, manager.lastname AS mgrname
FROM   employees worker  JOIN employees manager
ON     worker.reportsto = manager.employeeid ;

--ch9 Subquery

--找出 大於平均價之 prod

SELECT productid, productname, unitprice FROM products;
SELECT AVG(unitprice) FROM products;

--in ch5 where already know  avg is 28.86

SELECT productid, productname, unitprice 
FROM   products
WHERE  unitprice > 28.86

--Error Code: 1111. Invalid use of group function

SELECT productid, productname, unitprice 
FROM   products
WHERE  unitprice >  AVG(unitprice) 

--answer
SELECT productid, productname, unitprice
FROM   products
WHERE  unitprice > ( SELECT AVG(unitprice) 
                     FROM   products
                   );

--ch9-2　找出 單價大於第 2 類中任一產品單價之 prod

SELECT productid, productname, unitprice

FROM   products

WHERE  unitprice > ANY ( SELECT unitprice
  
                      FROM   products
   
                         WHERE CategoryID = 2) ;

--找出 單價大於第 2 類中所有產品單價之 prod

SELECT productid, productname, unitprice

FROM   products

WHERE  unitprice > ALL ( SELECT unitprice
  
                      FROM   products
   
                         WHERE CategoryID = 2) ;
 
