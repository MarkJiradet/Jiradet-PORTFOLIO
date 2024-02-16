.open restaurant.db

CREATE TABLE IF NOT EXISTS countrys(
  countryid   INT,
  countryname TEXT UNIQUE,
  PRIMARY KEY(countryid)
);

CREATE TABLE IF NOT EXISTS customers(
  customerid    INT,
  customername  TEXT NOT NULL,
  age           INT,
  telephone     INT,
  email         TEXT UNIQUE,
  countryid     INT,
  PRIMARY KEY(customerid),
  FOREIGN KEY(countryid) REFERENCES countrys(countryid)
);

CREATE TABLE IF NOT EXISTS chefs(
  chefid       INT,
  chefname     TEXT,
  salary       REAL,
  countryid    INT,
  PRIMARY KEY(chefid),
  FOREIGN KEY(countryid) REFERENCES countrys(countryid)
);

CREATE TABLE IF NOT EXISTS menus(
  menuid      INT,
  menuname    TEXT UNIQUE,
  price       REAL,
  PRIMARY KEY(menuid)
);

CREATE TABLE IF NOT EXISTS orders(
  orderid     INT,
  customerid  INT,
  menuid      INT,
  chefid      INT,
  PRIMARY KEY(orderid),
  FOREIGN KEY(customerid) REFERENCES customers(customerid),
  FOREIGN KEY(menuid) REFERENCES menus(menuid),
  FOREIGN KEY(chefid) REFERENCES chefs(chefid)
);

INSERT INTO countrys VALUES
  (1,'America'),
  (2,'China'),
  (3,'Japan'),
  (4,'England'),
  (5,'Korea'),
  (6,'Thailand');

INSERT INTO customers VALUES
  (1,'Jiradet Nakham',20,0942904542,'jiradet@gmail.com',6),
  (2,'Suporn Panmuang',19,0612218243,'suporn@gmail.com',6),
  (3,'Takashi Eigika',35,0621457821,'takashi@hotmail.com',5),
  (4,'Eimi Fukada',25,0952345876,'eimi.f@gmail.com',3),
  (5,'Aoi Japan',27,0814245278,'aoi@gmail.com',3),
  (6,'Smith Eithy',45,0642813417,'smith@hotmail.com',4),
  (7,'Nok Noi',14,NULL,'nok@hotmail.com',6),
  (8,'John Welcome',24,0986351147,'john@gmail.com',4),
  (9,'Chinghi Quan',28,0825241741,'chinghi@gmail.com',2),
  (10,'Ekkachai Rachayo',26,0612784485,'ekkachai@gmail.com',6);

INSERT INTO chefs VALUES
  (1,'Tsunami Walter',85000,3),
  (2,'Eian Master',120000,6),
  (3,'Dollar Annie',52000,4);

INSERT INTO menus VALUES
  (1,'Fried chicken',350),
  (2,'Omelet',100.50),
  (3,'Pizza',299),
  (4,'Kebab',70),
  (5,'Fried Fish',199),
  (6,'Steak',259),
  (7,'Fried Rice',99),
  (8,'Soup',79),
  (9,'Meatball',129),
  (10,'Lasagna',499);

INSERT INTO orders VALUES
(1,7,7,1),
(2,5,9,2),
(3,7,5,2),
(4,6,10,1),
(5,9,3,2),
(6,3,2,3),
(7,5,9,3),
(8,10,3,2),
(9,2,2,3),
(10,6,8,3),
(11,2,6,2),
(12,6,10,3),
(13,4,9,2),
(14,8,9,2),
(15,1,9,1),
(16,2,7,3),
(17,1,10,2),
(18,6,4,3),
(19,6,2,1),
(20,10,4,1),
(21,3,9,2),
(22,2,2,2),
(23,9,8,1),
(24,5,9,2),
(25,2,9,2),
(26,9,4,3),
(27,9,10,2),
(28,8,2,3),
(29,7,6,3),
(30,4,5,1),
(31,4,3,1),
(32,10,5,2),
(33,2,2,3),
(34,3,3,1),
(35,2,9,3),
(36,7,9,2),
(37,9,4,1),
(38,10,7,3),
(39,5,8,2),
(40,6,2,2),
(41,10,2,2),
(42,10,6,1),
(43,4,1,3),
(44,5,2,3),
(45,4,6,1),
(46,6,7,1),
(47,2,3,3),
(48,4,1,3),
(49,9,10,3),
(50,2,1,1),
(51,4,10,3),
(52,2,7,1),
(53,6,2,1),
(54,10,1,1),
(55,3,2,2),
(56,4,1,3),
(57,1,9,2),
(58,10,2,2),
(59,2,4,1),
(60,5,6,2),
(61,3,1,3),
(62,8,1,3),
(63,2,7,1),
(64,5,6,3),
(65,8,10,1),
(66,4,1,3),
(67,3,3,2),
(68,9,5,1),
(69,10,8,3),
(70,3,1,2),
(71,7,10,3),
(72,5,6,2),
(73,5,3,3),
(74,1,8,3),
(75,2,6,3),
(76,1,9,2),
(77,3,4,2),
(78,6,10,2),
(79,6,10,3),
(80,10,3,3),
(81,5,7,3),
(82,7,2,1),
(83,10,4,3),
(84,6,3,1),
(85,4,8,2),
(86,10,7,1),
(87,7,10,2),
(88,1,3,2),
(89,2,5,3),
(90,3,8,3),
(91,8,9,3),
(92,1,1,2),
(93,6,5,2),
(94,1,7,1),
(95,9,2,3),
(96,3,1,2),
(97,7,6,1),
(98,4,1,3),
(99,1,9,3),
(100,2,4,1);


.mode column
.header on

--Query 1:Find the customers who order the most price
SELECT
  orders.customerid AS ID,
  customers.customername AS Name,
  COUNT(orders.customerid) AS Total_Purchase,
  SUM(menus.price) AS Total_Price
FROM customers,orders,menus
WHERE orders.customerid = customers.customerid
  AND orders.menuid = menus.menuid
GROUP BY ID
ORDER BY Total_Price DESC;

--Query 2:What country are the customers in the most?
SELECT
  countryname AS Country,
  COUNT(customers.countryid) AS Total
FROM customers,countrys
WHERE customers.countryid = countrys.countryid
GROUP BY Country
ORDER BY Total DESC;

--Query 3:Which chef cooks the most?
SELECT
  orders.chefid AS ID,
  chefs.chefname AS Chef_Name,
  COUNT(orders.chefid) AS Total_Cooks
FROM orders,chefs
WHERE orders.chefid = chefs.chefid
GROUP BY ID
ORDER BY Total_Cooks DESC;

--Query 4:Find the number of people who eat fried rice.
SELECT
  ID,
  Name,
  COUNT(ID) AS Total_Order_Omelet
FROM(SELECT
      orders.customerid AS ID,
      customers.customername AS Name,
      orders.menuid AS MenuID,
      menuname AS MenuName
    FROM customers,orders,menus
    WHERE orders.customerid = customers.customerid
      AND orders.menuid = menus.menuid)
WHERE MenuName = 'Omelet'
GROUP BY ID,Name
ORDER BY Total_Order_Omelet DESC;

--Query 5:Which menu is the most popular?
WITH OrderAll AS(
  SELECT
      orders.menuid AS MenuID,
      menuname AS MenuName
  FROM customers,orders,menus
  WHERE orders.customerid = customers.customerid
    AND orders.menuid = menus.menuid
)

SELECT 
  MenuName,
  COUNT(MenuName) AS Total_Orders
FROM OrderAll
GROUP BY MenuName
ORDER BY Total_Orders DESC;