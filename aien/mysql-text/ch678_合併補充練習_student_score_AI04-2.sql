
/*
-- student 學員資料表 
-- course  學員各科成績

--** 單純 23 學員中 每人考三科, 有一學員 3科都沒考 , 沒登記分數 非登記成 零分
--** 難一點則 10號學員只考兩科   這時 平均分數 就會有爭議

--ch6
--查出分數(score) 大於90分以上的學員(不管那一科)
--查出課程名稱(name) 為 JAVA 且分數(score) 介於85分及90分之間的學員 
--列出學員各科分數,從高到低排序(不管那一科)
--列出學員各科分數,先依課程名稱(name)排序, 相同名稱再依分數從高到低排列 

--ch7
--查出 平均 的分數是幾分 (不管那一科)
--依各科(name)分組, 列出各科(name)最高 的分數是幾分
--依學號(id)分組, 列出各人總分
--依學號(id)分組, 列出各人總分 大於 250 以上者  (列出學號,總分)

--ch8
--列出學員姓名及各科成績
--列出學員姓名及各科成績 (未參加考試的學員也要列出)

--ch9
--查出學員任一科分數大於總平均的有那些 (含學號,個人分數)
--依學號(id)分組, 計算學員總分最高者 (含學號,總分)
*/

DROP   DATABASE IF EXISTS DB01; 
CREATE DATABASE DB01;

use DB01;

SET SQL_SAFE_UPDATES=0 ;

drop table IF EXISTS course ;
drop table IF EXISTS student ;
 

create table student
( id    int        PRIMARY KEY,    
  name  nchar(20),                 
  bdate date,
  tel   char(20)
);

create table course
( id    int     ,    
  name  nchar(20),   
  score int,         
  FOREIGN KEY(id) REFERENCES student(id) 
);
 
insert into student values ( 1, '陳昱瑾','1983-04-21','09205556781');
insert into student values ( 2, '林玴安','1983-09-23','09205556789');
insert into student values ( 3, '陳奕維','1983-08-25','09205556785');
insert into student values ( 4, '朱訓威','1983-07-27','09205556723');
insert into student values ( 5, '呂仲唐','1983-05-29','09205556889');
insert into student values ( 6, '林孟廷','1983-06-22','09205556729');
insert into student values ( 7, '廖子淇','1983-03-24','09205556726');
insert into student values ( 8, '謝雅蓁','1983-01-26','09205556729');
insert into student values ( 9, '陳岳澤','1983-02-28','09205556789');
insert into student values (10, '柯建羽','1983-11-20','09205556782');
insert into student values (11, '翁于荏','1983-10-21','09205556729');
insert into student values (12, '蕭煒迪','1983-04-23','09205556389');
insert into student values (13, '黃亮之','1983-05-25','09205556728');
insert into student values (14, '洪敏軒','1983-07-23','09205556029');
insert into student values (15, '邵柏鈞','1983-02-27','09205556783');
insert into student values (16, '周竑宇','1983-04-23','09205556789');
insert into student values (17, '呂傑霖','1983-06-29','09205556781');
insert into student values (18, '高誌宏','1983-04-22','09205556780');
insert into student values (19, '周惠育','1983-08-24','09205556789');
insert into student values (20, '黃逸旻','1983-04-26','09205556787');
insert into student values (21, '盧廷將','1983-09-28','09205556089');
insert into student values (22, '詹鎧伊','1983-04-20','09205556189');
insert into student values (23, '郭書宇','1983-05-25','09205556188');
 

insert into course values ( 1,'JAVA',85);
insert into course values ( 2,'JAVA',86);
insert into course values ( 3,'JAVA',80);
insert into course values ( 4,'JAVA',85);
insert into course values ( 5,'JAVA',75);
insert into course values ( 6,'JAVA',70);
insert into course values ( 7,'JAVA',92);
insert into course values ( 8,'JAVA',85);
insert into course values ( 9,'JAVA',83);
insert into course values (11,'JAVA',87);
insert into course values (12,'JAVA',85);
insert into course values (13,'JAVA',86);
insert into course values (14,'JAVA',85);
insert into course values (15,'JAVA',84);
insert into course values (16,'JAVA',75);
insert into course values (17,'JAVA',81);
insert into course values (18,'JAVA',85);
insert into course values (19,'JAVA',79);
insert into course values (20,'JAVA',85);
insert into course values (21,'JAVA',78);
insert into course values (22,'JAVA',85);

 
insert into course values ( 1,'電概',81);
insert into course values ( 2,'電概',80);
insert into course values ( 3,'電概',82);
insert into course values ( 4,'電概',84);
insert into course values ( 5,'電概',64);
insert into course values ( 6,'電概',83);
insert into course values ( 7,'電概',85);
insert into course values ( 8,'電概',87);
insert into course values ( 9,'電概',86);
insert into course values (10,'電概',85);
insert into course values (11,'電概',82);
insert into course values (12,'電概',81);
insert into course values (13,'電概',89);
insert into course values (14,'電概',85);
insert into course values (15,'電概',88);
insert into course values (16,'電概',87);
insert into course values (17,'電概',86);
insert into course values (18,'電概',85);
insert into course values (19,'電概',84);
insert into course values (20,'電概',82);
insert into course values (21,'電概',85);
insert into course values (22,'電概',81);
 

insert into course values ( 1,'T-SQL',85);
insert into course values ( 2,'T-SQL',85);
insert into course values ( 3,'T-SQL',80);
insert into course values ( 4,'T-SQL',85);
insert into course values ( 5,'T-SQL',85);
insert into course values ( 6,'T-SQL',83);
insert into course values ( 7,'T-SQL',85);
insert into course values ( 8,'T-SQL',82);
insert into course values ( 9,'T-SQL',91);
insert into course values (10,'T-SQL',85);
insert into course values (11,'T-SQL',85);
insert into course values (12,'T-SQL',87);
insert into course values (13,'T-SQL',85);
insert into course values (14,'T-SQL',85);
insert into course values (15,'T-SQL',86);
insert into course values (16,'T-SQL',85);
insert into course values (17,'T-SQL',85);
insert into course values (18,'T-SQL',89);
insert into course values (19,'T-SQL',85);
insert into course values (20,'T-SQL',88);
insert into course values (21,'T-SQL',85);
insert into course values (22,'T-SQL',84);
 
/* Unicode  若宣告為 NCHAR 可省略 N'字串' 但最好不要
insert into student values (24, N'黃瀞賢','1993-07-23','09206256029');
insert into student values (25, N'曾珦煊','1983-06-22','09205556789');
insert into student values (26, N'黃頎晧','1983-04-23','09207556789');

或
create table student
( id    int        PRIMARY KEY,    
  name  char(20)  CHARACTER SET utf8 COLLATE utf8_unicode_ci,                 
  bdate date,
  tel   char(20)
);

*/

select * from student;
select * from course;
