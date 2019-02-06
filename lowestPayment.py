#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Paste your code into this box
balance = 320000
annualInterestRate = 0.2

'''
when balance and annual InterstateRate are given, the following code returns the lowest monthly payment to pay the balance off in a year. The output will be to the cent.
'''

MonthlyInterestRate=annualInterestRate/12.0
LowerBound=balance/12
UpperBound=(balance*(1+MonthlyInterestRate)**12)/12.0


while True:
  newBalance=balance
  MinimumPay=(LowerBound+UpperBound)/2
  for i in range(12):
    UnpaidBalance=newBalance-MinimumPay
    interestCharge=MonthlyInterestRate*UnpaidBalance
    newBalance=UnpaidBalance+interestCharge
  if 0.01>newBalance>=0:
    MinimumPay=round(MinimumPay,2)
    print("Lowest Payment: "+str(MinimumPay))
    break
  elif newBalance>0.01:
    LowerBound=MinimumPay
  else:
    UpperBound=MinimumPay


# In[ ]:




