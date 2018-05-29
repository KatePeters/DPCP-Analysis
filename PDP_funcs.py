#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 09:48:33 2018

@author: u1490431
"""


def pdpbygroup(distractiondict, groupdict):
    ''' Distraction dict = discalc for the chosen group 
        groupdict is the whole disctionary on distraction 
        day from subsetter
    
    '''
    
    pdps_dis_group, med_pdps_dis_group, preDPs_dis_group, \
    pdps_notdis_group, med_pdps_notdis_group, preDPs_notdis_group = [],[],[],[],[],[]
    
    for index, rat in enumerate(distractiondict):
        pdps_dis = []
        preDPs_dis = []
        for distractorlick in rat[0]:
            
            if distractorlick in groupdict[index][0] and distractorlick != groupdict[index][0][-1]:
                lick_index = groupdict[index][0].index(distractorlick) 
                lick_index_plus1 = lick_index+1
                lick_index_minus3 = lick_index-3
                distracted_PDP = groupdict[index][0][lick_index_plus1] - groupdict[index][0][lick_index]
                distracted_preDP = groupdict[index][0][lick_index] - groupdict[index][0][lick_index_minus3]
            
            pdps_dis.append(distracted_PDP)
            preDPs_dis.append(distracted_preDP)
        pdps_dis_group.append(pdps_dis)
        med_pdps_dis_group.append(np.mean(pdps_dis))
        preDPs_dis_group.append(preDPs_dis)
    
    
    # Not distracted PDPs 
    
    for index, rat in enumerate(distractiondict):
        pdps_notdis = []
        preDPs_notdis = []
        for notdistractedlick in rat[1]:
            if notdistractedlick in groupdict[index][0] and notdistractedlick != groupdict[index][0][-1]:
                lick_index = groupdict[index][0].index(notdistractedlick) 
                lick_index_plus1 = lick_index+1
                lick_index_minus3 = lick_index-3
                notdistracted_PDP = groupdict[index][0][lick_index_plus1] - groupdict[index][0][lick_index]
                notdistracted_preDP = groupdict[index][0][lick_index] - groupdict[index][0][lick_index_minus3]
            
            pdps_notdis.append(notdistracted_PDP)
            preDPs_notdis.append(notdistracted_preDP)
        pdps_notdis_group.append(pdps_notdis)
        med_pdps_notdis_group.append(np.mean(pdps_notdis))
        preDPs_notdis_group.append(preDPs_notdis)
    
    return pdps_dis_group, med_pdps_dis_group, preDPs_dis_group, \
        pdps_notdis_group, med_pdps_notdis_group, preDPs_notdis_group
        
        
pdps_dis_sal_M, med_pdps_dis_sal_M, preDPs_dis_sal_M,\
pdps_notdis_sal_M, med_pdps_notdis_sal_M, preDPs_notdis_sal_M,\
 = pdpbygroup(discalc_sal_M, distraction_sal_M) 

pdps_dis_pcp_M, med_pdps_dis_pcp_M, preDPs_dis_pcp_M,\
pdps_notdis_pcp_M, med_pdps_notdis_pcp_M, preDPs_notdis_pcp_M,\
 = pdpbygroup(discalc_pcp_M, distraction_pcp_M) 

pdps_dis_sal_F, med_pdps_dis_sal_F, preDPs_dis_sal_F,\
pdps_notdis_sal_F, med_pdps_notdis_sal_F, preDPs_notdis_sal_F,\
 = pdpbygroup(discalc_sal_F, distraction_sal_F) 
 
pdps_dis_pcp_F, med_pdps_dis_pcp_F, preDPs_dis_pcp_F,\
pdps_notdis_pcp_F, med_pdps_notdis_pcp_F, preDPs_notdis_pcp_F,\
 = pdpbygroup(discalc_pcp_F, distraction_pcp_F) 


       