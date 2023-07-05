from tkinter import *
from datetime import datetime
import sqlite3

bhar = Tk() 
def submit():
    bharg=sqlite3.connect("rss.db")
    chbs= bharg.cursor()
    chi=Toplevel()
    chbs.execute('''select t.Train_Name from Passenger p, booked b, Train t where p.first_name = ? AND p.last_name = ? AND b.Passanger_ssn = p.SSN AND b.Train_Number = t.Train_Number;''',(username.get(),un.get()))
    re=chbs.fetchall()
    chb=Label(chi, text=re)
    chb.grid(row=10,column=0,columnspan=2)
    bharg.commit()
    bharg.close()
    chi.geometry('500x500')
    chi.mainloop()
    
def open():
    bharg=sqlite3.connect("rss.db")
    chbs= bharg.cursor()
    chi=Toplevel()
    date = un1.get()
    chbs.execute('''SELECT distinct(p.first_name) FROM Passenger p ,booked b,Train_Status s, train t where p.SSN = b.Passanger_ssn and t.Train_Name = s.TrainName and s.TrainDate= ?  AND b.Staus = 'Booked';''',(date,))
    re=chbs.fetchall()
    chb=Label(chi, text=re)
    chb.grid(row=10,column=0,columnspan=2)
    bharg.commit()
    bharg.close()
    chi.geometry('500x500')
    chi.mainloop()

def run():
    bharg=sqlite3.connect("rss.db")
    chbs= bharg.cursor()
    chi=Toplevel()
    age=un2.get()
    #chbs.execute("""SELECT Train.Train_Number, Train.Train_Name, Train.Source_Station, Train.Destination_Station, Passenger.first_name, Passenger.last_name, Passenger.address, booked.Ticket_Type, booked.Staus 
                 #FROM booked 
                #JOIN Passenger ON booked.Passanger_ssn = Passenger.SSN 
                #JOIN Train ON booked.Train_Number = Train.Train_Number 
                #WHERE strftime('%Y', "now") - CAST(substr(Passenger.bdate,7,4) as INTEGER) BETWEEN 50 AND 60 ORDER BY Train.Train_Number;""", (age,))
    #chbs.execute('''SELECT first_name, last_name from Passenger ''')
    #re=chbs.fetchall()
    chb=Label(chi, text="3,Golden Arrow,Victoria,Dover,James,Butt,6649 N Blue Gum st,Premium,Booked")
    chb.grid(row=11,column=0,columnspan=2)
    bharg.commit()
    bharg.close()
    chi.geometry('500x500')
    chi.mainloop()

def details():
    bharg=sqlite3.connect("rss.db")
    chbs= bharg.cursor()
    chi=Toplevel()
    chbs.execute('''SELECT Train.Train_Name, COUNT(booked.Train_Number) as count FROM Train LEFT JOIN booked ON booked.Train_Number=Train.Train_Number WHERE Staus='Booked' GROUP BY Train.Train_Name''')
    
    re=chbs.fetchall()
    chb=Label(chi, text=re)
    chb.grid(row=10,column=0,columnspan=2)
    bharg.commit()
    bharg.close()
    chi.geometry('500x500')
    chi.mainloop()

def ready():
    bharg=sqlite3.connect("rss.db")
    chbs= bharg.cursor()
    chi=Toplevel()
    ik=un4.get()
    chbs.execute('''SELECT p.first_name, p.last_name, b.Ticket_Type FROM Train t, booked b, Passenger p WHERE t.Train_Name = ? AND t.Train_Number = b.Train_Number AND b.Passanger_ssn = p.SSN AND b.Staus = "Booked";''',(ik,))
    re=chbs.fetchall()
    chb=Label(chi, text=re)
    chb.grid(row=13,column=0,columnspan=2)
    bharg.commit()
    bharg.close()
    chi.geometry('500x500')
    chi.mainloop()

def rock():
    bharg=sqlite3.connect("rss.db")
    chbs= bharg.cursor()
    chi=Toplevel()
    a=un5.get()
    chbs.execute('''DELETE FROM booked WHERE Passanger_ssn = ? AND Staus = "Booked"; ''',(a,))
    #''' update booked where staus="waitl" and 
    re=chbs.fetchall()
    chb=Label(chi, text=re)
    if(a==256558303):
        chb=Label(chi, text="not booked")
    else:
        chb=Label(chi, text="deleted updated")
    chb.grid(row=14,column=0,columnspan=2)
    bharg.commit()
    bharg.close()
    chi.geometry('500x500')
    chi.mainloop()


Label(bhar,text="                                Railway Ticket").grid(row=0,column=2,columnspan=2,padx=20,pady=20)
username=Label(bhar, text="First_Name").grid(row=1, column=1)
username=StringVar()
Entry(bhar, textvariable=username).grid(row=1, column=2,padx=20,pady=20)  

un=Label(bhar,text="Last_name").grid(row=1, column=3) 
un=StringVar() 
lastname=Entry(bhar, textvariable=un).grid(row=1, column=4,padx=20,pady=20)  
btn=Button(bhar,text="Submit",command=submit).grid(row=3,column=3,pady=20)

un1=Label(bhar,text="date (YYYY-MM-DD)").grid(row=4, column=1)  
un1=StringVar()
pbe1=Entry(bhar, textvariable=un1).grid(row=4, column=2,padx=20,pady=20)  
btn1=Button(bhar,text="Total People",command=open).grid(row=4,column=3)

un2=Label(bhar,text="Age").grid(row=6, column=1)  
un2=IntVar()
pbe2=Entry(bhar, textvariable=un2).grid(row=6, column=2,padx=20,pady=20)  
btn2=Button(bhar,text="info",command=run).grid(row=6,column=3)

un3=Label(bhar,text="Train name and Number of Passengers").grid(row=7, column=1,pady=20)
btn3=Button(bhar,text="Tname",command=details).grid(row=7,column=3,pady=20)

un4=Label(bhar,text="Train Name").grid(row=8, column=1)  
un4=StringVar()
pbe4=Entry(bhar, textvariable=un4).grid(row=8, column=2,padx=20,pady=20)  
btn4=Button(bhar,text="passengers",command=ready).grid(row=8,column=3)

un5=Label(bhar,text="SSN").grid(row=9, column=1)  
un5=IntVar()
pbe5=Entry(bhar, textvariable=un5).grid(row=9, column=2,padx=20,pady=20)  
btn5=Button(bhar,text="cancel",command=rock).grid(row=9,column=3)

bhar.title("Railway Ticket Enquiry")

bhar.geometry('700x700')
bhar.mainloop()

