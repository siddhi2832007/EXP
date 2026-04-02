# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:41:03 2026

@author: User
"""

# creating an empty dictionary
student ={}

# Adding key - value pairs
student["name"]=["siddhi"]
student["age"]=19
student["course"]="python"

print("Dictionary after adding elements:")
print(student)

# Updating a value
student["age"]=20

print("\nDictionary after updating a values:")
print(student)

# Deleting a key-values pair
del student["course"]

print("\nDictionary after deleting a key-value pair:")
print(student)
