#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 09:23:00 2018

@author: u1490431
"""





def disbygroup(dictionary):
    dis = []
    for rat in dictionary:
        
        discalc = distractionCalc2(rat[0])         
        distracted, notdistracted = distractedOrNot(discalc, rat[0])
        dis.append([distracted, notdistracted])
        
    return dis
    


#def percentdisbygroup(dictionary):    
    

#def pdpbygroup():

    