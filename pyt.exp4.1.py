# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 11:02:08 2026

@author: User
"""
# Taking list input from the user 
n=int(input("Enter numbers of element:"))
numbers=[]

for i in range(n):
    num= int(input(f"Enter element{i+1}:"))
    numbers.append(num)
    
# calculating sum and average
total=sum(numbers)
average=total/n if n>0 else 0

print("List:",numbers)
print("sum of elements:",total)
print("Average of elements:",average)
   
# %%

