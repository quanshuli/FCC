# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 16:36:06 2021

@author: peace
"""

class Category:
    
    ledger = []
    amount = 0
    name = ''
        
    def __init__(self, name):
        self.ledger = []
        self.amount = 0
        self.name = name
        
    def __str__(self):
        output = ''
        for item in self.ledger:
            output += ((item['description'].ljust(23) 
                       if len(item['description']) < 23 
                       else item['description'][0:23]) 
                        + str(item['amount']).rjust(7) + '\n')
            
        output = (self.name.center(30,'*') + '\n' + output
                  + 'Total:' + str(self.amount))
                  
        return output
        
    def deposit(self, amount, description=''):
        
        self.amount += amount
        self.ledger.append({'amount':amount ,
                       'description':description})
        
    def withdraw(self, amount, description='withdraw'):
        
        if self.amount < amount:
            return False
        else:
            self.amount-=amount
            self.ledger.append({'amount':amount*-1 ,
                       'description':description})
            return True
        
    def get_balance(self):
        
        return self.amount
    
    def transfer(self,amount, a_category):
        
        self.withdraw(amount,'Transfer to '+a_category.name)
        a_category.deposit(amount, 'Transfer from '+self.name)
        
        return True
        
        
    def check_funds(self,amount):
        if amount > self.amount:
            return False
        else:
            return True
        
def create_spend_chart(obj):
    import math
    
    spend = []
    withdraw = []
    deposit = []
    for i in range(0,len(obj)):

        for item in obj[i].ledger:
            if item['description'] == 'withdraw':
                withdraw.append(item['amount'] * -1)
            elif item['description'] == 'deposit':
                deposit.append(item['amount'] )
            
    #print(deposit,withdraw)
    for i in range(0,len(deposit)):
        spend.append((withdraw[i] / deposit[i]) * 100)
        
    #print(spend)
    output = 'Percentage spent by category'
    number = 100
    while True:
        output += '\n' + str(number).rjust(3) + '| '
        
        for i in range(0,len(spend)):
            if spend[i] > number:
                output += 'o  '
            else:
                output += '   '
                       
        number -= 10
        if number < 0:
            break
        
    output += '\n    ' + '-' * 10
    
    for i in range(0,len(obj)):
        obj[i].name[0].upper()
         
    count = 0
    while True:
        output += '\n    |'
        
        for i in range(0,len(obj)):
            if len(obj[i].name) > count:
                output += obj[i].name[count]+'  '
            else:
                output += '   '
                
        count += 1
        
        if all(count > len(obj[i].name) for i in range(0,len(obj))):
            break
    
    return output
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    