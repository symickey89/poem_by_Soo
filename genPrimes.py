#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def prime_detector(number,primeList):
  for item in primeList:
    if number%item==0:
      return False
  return True

def genPrimes():
  primeList=[2]
  number=3
  yield 2
  while True:
      if prime_detector(number,primeList)==True:
        primeList.append(number)
        yield number
        number+=1
      else:
        number+=1

