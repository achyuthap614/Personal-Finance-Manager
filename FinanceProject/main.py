#Personal Finance Management System
#This code implements a simple personal finance management system using linked lists. It allows users to create accounts, load accounts, and manage transactions. Each account can have multiple transactions associated with it.

from datetime import datetime
from accounts import Account_Manager
import json
import os
if __name__=="__main__":        
 a1=Account_Manager()


 while True:
    if  os.path.exists("Account.json"):
        with open("Account.json","r") as f:
            data=json.load(f)
            for acc in data:
                a1.insert(acc["Account Name"])
                
    print("--Personal Finance Management--")
    print("1.Create Account")
    print("2.Load Account")
    print ("3.Delete Account")
    try:
     choice=int(input("Enter your choice : "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    if choice==1:
        name=input("Enter your name:")
        a1.insert(name)
        
        
    elif choice==2:
        try:
         print("Choose your ACCOUNT")
         a1.display()
         action=input("Do You wanna Load your Account : ")
         if action.lower()=="y" or action.lower()=="yes":
          choose_acc=input("Enter Account Name : ")
         else:
            print("Please give a valid input")
            continue
         person=a1.load(choose_acc)
         if person is None:
             print("Account not found. Please enter a valid account name.")
             continue
        except AttributeError:
            print("Account not found .Please enter a valid account name.")
            continue
        tran_option=input("Do yyou wanna add transaction (Y/N) ? : ")
        if tran_option.lower() =="y" or tran_option.lower()=="yes":
             pass
        else:
             continue
        Cateogory=["food","Transport","Entertainment","Bills","Medical","Other"]      
        while True:
         a=input("Enter Date (YY-MM-DD) : ")
         try:
          validate=datetime.strptime(a,"%Y-%m-%d")
         except ValueError:
             print("Invalid date format Please enter date in yy-mm-dd format")
         index=1
         for i in Cateogory:
             print(f"{index}.{i}")
             index+=1
         try:
          b=int(input(f"Choose the category :  "))
          if b<=len(Cateogory):
           b=Cateogory[b-1]
           print(f"You have choosen {b} category")
         except ValueError:
             print("Invalid Input. Please enter a number.")
             continue
         c=int(input("Enter the Transaction Amount :"))
         person.transaction_manager.Income(a,b,c)
         d=input("Do you wanna add more transaction (Y/N) ? : ")
         
         if d.lower()=="y" or d.lower()=="yes" :
            pass
         else:
             person.transaction_manager.display()
             break        
        
         
    
                            
        
    
    elif choice ==3:
        a1.save_account()
        with open("Account.json","w") as f:
            json.dump(a1.save_account(),f,indent=4)
        print("Account Data Saved Successfully.")    
        break
    
        