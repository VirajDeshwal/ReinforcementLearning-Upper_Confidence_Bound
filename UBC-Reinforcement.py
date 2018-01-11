#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 23:03:28 2018

@author: virajdeshwal
"""

#Upper_Confidence_Bound

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

file = pd.read_csv('Ads_CTR_Optimisation.csv')
'''We are dealing with the different version of the same advertisement for the user'''
'''We have to find the CTR(Click through Rate )for the user. We have the clicks from 10000 users
and based on the clicks from 100k users we will choose which ads to show to the user.
'''

'''There is no library to implement Upper Confidence Bound Algo.
We have to write it from scratch. Let's do it ;) '''

#implementing the UPPER CONFIDENCE BOUND
#Number of the users
N=10000
d=10
ads_selected = []
#defind the two variables 
numbers_of_selections = [0]*d
total_reward = 0
sum_of_rewards = [0]*d

#we will loop all the selctions of the users 

for n in range(0,N):
    ad = 0
    max_upper_bound =0
    #We need to compute of each version of the ads (the average reward and the confidence  interval)
    for i in range(0,d):
        if (numbers_of_selections [i]>0):
            avg_rewards =sum_of_rewards[i]/numbers_of_selections[i]
            delta_i = math.sqrt(3/2* math.log (n + 1)/numbers_of_selections[i])
            upper_bound =avg_rewards + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            max_upper_bound=upper_bound
            ad =i
        ads_selected.append(ad)
        numbers_of_selections[ad]=numbers_of_selections[ad] +1
        reward=file.values[n,ad]
        sum_of_rewards[ad]= sum_of_rewards[ad] + reward
        total_reward = total_reward +reward
        
        
#Now time for visualize the results
plt.hist(ads_selected)
plt.title('Histogram of Ads Selected')
plt.xlabel('Ads')
plt.ylabel('Number of time Ad was selected')
plt.show()

print('\n\n Done ;)')

        
    
