#!/usr/bin/env python
# coding: utf-8

# In[ ]:


string=input("Enter a string:")
newstring=string[0]+string[1:].replace(string[0],'$')
print("The new string is",newstring)

