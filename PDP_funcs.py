#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 09:48:33 2018

@author: u1490431
"""

# SALINE MALES 
# Distracted PDPs  / and preDPs
pdps_dis_sal_M, pdps_notdis_sal_M = [], [] 
preDPs_dis_sal_M, preDPs_notdis_sal_M = [], [] 
med_pdps_dis_sal_M, med_pdps_notdis_sal_M = [], []

def pdpbygroup(distractiondict, groupdict):
''' Distraction dict = discalc for the chosen group 
    groupdict is the whole disctionary on distraction 
    day from subsetter

'''
    
    pdps_dis_group, med_pdps_dis_group, preDPs_dis_group, \
    pdps_notdis_group, med_pdps_notdis_group, preDPs_notdis_group = [],[],[],[],[],[]
    
    for index, rat in enumerate(dictionary):
        pdps_dis = []
        preDPs_dis = []
        for distractorlick in rat[0]:
            
            if distractorlick in distraction_sal_M[index][0] and distractorlick != distraction_sal_M[index][0][-1]:
                lick_index = distraction_sal_M[index][0].index(distractorlick) 
                lick_index_plus1 = lick_index+1
                lick_index_minus3 = lick_index-3
                distracted_PDP = distraction_sal_M[index][0][lick_index_plus1] - distraction_sal_M[index][0][lick_index]
                distracted_preDP = distraction_sal_M[index][0][lick_index] - distraction_sal_M[index][0][lick_index_minus3]
            
            pdps_dis.append(distracted_PDP)
            preDPs_dis.append(distracted_preDP)
        pdps_dis_group.append(pdps_dis)
        med_pdps_dis_group.append(np.mean(pdps_dis))
        preDPs_dis_group.append(preDPs_dis)
    
    
    # Not distracted PDPs 
    
    for index, rat in enumerate(discalc_sal_M):
        pdps_notdis = []
        preDPs_notdis = []
        for notdistractedlick in rat[1]:
            if notdistractedlick in distraction_sal_M[index][0] and notdistractedlick != distraction_sal_M[index][0][-1]:
                lick_index = distraction_sal_M[index][0].index(notdistractedlick) 
                lick_index_plus1 = lick_index+1
                lick_index_minus3 = lick_index-3
                notdistracted_PDP = distraction_sal_M[index][0][lick_index_plus1] - distraction_sal_M[index][0][lick_index]
                notdistracted_preDP = distraction_sal_M[index][0][lick_index] - distraction_sal_M[index][0][lick_index_minus3]
            
            pdps_notdis.append(notdistracted_PDP)
            preDPs_notdis.append(notdistracted_preDP)
        pdps_notdis_group.append(pdps_notdis)
        med_pdps_notdis__group.append(np.mean(pdps_notdis))
        preDPs_notdis__group.append(preDPs_notdis)
    
    return pdps_dis_group, med_pdps_dis_group, preDPs_dis_group, \
        pdps_notdis_group, med_pdps_notdis_group, preDPs_notdis_group