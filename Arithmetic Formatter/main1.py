# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 11:03:42 2021

@author: peace
"""

# This entrypoint file to be used in development. Start by reading README.md
from arithmetic_arranger import arithmetic_arranger
from unittest import main



#print("  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------")

#print("   32         1      45      123\n- 698    - 3801    + 43    +  49\n-----    ------    ----    -----\n -666     -3800      88      172")

#print('------------------------------')

#print(arithmetic_arranger(["32 - 698", "3801 + 2", "45 + 43", "123 + 49"]))
#print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"],True))

# Run unit tests automatically
main(module='test_module', exit=False)

