from tabulate import tabulate
import mysql.connector as mysql
headers=['S_NO','Company_Name','flight_model','Departure','Arrival','Date','time_of_departure','flight_terminal']
adminpass="jai20012007"
connection=mysql.connect(host="localhost",user="root",password="jai20012007",database="FLIGHTS")
cursor=connection.cursor()
def updateDate():
    starter=int(input("enter the S_NO of flight whose date you want to update-- "))
    updated=int(input("enter updated date-- "))
    cmd="update flight set Date = {updated} where S_NO = {starter}".format(updated=updated,starter=starter)
    cursor.execute(cmd)
    connection.commit()
    print("date updated!!")

def updateTime():
    starter = int(input("enter S_NO of flight whose time you want to update-- " ))  
    updated = input("enter time in [h:mm AM/PM] format-- ")
    cmd="update flight set time_of_departure='{time}' where S_NO={upt}".format(time=updated,upt=starter)  
    cursor.execute(cmd)
    connection.commit()
    print("time updated!!")

def updateTerminal():
    starter=int(input("enter S_NO of flight whose terminal you want to update-- "))
    updated=input("enter updated terminal-- ")
    cmd="update flight set flight_terminal='{term}' where S_NO={num}".format(term=updated,num=starter)
    cursor.execute(cmd)
    connection.commit()
    print("terminal updated")

def deleteFlight():
    S_NO=int(input("enter S_NO of the flight you want to delete-- "))
    cmd="delete from flight where S_NO ={S}".format(S=S_NO)
    cursor.execute(cmd)
    connection.commit()
    print("flight schedule deleted  ===> FLIGHT CANCLED...")

def addFlight():
    S_NO=int(input("enter serial number-- "))
    Company_Name=input("enter company's name-- ")
    Flight_model=input("enter flight's model-- ")
    Departure=input("enter departure place-- ")
    Arrival=input("enter arrival place-- ")
    Date=int(input('enter date of departure-- '))
    time=input("enter time of departure-- ")
    terminal=input("enter terminal from where the flight will take of-- ")
    cmd="insert into flight values({num},'{com}','{fmod}','{dep}','{arr}',{date},'{time}','{terminal}')".format(num=S_NO,com=Company_Name,fmod=Flight_model,dep=Departure,arr=Arrival,date=Date,time=time,terminal=terminal)
    cursor.execute(cmd)
    connection.commit()
    print("new flight schedule added...")

def viewFlights():
    cmd="select *from flight"
    cursor.execute(cmd)
    val=cursor.fetchall()
    fval=[]
    for i in val:
        fval.append(i)
    print("here are all the available flights----=====>>>>>")
    print(' ')
    print(tabulate(fval,headers=headers))
    print(' ')

def selectFlight():
    selection=int(input("enter S_NO of the flight you want to choose-- "))
    cmd="select *from flight where S_NO={num}".format(num=selection)
    cursor.execute(cmd)
    val=cursor.fetchall()
    fval=[]
    for i in val:
        fval.append(i)
    print("detailes of your chosen flight are as follows-----=====>>>>>")
    print(' ')
    print(tabulate(fval,headers=headers))
    print(' ')

while(True):
    print(""" **************----->>>>>>>>>>>>> [[BOOK MY FLIGHT]]<<<<<<<<<<<<<-----**************
          
          1. Admin
          2. User
          3. Exit application""")
    choice=int(input("enter your choice (1/2/3)-- "))

    if choice ==2:
        print(""" WELCOME USER TO BOOK MY FLIGHT!!!!
              1. View flights
              2. Book flight
              3. Exit """)
        choice1=int(input("enter your choice (1/2/3)-- "))
        if choice1==1:
            viewFlights()
            continue
        elif choice1==2:
            selectFlight()
            print(' ')
            print("press ctrl button plus click the below url to access booking confirmarion")
            print(' ')
            print("close terminal to view confirmation----")
            print(' ')
            print("file:///C:/Users/Jai%20Ratna/Downloads/DocScanner%2012-Aug-2024%205-38%E2%80%AFpm.pdf")
            print(' ')
            continue
        elif choice1==3:
            print("thanks for visiting!!")
            continue
        else:
            print("invalid input$$$") 
    
    elif choice ==3:
        print("thanks for visiting!!")
        connection.close()
        break

    elif choice==1:
        enterpassword=input("enter passwrd to log in-- ")
        if enterpassword == adminpass:
            print(""" WELCOME ADMIN TO BOOK MY FLIGH!!!!
               1. update date
               2. update time 
               3. update terminal
               4. add flight
               5. delete flight
               6. Exit""")
            choice2 = int(input("enter your choice (1/2/3/4/5/6)"))
            if choice2 ==1:
                updateDate()
                continue
            elif choice2==2:
                updateTime()
                continue
            elif choice2==3:
                updateTerminal()
                continue
            elif choice2==4:
                addFlight()
                continue
            elif choice2==5:
                deleteFlight()
                continue
            elif choice2==6:
                print("thanks for visiting!!")
                continue
            else:
                print("invalid input:::::::::::::::::::::::::::::::::::::::::")
        else:
            print("incorrect password!!!!!!")
            continue
    else:
        print("invalid input$$$$")
        break
