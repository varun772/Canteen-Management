import subprocess as sp
import pymysql
import pymysql.cursors
import re
from datetime import date,datetime as dt,time,timedelta
from dateutil import parser
from dateutil.relativedelta import relativedelta
from tabulate import tabulate
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def viewTable(rows):
    a = []
    try:
        a.append(list(rows[0].keys()))
    except:
        print("\n-----------------\nEMPTY TABLE\n-----------------\n")
        return
    for row in rows:
        b = []
        for k in row.keys():
            b.append(row[k])
        a.append(b)
    print(tabulate(a, tablefmt="psql", headers="firstrow"))
    print()
def isValid(s): 
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}") 
    return Pattern.match(s)
def addbill():
    try:
        newbill={}
        newbill[0]=int(input("Customer ID:"))
        newbill[1]=input("Name of the person:")
        newbill[2]=int(input("StallID:"))
        newbill[3]=int(input("Amount:"))
        newbill[4]=input("Date and time:")
        print(newbill[4])
        temp=str(newbill[2])
        print(temp)
        newbill[5]=temp + "-" + newbill[4]
        print(newbill[5])
        input("enter1")
        query="INSERT INTO Bill VALUES('%d','%s','%d','%d','%s','%s')" %(newbill[0],newbill[1],newbill[2],newbill[3],newbill[4],newbill[5])
        base.cursor().execute(query)
        base.commit()
        #amount="SELECT Amount FROM Customers WHERE ID='%d'" % (newbill[0])
        #print(amount)
        #tmp = sp.call('clear', shell=True)
        #base.cursor().execute(amount)
        #print("Second Executed")
        #records=base.cursor().fetchall()
        #for row in records:
        #    print(row[0])
        #print("Printed")
        #value=value+newbill[3]
        #print(value)
        update="UPDATE Customers SET Amount = Amount + %d WHERE ID = '%d';" % (newbill[3],newbill[0])
        base.cursor().execute(update)
        base.commit()
    except Exception as exp:
        base.rollback()
        print("Failed")
        print(">>>>",exp)
def addcustomer():
    try:
        newcus={}
        newcus[0]=input("Name:")
        newcus[1]=input("Gender:")
        if(newcus[1]=="M" or newcus[1]=="F"):    
            newcus[2]=int(input("ID:"))
            newcus[3]=input("Role:")
            newcus[4]=input("EmailID:")
            if(re.search(regex,newcus[4])):    
                newcus[5]=int(input("Amount:"))
                newcus[6]=input("Phone Numbers:")
                numbers=newcus[6].split(" ")
                query="INSERT INTO Customers VALUES('%s','%c','%d','%s','%s','%d')" %(newcus[0],newcus[1],newcus[2],newcus[3],newcus[4],newcus[5])
                cur.execute(query)
                base.commit()
                for number in numbers:
                    if(isValid(number)):
                        phone="INSERT INTO CustomerNumber VALUES('%d','%s','%s')" % (newcus[2],newcus[0],number)
                        base.cursor().execute(phone)
                        base.commit()
                    else:
                        txt="{num} is not a valid phone number"
                        print(txt.format(number))
            else:
                print("Email is not valid")
        else:
            print("Gender is not valid")
    except Exception as exp:
        base.rollback()
        print("Failed")
        print(">>>>",exp)
def addstall():
    try:
        news={}
        news[0]=input("Stall name:")
        news[1]=int(input("Stall ID:"))
        news[2]=input("Opening time:")
        news[3]=input("Closing time:")
        start_time=dt.strptime(news[2],"%H:%M:%S")
        end_time=dt.strptime(news[3],"%H:%M:%S")
        if(end_time<start_time):
            end_time += timedelta(days=1)
        duration=end_time-start_time
        query="INSERT INTO Stall VALUES('%s','%d','%s','%s','%s')" % (news[0],news[1],news[2],news[3],duration)
        base.cursor().execute(query)
        base.commit()
    except Exception as exp:
        base.rollback()
        print("Failed")
        print(">>>>",exp)
def addDependent():
    try:
        newd={}
        newd[0]=int(input("Customer ID:"))
        newd[1]=input("DependentName:")
        newd[2]=input("DependentGender:")
        if(newd[2]=="M" or newd[2]=="F"):
            query="INSERT INTO Dependents VALUES('%d','%s','%c')" % (newd[0],newd[1],newd[2])
            cur.execute(query)
            base.commit()
        else:
            print("Gender is not valid")
    except Exception as exp:
        base.rollback()
        print("Failed")
        print(">>>>",exp)
def addEmployee():
    try:
        newem={}
        newem[0]=input("Name of the Employee:")
        newem[1]=input("Gender:")
        if(newem[1]=="M" or newem[1]=="F"):
            newem[2]=int(input("Employee ID:"))
            newem[3]=int(input("Stall ID:"))
            newem[4]=input("Role:")
            newem[5]=int(input("Salary:"))
            newem[6]=int(input("WorkingDays:"))
            newem[7]=int(input("ManagerID:"))
            query="INSERT INTO Employee VALUES('%s','%c','%d','%d','%s','%d','%d','%d')" % (newem[0],newem[1],newem[2],newem[3],newem[4],newem[5],newem[6],newem[7])
            cur.execute(query)
            base.commit()
        else:
            print("Gender is not valid")
    except Exception as exp:
        base.rollback()
        print("Failed")
        print(">>>>",exp)
def hikeEmployee():
    try:
        id=int(input("Employee ID:"))
        final=int(input("Final Salary:"))
        query="UPDATE Employee SET Salary='%d' WHERE ID='%d'" % (final,id)
        cur.execute(query)
        base.commit()
    except Exception as exp:
        base.rollback()
        print("Failed")
        print(">>>>",exp)
def deleteCustomer():
    try:
        delc={}
        delc[0]=int(input("Customer ID to be deleted:"))
        delphone="DELETE FROM CustomerNumber WHERE CustomerID=%d"%(delc[0])
        cur.execute(delphone)
        base.commit()
        query="DELETE FROM Customers WHERE ID='%d';" % (delc[0])
        cur.execute(query)
        base.commit()
    except Exception as exp:
        base.rollback()
        print("Failed")
        print(">>>>",exp)
def deleteEmployee():
    try:
        dele={}
        dele[0]=int(input("Employee ID to be deleted:"))
        query="DELETE FROM Employee WHERE ID='%d';" % (dele[0])
        cur.execute(query)
        base.commit()
    except Exception as exp:
        base.rollback()
        print("Failed")
        print(">>>>",exp)
def ListCustomerDetails():
    try:
        id=int(input("Customer ID:"))
        query="SELECT * FROM Customers WHERE ID='%d'" % (id)
        cur.execute(query)
        detail=cur.fetchall()
        viewTable(detail)
    except Exception as exp:
        base.rollback()
        print("Failed")
        print(">>>>",exp)
def Customerpaid():
    try:
        id=int(input("Customer ID:"))
        paid=int(input("Amount paid:"))
        query="UPDATE Customers SET Amount = Amount - %d WHERE ID=%d" % (paid,id)
        base.cursor().execute(query)
        base.commit()
    except Exception as exp:
        base.rollback()
        print("Failed")
        print(">>>>",exp)
def listabove500():
    try:
        query="SELECT * FROM Customers WHERE Amount>500"
        print(query)
        cur.execute(query)
        record=cur.fetchall()
        viewTable(record)
    except Exception as exp:
        base.rollback()
        print("Failed")
        print(">>>>",exp)
def totalspent():
    try:
        Cid=int(input("Customer ID:"))
        total="SELECT SUM(Amount) AS Total FROM Bill WHERE CustomerID = %d" % (Cid)
        cur.execute(total)
        spentrecords=cur.fetchall()
        viewTable(spentrecords)
    except Exception as exp:
        base.rollback()
        print("Failed")
        print(">>>>",exp)
def displaycustomers():
    query="SELECT * FROM Customers"
    print(query)
    cur.execute(query)
    record=cur.fetchall()
    viewTable(record)
def displaystalls():
    query="SELECT * FROM Stall"
    print(query)
    cur.execute(query)
    record=cur.fetchall()
    viewTable(record)
def displaybills():
    query="SELECT * FROM Bill"
    print(query)
    cur.execute(query)
    record=cur.fetchall()
    viewTable(record)
def displayemployees():
    query="SELECT * FROM Employee"
    print(query)
    cur.execute(query)
    record=cur.fetchall()
    viewTable(record)
def functions(given):
    if(given==1):
        addcustomer()
    elif(given==2):
        addbill()
    elif(given==3):
        addDependent()
    elif(given==4):
        addstall()
    elif(given==5):
        addEmployee()
    elif(given==6):
        hikeEmployee()
    elif(given==7):
        ListCustomerDetails()
    elif(given==8):
        deleteCustomer()
    elif(given==9):
        deleteEmployee()
    elif(given==10):
        listabove500()
    elif(given==11):
        Customerpaid()
    elif(given==12):
        totalspent()
    elif(given==13):
        displaycustomers()
    elif(given==14):
        displaystalls()
    elif(given==15):
        displaybills()
    elif(given==16):
        displayemployees()
    else:
        print("Invalid Option")    
givenhost=input("Enter host:")
givenuser=input("Enter user:")
givenport=int(input("Enter port:"))
givenpassword=input("Enter password:")
tmp = sp.call('clear', shell=True)
try:
    base= pymysql.connect(host=givenhost,user=givenuser,port=givenport,password=givenpassword,db= "CANTEEN", cursorclass=pymysql.cursors.DictCursor)
    tmp = sp.call('clear', shell=True)
    if(base.open):
        print("Connected")
    else:
        print("Connection failed")
    with base.cursor() as cur:
        while(1):
            print("Select 1 to add new customer")
            print("Select 2 to add a new bill")
            print("Select 3 to add a new dependent")
            print("Select 4 to add a new stall")
            print("Select 5 to add a new Employee")
            print("Select 6 to give hike to an Employee")
            print("Select 7 to list customer details")
            print("Select 8 to delete a customer")
            print("Select 9 to delete an employee")
            print("Select 10 to list employees with Amount>500")
            print("Select 11 if a customer paid some amount")
            print("Select 12 for amount spent by a customer")
            print("Select 13 to print all the customers")
            print("Select 14 to print all the stalls")
            print("Select 15 to print all the bills")
            print("Select 16 to print all the employees")
            print("Select 17 to exit")
            received=int(input("Enter choice:"))
            if(received==17):
                break
            else:
                functions(received)
except Exception as exp:
    tmp=sp.call('clear',shell=True)
    print("Connection to the database is failed")
    print(">>>>",exp)