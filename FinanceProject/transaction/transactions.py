class Transaction:
    def __init__ (self,Date,Amount,Category):
        self.Date=Date
        self.Amount=Amount
        self.Category=Category
        self.next=None  
        self.prev=None
class Transaction_manager:
    def __init__(self):
        self.head=None
    def Income(self,Date,Amount,categories):
        tran=Transaction(Date,Amount,categories,)
        temp=self.head
        if self.head is None:
              self.head=tran
              return
        while temp is not None and temp.next is not None:
            temp=temp.next
        temp.next=tran # type: ignore
        tran.prev=temp  # type: ignore
        
    def display(self):
        temp=self.head
        while temp is not None:
            print(f" Date : {temp.Date} \n Amount : {temp.Amount} \n Category : {temp.Category}")
            temp=temp.next    
    
    def export(self):
        tran=[]
        temp=self.head
        while temp is not None:
            tran.append({"Date":temp.Date,
                              "Category":temp.Category,
                              "Amount":temp.Amount})
            temp=temp.next
        return tran