# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 13:06:19 2021

@author: peace
"""

import re

def add_time(*inputs):
  weekdays=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
  
  #parse time 
  start=re.split('[ :]',inputs[0])
  hours=int(start[0])
  mins=int(start[1])
  if start[2]=='PM':
    hours+=12

  duration=re.split(':',inputs[1])
  duration_hours=int(duration[0])
  duration_mins=int(duration[1])

  hours += duration_hours
  mins += duration_mins

  apm = 'AM'
  days = 0

  
  if mins >= 60:
    hours1, mins = divmod(mins, 60)
    hours += hours1
      
  if hours >= 24:
    days, hours= divmod(hours, 24)

  if hours >= 12:
    apm = 'PM'
    if hours > 12:
      hours -= 12

  if hours == 0:
    hours = 12

  theday = 0
  new_time = ''
  
  print(hours,apm,mins)


  if len(inputs) == 3:  
    for i in range(0,7):
      if weekdays[i].lower() == inputs[2].lower():
        if i + days > 6:
         dispose , theday = divmod(i + days,7)
        else:
          theday = i + days
    if days == 1:
      new_time = str(hours) + ':' + str(mins).zfill(2) + ' ' + apm + ', ' + weekdays[theday] + ' (next day)'
      return new_time
    elif days > 1:
      new_time = str(hours) + ':' + str(mins).zfill(2) + ' ' + apm + ', ' + weekdays[theday] + ' (' + str(days) + ' days later)'
      return new_time
    else:
      new_time = str(hours) + ':' + str(mins).zfill(2) + ' ' + apm + ', ' + weekdays[theday]
      return new_time
  elif len(inputs) == 2:
    if days == 1:
      new_time = str(hours) + ':' + str(mins).zfill(2) + ' ' + apm + ' (next day)'
      return new_time
    elif days > 1:
      new_time = str(hours) + ':' + str(mins).zfill(2) + ' ' + apm + ' (' + str(days) + ' days later)'
      return new_time
    else:
      new_time = str(hours) + ':' + str(mins).zfill(2) + ' ' + apm
      return new_time
  else:
    return "Wrong arguments!"

 