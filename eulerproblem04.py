# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 11:19:16 2021

@author: Umeshika
"""
#The library is imported to calculate executing time
from datetime import datetime
#The variable is created to get the starting time when the code is run 
starttime=datetime.now()
#the two variables were defined with the smallest 3-digit numbers
a=100
b=100
"""The variable is created for the Largest palindrome
 product and initialized the value"""
product_of_ab=0
#The function is defined to get the palindrome number
def palindromeNo(n):
#The variable is defined to get the number as string value    
    No_Word=str(n) 
#check whether the string value forward and backward are equal each other       
    if No_Word == No_Word[::-1]:
#the string value forward and backward way are equal each other and give 1        
        return 1
#the string value forward and backward are not equal each other and give 0     
    else:
        return 0
#a and b is defined in range 100 to 999
for a in range(100,1000):
    for b in range(100,1000):
        if palindromeNo(a*b)==1 and (a*b)>product_of_ab:
#the Largest palindrome product was taken by multipling a and b             
            product_of_ab=(a*b)
            print(a,"X",b)
print(product_of_ab) #final answer is printed 
"""The code executing time is calculated using
 difference of the start time and end time"""
print (datetime.now()-starttime)   