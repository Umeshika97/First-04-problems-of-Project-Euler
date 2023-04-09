# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 22:36:16 2021

@author: acer
"""
#The library is imported to calculate executing time
from datetime import datetime 
#The variable is create to get the starting time when the code is run
starttime=datetime.now()
Total_sum = 0#The variable is created to initialize the total sum 
initial_value=0#The variable is created to initialize the initial value 
#The variable is created to initialize the first value of is Fibonacci sequence
second_Intvalue=1

while second_Intvalue < 4000000:#All natural numbers are selected below 4,000,000 
#All the even numbers of Fibonacci sequence are selected 
    if second_Intvalue % 2 == 0:
    #After that the sum of the even-valued terms were calculated
        Total_sum= Total_sum + second_Intvalue
    #   using while loop assigns the first and second initial values again and again 
    initial_value,second_Intvalue= second_Intvalue,initial_value + second_Intvalue
print(Total_sum)#The answer of total summatoin is printed
"""The code executing time is calculated using
 difference of the start time and end time"""
print (datetime.now()-starttime)



