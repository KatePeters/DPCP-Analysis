#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 07:39:25 2018

@author: u1490431
"""

modalitykey = {'whitenoise':[1,4], 'tone':[2,5], 'combined3':[3,6]}

#modalitykey as a dictionary 

def discalc_modalities(dictionary, modalitykey, ):
    percent_dis_whitenoise_group = []
    percent_dis_tone_group = []
    percent_dis_combined_group = []
    discalcgroup = []
    ## SAL MALES - DISTRACTION DAY ONLY - DISTRACTOR TYPE ANALYSIS INCLUDED
# Finds distracted or not (corrects for med slipping issue)
    for rat in dictionary:
        
        discalc = distractionCalc2(rat[0])
        distracted, notdistracted = distractedOrNot(discalc, rat[0])
      #  work out percentage and add this too 
        discalcgroup.append([distracted, notdistracted])
    
        dis_numeric = []
        ndis_numeric = []
    # Modality analysis - calculates which distractors contain different features (whitenoise, tone or combination)
    # Then works out on how many of these trials rats are distracted (individual) before creating a mean 
        for d in distracted:
            dis_numeric.append([rat[2][idx] for idx, val in enumerate(discalc) if val == d][0])
        for nd in notdistracted:
            ndis_numeric.append([rat[2][idx] for idx, val in enumerate(discalc) if val == nd][0])   
        # Makes the distracted trial types into integers 
        dis_numeric = [int(d) for d in dis_numeric]
        # Counts to work out percentages after finding how many are each modality 
        d_whitenoise_count = 0
        d_tone_count = 0
        d_combined_count = 0 
        
        dis_type_text = [] #labels the distypes with text labels and adds to the counts
        for d in dis_numeric:
            if d in modalitykey['whitenoise']:
                dis_type_text.append('whitenoise')
                d_whitenoise_count += 1
            elif d in modalitykey['tone']:
                dis_type_text.append('tone')
                d_tone_count += 1
            elif d in modalitykey['combined3']:
                dis_type_text.append('combined3')
                d_combined_count += 1 
        d_percent_white_noise = d_whitenoise_count / (len(dis_type_text))*100
        d_percent_tone = d_tone_count / (len(dis_type_text))*100
        d_percent_combined = d_combined_count / (len(dis_type_text))*100  
    
        # Non-distracted trials by modality 
        ndis_numeric = [int(d) for d in ndis_numeric]
        nd_whitenoise_count = 0
        nd_tone_count = 0
        nd_combined_count = 0 
        
        ndis_type_text = []
        for d in ndis_numeric:
            if d in modalitykey['whitenoise']:
                ndis_type_text.append('whitenoise')
                nd_whitenoise_count += 1
            elif d in modalitykey['tone']:
                ndis_type_text.append('tone')
                nd_tone_count += 1
            elif d in modalitykey['combined3']:
                ndis_type_text.append('combined3')
                nd_combined_count += 1 
                
    
        nd_percent_white_noise = nd_whitenoise_count / (len(ndis_type_text))*100
        nd_percent_tone = nd_tone_count / (len(ndis_type_text))*100
        nd_percent_combined =  nd_combined_count / (len(ndis_type_text))*100
        
        percent_distracted_whitenoise = d_whitenoise_count / (d_whitenoise_count + nd_whitenoise_count) *100
        percent_distracted_tone = d_tone_count / (d_tone_count + nd_tone_count) *100
        percent_distracted_combined = d_combined_count / (d_combined_count + nd_combined_count) *100  
        
        percent_dis_whitenoise_group.append(percent_distracted_whitenoise)
        percent_dis_tone_group.append(percent_distracted_tone)
        percent_dis_combined_group.append(percent_distracted_combined)
      
    mean_percent_WHITENOISE = np.mean(percent_dis_whitenoise_group) # the average percentage of JUST whitenoise trials that rats are distracted on 
    mean_percent_TONE = np.mean(percent_dis_tone_group)
    mean_percent_COMBINED = np.mean(percent_dis_combined_group)
    
    
    return discalcgroup, percent_dis_whitenoise_group, percent_dis_tone_group, \
            percent_dis_combined_group, mean_percent_WHITENOISE, mean_percent_TONE, \
            mean_percent_COMBINED













