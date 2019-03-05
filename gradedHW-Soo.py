#!/usr/bin/env python
# coding: utf-8

# In[2]:


#This function takes a list and prints out each item in a list and its type

data_input=['hello',3,'5',3.2,'7.4',[1,2,'world']]

def type_of_data(list_data):
    for item in list_data:
      print (str(item) + " is " + str(type(item)))

type_of_data(data_input)

