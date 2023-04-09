# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 21:34:20 2021

@author: acer
"""
#The library is imported to calculate executing time
from datetime import datetime 
#The variable is create to get the starting time when the code is run
start=datetime.now()
Total_Sum35= 0#The variable is created to initialize the total sum 

for a in range(1000): #All natural numbers are selected below 1000
    if (a%3 == 0 or a%5 == 0):#All the multiples of 3 or 5 are selected
    #The sum of all the multiples of 3 or 5 are calculated 
        Total_Sum35 = Total_Sum35+a 

print (Total_Sum35)#The answer of total sum is printed

"""The code executing time is calculated using
 difference of the start time and end time"""
print (datetime.now()-start)


