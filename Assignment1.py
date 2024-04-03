#!/usr/bin/env python
# coding: utf-8

# In[17]:


def github() -> str:
 
    return "https://github.com/AlisonH0/Econ-481.git"


# In[44]:


#Excercise 2
def evens_and_odds(n: int) -> dict:
    evens = 0
    odds = 0
    for i in range(n):
        if i % 2 == 0:
            evens += i
        else:
            odds += i
    dict = {
        'evens': evens,
        'odds' : odds
    }
    return dict

evens_and_odds(4)


# In[45]:


#Excercise 3
from typing import Union
from datetime import datetime, date, time, timedelta

def time_diff(date_1: str, date_2: str, out: str) -> Union[str,float]:
    dt1 = datetime.strptime(date_1, "%Y-%m-%d")
    dt2 = datetime.strptime(date_2, "%Y-%m-%d")

    timeDiff = dt2 - dt1
    result = abs(timeDiff.days)
    
    if isinstance(out, str):
        return "There are " + str(result) + " days between the two dates"

    return result

#time_diff('2020-01-01', '2020-01-02', 'float')
time_diff('2020-01-03', '2020-01-01', 'string')


# In[41]:


def reverse(in_list: list) -> list:

    list2 = []
    
    for i in range(len(in_list)-1, -1, -1):
        list2.append(in_list[i])
    
    return list2

reverse(['a', 'b', 'c'])


# In[16]:


#Excercise 5
def prob_k_heads(n: int, k: int) -> float: # n > k
    nFact = kFact = diffFact = probK = probDiff = 1.
    diff = n-k
    
    for i in range(1, n+1):
        nFact *= i
    for i in range(1, k+1):
        kFact *= i
        probK *= 0.5
    for i in range(1, diff+1):
        diffFact *= i
        probDiff *= 0.5
        
    result = nFact/(kFact*diffFact)
    return result*probK*probDiff


# In[ ]:




