from tkinter import *
import csv
import sqlite3



bhar= sqlite3.connect('railway.db')
chb= bhar.cursor()
chb.execute('''CREATE TABLE booked(
   Passanger_ssn INTEGER  NOT NULL
  ,Train_Number  INTEGER  NOT NULL
  ,Ticket_Type   CHAR(7) NOT NULL
  ,Staus         CHAR(6) NOT NULL
);''')

chb.execute('''CREATE TABLE passenger(
    first_name VARCHAR(9) NOT NULL PRIMARY KEY
    ,last_name  VARCHAR(9) NOT NULL
    ,address    VARCHAR(21) NOT NULL
    ,city       VARCHAR(13) NOT NULL
    ,county     VARCHAR(14) NOT NULL
    ,phone      VARCHAR(12) NOT NULL
    ,SSN        INTEGER  NOT NULL
    ,bdate      DATE  NOT NULL);''')

chb.execute('''CREATE TABLE Train_status(
   TrainDate             DATE  NOT NULL
  ,TrainName             VARCHAR(17) NOT NULL
  ,PremiumSeatsAvailable INTEGER  NOT NULL
  ,GenSeatsAvailable     INTEGER  NOT NULL
  ,PremiumSeatsOccupied  INTEGER  NOT NULL
  ,GenSeatsOccupied      INTEGER  NOT NULL
);''')

chb.execute('''CREATE TABLE Train(
   Train_Number        INTEGER  NOT NULL 
  ,Train_Name          VARCHAR2 NOT NULL
  ,Premium_Fair        INTEGER  NOT NULL
  ,General_Fair        INTEGER  NOT NULL
  ,Source_Station      CHAR(10) NOT NULL
  ,Destination_Station CHAR(9) NOT NULL
);''')

f1= open('booked.csv')
ch1 = csv.reader(f1)
chb.executemany("INSERT INTO booked(Passanger_ssn,Train_Number,Ticket_Type,Staus) VALUES(?,?,?,?)", ch1)
f2= open('Train_status.csv')
ch2= csv.reader(f2)
chb.executemany("INSERT INTO Train_status(TrainDate,TrainName,PremiumSeatsAvailable,GenSeatsAvailable,PremiumSeatsOccupied,GenSeatsOccupied) VALUES(?,?,?,?,?,?)", ch2)
f3= open('Train.csv')
ch3= csv.reader(f3)
chb.executemany("INSERT INTO Train(Train_Number,Train_Name,Premium_Fair,General_Fair,Source_Station,Destination_Station) VALUES(?,?,?,?,?,?)", ch3)
f4= open('Passenger.csv')
ch4= csv.reader(f4)
chb.executemany("INSERT INTO Passenger(first_name,last_name,address,city,county,phone,SSN,bdate) VALUES(?,?,?,?,?,?,?,?)", ch4)
bhar.commit()
bhar.close()

