#!/usr/bin/env python
# coding: utf-8

# In[5]:


list = []
n=int(input("Enter number of elemnets:"))   
for i in range(0, n):
    elements = int(input())
    list.append(elements)
S=1
for j in list:
    S=S*j
print(S)


# In[4]:


list=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
import operator
list.sort(key=operator.itemgetter(1))
print(list)


# In[44]:


d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}
for i, j in d1.items():
    for x, y in d2.items():
        if i == x:
            d3[i]=(j+y)
print(d3)


# In[36]:


n=int(input("Enter number of elements: "))
    S={i : i*i for i in range (1,n+1)}:
               print(S)


# In[33]:


list= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
import operator
list.sort(key=operator.itemgetter(1),reverse=True)
print(list)


# In[22]:





# In[ ]:




