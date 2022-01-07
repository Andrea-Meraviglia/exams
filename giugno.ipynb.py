# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Programming in Python
# ## Exam: June 21, 2021
#
#
# You can solve the exercises below by using standard Python 3.9 libraries, NumPy, Matplotlib, Pandas, PyMC3.
# You can browse the documentation: [Python](https://docs.python.org/3.9/), [NumPy](https://numpy.org/doc/stable/user/index.html), [Matplotlib](https://matplotlib.org/stable/contents.html), [Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html), [PyMC3](https://docs.pymc.io/).
# You can also look at the [slides of the course](https://homes.di.unimi.it/monga/lucidi2021/pyqb00.pdf) or your code on [GitHub](https://github.com).
#
# **It is forbidden to communicate with others.** 
#

import numpy as np              # type: ignore
import matplotlib.pyplot as plt # type: ignore
# %matplotlib inline

import pandas as pd     

# ### Exercise 1 (max 2 points)
#
# A recent exploration of Venus has discovered a new organism, now known as *Sarchiapus Examinis*. The data collected about *Sarchiapi E.* individuals are available in the file `data.csv`. For each individual the DNA, an age in days, and a length in centimeters were recorded. 
#
# Read the data in a Pandas DataFrame.
#

# +
    
dna = pd.read_csv('data.csv') #import
# -

dna


# ### Exercise 2 (max 3 points)
#
# Plot the distribution of length.

#plot
fig,ax=plt.subplots()
_=ax.hist(dna['length'], label='Young', density=True, bins='auto')
_=ax.set_title('Length distribution')
_=ax.set_xlabel('lenght')
_=ax.set_ylabel('counts')
_=ax.grid()

fig, ax = plt.subplots()
_=ax.hist(dna['length'], density=True, label='Length', bins='auto')
_=ax.set_xlabel('Lenght')
_=ax.set_ylabel('counts')
_=ax.set_title('Lenght distribution')
_=ax.grid()

# ### Exercise 3 (max 5 points)
#
# Collect in a new Pandas DataFrame the mean and standard deviation of length for each age.

#insert in a new data frame 
group=dna.groupby(['age'])
group['length'].agg(['mean','std'])


group=dna.groupby(['age'])
group['length'].agg(['mean','std','max'])






# ### Exercise 4 (max 5 points)
#
# The gender of a *Sarchiapus E.* individual is defined by the first letter of its DNA: an `'A'` or a `'C'` is considered a male, otherwise is considered a female. Add a column to the data with the gender.

#male or female
def gender(dna)-> str:
    if (dna['dna'][0] == 'A')| (dna['dna'][0] == 'C'):
        gender = 'male'
    else:
        gender = 'female'
    return gender



#chiamare funzione in nuova colonna 
dna['gender']=dna.apply(gender,axis=1)
dna



# ### Exercise 5 (max 3 points)
#
# Plot the distribution of length for male *Sarchiapi E.*.
#

fig,ax=plt.subplots()
length_m = dna.loc[dna['gender'] =='male']['length']
_=ax.hist(length_m)
_=ax.set_title('distribution of length')
_=ax.set_xlabel('lenght')
_=ax.grid()

# ### Exercise 6 (max 7 points)
#
#
# Define a function `count_twins` that takes a string and a character and returns how many times the substring composed by the character repeated twice can be found in the whole string. For example, if the string is `'ZXXZXXXZCCCX'`, and the character `'X'`, the result should be 3.
#
# To get the full marks, you should declare correctly the type hints (the *signature* of the function) and add a doctest string. 

stringa='ZaXXZXXXZCCCX'
print(stringa[2:4])
carattere='X'


def count_twins(stringa:str,carattere:str)->int:
    count=0
    for i in range(0,len(stringa)-1):
        if(stringa[i] == stringa[i+1] == carattere):
            count=count+1
    return count


count_twins(stringa,carattere)

# ### Exercise 7 (max 5 points)
#
# Using the function defined in Exercise 5, add a column `a_twins` with the number of `'A'` twins in the DNA of each *Sarchiapus E.*.

#colonna=nomedata.apply( lambda comedata: funzione(), axis)
dna['a_twins']=dna.apply( lambda dna: count_twins(dna['dna'],'A'),axis=1)
dna

# ### Exercise 8 (max 3 points)
#
# Consider the hypothesis that the length of each *Sarchiapus E.* is normally distributed with a mean equal to the number of `'A'` twins in its DNA and a standard deviation that you assume to be uniformed distributed between 0 and 10. Code this statistical hypothesis as a PyMC3 model and plot the distribution of the standard deviation after having seen the collected data.

import pymc3 as pm 

# +
length_pm= pm.Model() 

with length_pm:
    
    mu=dna['a_twins']  #richiamo variabile, inizio, fine
    sigma=pm.Uniform('sigma',0,10)
    
    o = pm.Normal('length',mu, sigma, observed=dna['length']) 
    
# -

with length_pm:
    posterior= pm.sample(2000, return_inferencedata=False)

posterior[1]


fig, ax =plt.subplots()
_=ax.hist(posterior['sigma'],bins='auto',density=True, color='c', ec='k')
_=ax.set_title('posterior lenght')
_=ax.grid()


