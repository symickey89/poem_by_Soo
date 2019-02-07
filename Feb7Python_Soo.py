#!/usr/bin/env python
# coding: utf-8

# In[2]:


#doubleTheList takes a sequence of elements as an argument 
#and returns a list containing the original sequence and the 
#sequence of doubled elements as separate lists.


def doubleTheList(sequence):
    result=[sequence]
    doubledList=[]
    for element in sequence:
        doubledList=doubledList+[element*2]
    result=result+[doubledList]
    return result


# In[ ]:




