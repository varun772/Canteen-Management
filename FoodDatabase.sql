DROP DATABASE IF EXISTS `CANTEEN`;
CREATE SCHEMA `CANTEEN`;
USE `CANTEEN`;
DROP TABLE IF EXISTS `Customers`;
CREATE TABLE Customers(
    Name varchar (100) NOT NULL,
    Gender char NOT NULL,
    ID int NOT NULL,
    Role varchar (100) NOT NULL,
    EmailID varchar (100) NOT NULL,
    Amount int NOT NULL);
ALTER TABLE Customers ADD PRIMARY KEY (ID); 
DROP TABLE IF EXISTS `Stall`;
CREATE TABLE Stall(
    Stallname varchar (100) NOT NULL,
    ID int NOT NULL,
    Openingtime TIME NOT NULL,
    Closingtime TIME NOT NULL,
    Duration TIME NOT NULL);
ALTER TABLE Stall ADD PRIMARY KEY (ID);
DROP TABLE IF EXISTS `Dependents`;
CREATE TABLE Dependents(
    CustomerID int NOT NULL,
    Dependentname varchar(50) NOT NULL,
    DependentGender char NOT NULL);
DROP TABLE IF EXISTS `CustomerNumber`;
CREATE TABLE CustomerNumber(
    CustomerID int NOT NULL,
    Customername varchar(100) NOT NULL,
    Phonenumber varchar(100) NOT NULL);
ALTER TABLE CustomerNumber ADD PRIMARY KEY (Phonenumber); 
DROP TABLE IF EXISTS `Breakfast`;
CREATE TABLE Breakfast(
    SID int NOT NULL,
    Item varchar(100) NOT NULL,
    Price int NOT NULL);
DROP TABLE IF EXISTS `Lunch`;
CREATE TABLE Lunch(
    SID int NOT NULL,
    Item varchar(100) NOT NULL,
    Price int NOT NULL);
DROP TABLE IF EXISTS `Dinner`;
CREATE TABLE Dinner(
    SID int NOT NULL,
    Item varchar(100) NOT NULL,
    Price int NOT NULL);
DROP TABLE IF EXISTS `ExpenditureCalculation`;
CREATE TABLE ExpenditureCalculation( 
    StallID int NOT NULL,
    Edate DATE NOT NULL,
    BOrderNumber varchar(100) NOT NULL,
    EmployeeID int NOT NULL);
DROP TABLE IF EXISTS `Bill`;
CREATE TABLE Bill(
    CustomerID int NOT NULL,
    Name varchar(100) NOT NULL,
    StallID int NOT NULL,
    Amount int NOT NULL,
    DateandTime TIMESTAMP NOT NULL,
    Ordernumber varchar(100) NOT NULL);      
ALTER TABLE Bill ADD PRIMARY KEY (Ordernumber);
DROP TABLE IF EXISTS `StallMaintenance`;
CREATE TABLE StallMaintenance(
    StallID int NOT NULL,
    Sdate DATE NOT NULL,
    Income int NOT NULL,
    Expenditure int NOT NULL);
ALTER TABLE StallMaintenance ADD PRIMARY KEY (Sdate,StallID);
DROP TABLE IF EXISTS `Employee`;
CREATE TABLE Employee(
    Name varchar(100) NOT NULL,
    Gender char NOT NULL,
    ID int NOT NULL,
    StallID int NOT NULL,
    Role varchar(100) NOT NULL,
    Salary int NOT NULL,
    Workingdays int NOT NULL,
    ManagerID int NOT NULL);
ALTER TABLE Employee ADD PRIMARY KEY (ID);
ALTER TABLE Breakfast ADD FOREIGN KEY (SID) REFERENCES Stall(ID);
ALTER TABLE Lunch ADD FOREIGN KEY (SID) REFERENCES Stall(ID);
ALTER TABLE Dinner ADD FOREIGN KEY (SID) REFERENCES Stall(ID);
ALTER TABLE Dependents ADD FOREIGN KEY (CustomerID) REFERENCES Customers(ID);
ALTER TABLE CustomerNumber ADD FOREIGN KEY (CustomerID) REFERENCES Customers(ID);
/*ALTER TABLE ExpenditureCalculation ADD FOREIGN KEY (StallID,Edate) REFERENCES StallMaintenance(StallID,Sdate);*/
ALTER TABLE ExpenditureCalculation ADD FOREIGN KEY (Edate,StallID) REFERENCES StallMaintenance(Sdate,StallID);
/*ALTER TABLE ExpenditureCalculation ADD FOREIGN KEY (Edate) REFERENCES StallMaintenance(Sdate);*/
ALTER TABLE ExpenditureCalculation ADD FOREIGN KEY (StallID) REFERENCES Stall(ID);
ALTER TABLE StallMaintenance ADD FOREIGN KEY (StallID) REFERENCES Stall(ID);
ALTER TABLE Employee ADD FOREIGN KEY (StallID) REFERENCES Stall(ID);
ALTER TABLE ExpenditureCalculation ADD FOREIGN KEY (BOrdernumber) REFERENCES Bill(Ordernumber);
ALTER TABLE ExpenditureCalculation ADD FOREIGN KEY (EmployeeID) REFERENCES Employee(ID);
ALTER TABLE Employee ADD FOREIGN KEY (ManagerID) REFERENCES Employee(ID);
LOCK TABLES `Customers` WRITE;
INSERT INTO Customers VALUES('Lokesh Paidi','M',1,'Student','Lokesh.paidi@students.iiit.ac.in',0);
INSERT INTO Customers VALUES('Kasam Kranthi','M',2,'TA','kranthi.kumar@students.iiit.ac.in',143);
INSERT INTO Customers VALUES('Chelpuri Abhijith','M',3,'Student','abhijith.chelpuri@students.iiit.ac.in',420);
UNLOCK TABLES;
LOCK TABLES `CustomerNumber` WRITE;
INSERT INTO CustomerNumber VALUES('1','Lokesh Paidi','8989898989');
INSERT INTO CustomerNumber VALUES('2','Kasam Kranthi','9898989898');
INSERT INTO CustomerNumber VALUES('3','Chelpuri Abhijith','9797979797');
UNLOCK TABLES;
LOCK TABLES `Stall` WRITE;
INSERT INTO Stall VALUES ('Night station',1,'18:00:00','03:00:00','09:00:00');
INSERT INTO Stall VALUES ('Tantra Food stall',2,'13:00:00','23:00:00','10:00:00');
INSERT INTO Stall VALUES ('Juice stall',3,'14:00:00','02:00:00','12:00:00');
INSERT INTO Stall VALUES ('Yellow Box',4,'08:00:00','21:00:00','13:00:00');
UNLOCK TABLES;
LOCK TABLES `Breakfast` WRITE;
INSERT INTO Breakfast VALUES(4,'Idly',20);
INSERT INTO Breakfast VALUES(4,'Dosa',25);
INSERT INTO Breakfast VALUES(4,'Upma',20);
UNLOCK TABLES;
LOCK TABLES `Lunch` WRITE;
INSERT INTO Lunch VALUES(2,'Veg Fried rice',50);
INSERT INTO Lunch VALUES(2,'Egg Noodles',65);
INSERT INTO Lunch VALUES(2,'Biryani',80);
UNLOCK TABLES;
LOCK TABLES `Dinner` WRITE;
INSERT INTO Dinner VALUES(2,'Veg Noodles',55);
INSERT INTO Dinner VALUES(3,'Egg Noodles',65);
INSERT INTO Dinner VALUES(3,'Chicken Noodles',80);
UNLOCK TABLES;