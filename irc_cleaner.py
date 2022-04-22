#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 17:24:23 2022

@author: lenox
"""
   
"""
This script will apply the functions
from irc_parse.py to the real dataset
and produce a clean dataframe that is 
suitable for analysis in a Jupyter Notebook.
"""
#%% imports

import pandas as pd
import irc_parse

#%% read in data

raw_log = []
with open('hackers.log', 'r', errors='ignore') as log_file:
    raw_log = log_file.readlines()

#%% create dataframe

hackers = pd.DataFrame(raw_log, columns=['original_data'])


#%% use the is_date_row function to
# check if a row is actually a date.

hackers['is_date_row'] = hackers['original_data'].apply(irc_parse.is_date_row)

#%%apply the is_messgae function 

hackers['is_message'] = hackers['original_data'].apply(irc_parse.is_message)

#%% save data to cleaner

hackers.to_csv('hackers_clean.csv')

#%% (1.1) Which users posted the most messages (2pts)?



#%% (1.2) Which users logged in the greatest number of times? (2pts)


#%% (1.3) Which users spent the most time in the chat? (3pts)


#%% (1.4) Who are the administrators (username begins with @) (1pt).


#%% (2.1) Count the total number of written messages (only those with actual text content) (1 pts).

len(hackers.loc[hackers['is_message']==True])
print(len(hackers.loc[hackers['is_message']==True]))

#%% (2.2) Find the most common words (only include message content) (2 pts)


#%% (2.3) Find and rank (by count) words not in an English dictionary (2 pts). 
          #This is a simple method that can identify some names of malware tools.


#%% (2.4) How many distinct URLs were posted in the chat? (1 pt)


#%% (2.5) Which URLs were posted the most (top 5)? (1 pt)


#%% (2.6) Which domains (e.g. github.com/ or youtube.com) were shared the most.


#%% (2.7) Generate a list of sites on the Dark Web (sites ending in .onion) (1pt)


#%% (3.1) Which hours of the day had the most messages (1 pt)?


#%% (3.2) Which days had the most messages (top 10 days) (2pts)?


#%% (3.3) Rank the days of the week by average message count (1pt).


