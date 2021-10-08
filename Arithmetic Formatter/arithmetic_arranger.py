# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 10:45:51 2021

@author: peace
"""
import re

def arithmetic_arranger(*problems):

  #first to judge if the problem can be continued
  if len(problems[0]) > 5:
    raise Exception("Error: Too many problems.") 
  for strs in problems[0]:
    if re.search("[*/]", strs):
      raise Exception("Error: Operator must be '+' or '-'.")
    elif re.search("[a-zA-Z]", strs):
      raise Exception("Error: Numbers must only contain digits.")
    else:
      for i in strs.split():
        if len(i)>4:
          raise Exception("Error: Numbers cannot be more than four digits.")
  
  #second start to process the str array for further use
  #print(cal)
  cal=[]
  for item in problems[0]:
    cal1=item.split()
    if cal1[1]=='+':
        cal1.append(int(cal1[0])+int(cal1[2]))
    else:
        cal1.append(int(cal1[0])-int(cal1[2]))
    cal1.append(max(len(cal1[0]),len(cal1[2]),len(str(cal1[3]))+2))
    cal.append(cal1)
    

  #third to print the array
  #generate print format expression
  fmt=''
  for j in range(0,len(cal)):#len(cal) columns of equations to print
    fmt+=('{:>'+str(cal[j][4])+'}'+'    ') 
  fmt=fmt.strip()+'\n'
    
  answer=''

  if len(cal)==4:
    answer=((fmt).format(cal[0][0],cal[1][0],cal[2][0],cal[3][0]))+\
            ((fmt).format(cal[0][1]+' '*(cal[0][4]-len(cal[0][2])-1)+cal[0][2],
                        cal[1][1]+' '*(cal[1][4]-len(cal[1][2])-1)+cal[1][2],
                        cal[2][1]+' '*(cal[2][4]-len(cal[2][2])-1)+cal[2][2],
                        cal[3][1]+' '*(cal[3][4]-len(cal[3][2])-1)+cal[3][2]))+\
            ((fmt).format('-'*cal[0][4],'-'*cal[1][4],'-'*cal[2][4],'-'*cal[3][4]))

  elif len(cal)==5:
    answer=((fmt).format(cal[0][0],cal[1][0],cal[2][0],cal[3][0],cal[4][0]))+\
        ((fmt).format(cal[0][1]+' '*(cal[0][4]-len(cal[0][2])-1)+cal[0][2],
                      cal[1][1]+' '*(cal[1][4]-len(cal[1][2])-1)+cal[1][2],
                      cal[2][1]+' '*(cal[2][4]-len(cal[2][2])-1)+cal[2][2],
                      cal[3][1]+' '*(cal[3][4]-len(cal[3][2])-1)+cal[3][2],
                      cal[4][1]+' '*(cal[4][4]-len(cal[4][2])-1)+cal[4][2]))+\
        ((fmt).format('-'*cal[0][4],'-'*cal[1][4],'-'*cal[2][4],'-'*cal[3][4],'-'*cal[4][4]))

  if len(problems)>1:
    if len(cal)==4:
      answer+=((fmt).format(cal[0][3],cal[1][3],cal[2][3],cal[3][3]))

    if len(cal)==5:
      answer+=((fmt).format(cal[0][3],cal[1][3],cal[2][3],cal[3][3],cal[4][3]))
      
  print(answer)
  return answer



   
