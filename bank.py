class bank :
    
    global db 
    db = {"a":["bal","loan","lst_add "]}
    
    def __init__(self,name):
        self.bal = 0 
        self.loan = 0 
        self.name = name
        self.lst_add = 0 
        db[self] = [self.name,self.bal ,self.loan,self.lst_add]
        
    def deposit(self, a,val ):
        db[self][1] +=val 
        
        
        
        
        
    def display(self ,name):
        if name  in db :
            print(db[name])
        else:
            print("NO Account ")
        
    
    
    
a = bank("uday")
a.deposit("uday",10)
a.display("uda")
b = bank("k")
b.display("k")



        
        
    
    
    
    