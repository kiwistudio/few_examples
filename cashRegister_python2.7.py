class CashRegister(object):
    "Simple CashRegister class"
    
    def __init__(self):
        
        print '_'*10, 'A new CashRegister', '_'*10
        self.storage = {'apples': [12, 7.05], 'eggs': [0, 12.02], 'oranges': [45, 15.2], 'wheat': [100, 32.6]}
        self.CHECK = []
        self.IND = []
        self.total = 0
        

    def print_storage(self):       
        'Prints sontents of storage'
        
        print '-'*10, 'Storage', '-'*10
        for item in self.storage:
            print self.storage[item][0], ' of ', item, ' for ', self.storage[item][1], ' per item'
        print '-'*29


    def  add_product(self, product, quantity, price):
        "Adds product to storage"
        
        self.storage[product] = [quantity, float(price)]
        

    def change_product_price(self, product, new_price):
        "Change price of specified product"
        
        if product in self.storage:
            print 'Change price for', product, 'from', self.storage[product][1], 'to', new_price + 0.00
            self.storage[product][1] = new_price
        else:
            print 'Product', product, 'is not in storage'


    def print_check(self):
        "Print all items in check to screen"
        
        print '-'*10, 'Check', '-'*10
        for item in range(len(self.CHECK)):
            print self.CHECK[item][1], 'units of', self.CHECK[item][0] , 'for', float(self.CHECK[item][2]), 'money'
        print 'total cost: ', self.coast
        print '-'*27


    def buy(self, product, quantity):
        "Main buying operation. Adds product to check, updates cash_check"
        
        if product in self.storage:
            self.CHECK.append((product, quantity, (self.storage[product][1] * quantity)))
            self.coast = 0        
            if quantity <= self.storage[product][0]:
                if self.storage[product][0] > 0:
                    for i in range (len(self.CHECK)):
                        self.storage[self.CHECK[i][0]][0] -= self.CHECK[i][1]
                for item in range(len(self.CHECK)):
                    self.coast += float(self.CHECK[item-1][2])
                self.total = self.coast
                self.print_check()            
            else:
                self.CHECK.remove((product, quantity, (self.storage[product][1] * quantity)))
                print"'You can't buy more than there is in the storage!"
        else:
            print 'Product', product, 'is not in storage'
        
        
    def cancel(self, *args):
        
        self.IND = list(args)
        if args:
            for j in self.ind:
                self.coast -= float(self.CHECK[j][2])
                del(self.CHECK[j])                
        else:
            self.CHECK = []
            self.coast = 0
        self.IND = []
        self.print_check()


    def purchase(self):
        """To finish buying operation you should call this function.
        Removes products listed in check from storage, updates cash_register_total,
        refreshes the check and cash_check variables"""
        
        for i in range (len(self.CHECK)):      
            if self.storage[self.CHECK[i][0]][0] == 0:
                del(self.storage[self.CHECK[i][0]])
        self.coast = 0
        self.CHECK = []
        
          

    def print_total_cash(self):
        "Prints how many cash was made during session"
        
        print "Today we made", self.total
    

        
        
        
       
s = CashRegister()
s.print_storage() 
s.add_product('milk', 20 , 10.99)
s.print_storage()
print
s.change_product_price('milk', 11)
print
s.buy('milk', 10)
s.buy('wheat', 60)
s.buy('apples', 5)




