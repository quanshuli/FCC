# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:47:37 2021

@author: peace
"""

# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


print(1,add_time("11:06 PM", "2:02"))#pass
print(2,add_time("3:30 PM", "2:12"))#pass
print(3,add_time("11:55 AM", "3:12"))#pass
print(4,add_time("9:15 PM", "5:30"))#pass
print(5,add_time("11:40 AM", "0:25"))
print(6,add_time("2:59 AM", "24:00"))
print(7,add_time("11:59 PM", "24:05"))
print(8,add_time("8:16 PM", "466:02"))
print(9,add_time("5:01 AM", "0:00"))
print(10,add_time("3:30 PM", "2:12", "Monday"))
print(11,add_time("2:59 AM", "24:00", "saturDay"))
print(12,add_time("11:59 PM", "24:05", "Wednesday"))

print(13,add_time("8:16 PM", "466:02", "tuesday"))


# Run unit tests automatically
main(module='test_module', exit=False)