from transaction import Transaction_manager
class Account:
    def __init__(self,ACC_Name): #Account nodes will be created with the account name and a transaction manager to handle transactions for that account.
        self.ACC_Name=ACC_Name
        self.next=None
        self.prev=None
        self.transaction_manager=Transaction_manager() 
        
class Account_Manager:
    def __init__(self):
        self.head=None
    
    def insert(self,acc_name):
        names=Account(acc_name)
        if self.head is None:
            self.head=names
            return
        else:   
            temp=self.head
            while temp.next is not None:
             temp=temp.next
        temp.next=names # type: ignore
        names.prev=temp # pyright: ignore[reportAttributeAccessIssue]
        
    def display(self):
        temp=self.head
        i=1
        while temp is not None:
            print(f"{i}.{temp.ACC_Name}")       
            temp=temp.next
            i+=1
    def load(self,find):
        
        temp=self.head
        while temp is not None and temp.ACC_Name!=find:
            temp=temp.next
        if temp is None:
            return None
        print(f"--Welcome {temp.ACC_Name}--")
        return temp
        
    
    
    def save_account(self):
        store=[]
        temp=self.head
        while temp is not None:
            store.append({"Account Name " :temp.ACC_Name,
                               "Transactions " : temp.transaction_manager.export()})
            
            temp=temp.next
        print(store)
        return store           