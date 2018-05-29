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
    
# Modelled distractors by group (last lick day)    
mod_dis_sal_M = disbygroup(last_lick_sal_M)
mod_dis_pcp_M = disbygroup(last_lick_pcp_M)
mod_dis_sal_F = disbygroup(last_lick_sal_F)
mod_dis_pcp_F = disbygroup(last_lick_pcp_F)
    
# Habituation days by group 
hab1_dis_sal_M = disbygroup(hab1_sal_M)
hab2_dis_sal_M = disbygroup(hab2_sal_M)

hab1_dis_pcp_M = disbygroup(hab1_pcp_M)
hab2_dis_pcp_M = disbygroup(hab2_pcp_M)

hab1_dis_sal_F = disbygroup(hab1_sal_F)
hab2_dis_sal_F = disbygroup(hab2_sal_F)

hab1_dis_pcp_F = disbygroup(hab1_pcp_F)
hab2_dis_pcp_F = disbygroup(hab2_pcp_F)

# Amphetamine days by group 
amph_dis_sal_M = disbygroup(amph_sal_M)
amph_dis_pcp_M = disbygroup(amph_pcp_M)

amph_dis_sal_F = disbygroup(amph_sal_F)
amph_dis_pcp_F = disbygroup(amph_pcp_F)

#def percentdisbygroup(dictionary):    