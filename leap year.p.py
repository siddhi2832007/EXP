# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 10:00:36 2026

@author: siddhi kadam
"""

year = int(input("Enter year:"))
if (year % 400==0) or (year% 4==0 and year % 100!=0):
        print("Leap year")
        
else:
     print("Not a Leap Year")
