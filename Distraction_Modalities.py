#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 19:16:10 2018

@author: u1490431
"""

''' MODALITY ANALYSIS - DISTRACTORS ''' 

import matplotlib.pyplot as plt

filename = '!2017-04-18_08h50m.Subject dpcp1.7'
path = medfolder + filename # add in the actual path here, and edit to fit in the for loops
                            # of the main programme 
#allvars = medfilereader(path, remove_var_header = True)


med_dis_times, dis_type = medfilereader(path, varsToExtract = ['i','j'], remove_var_header = True)
onsets, offsets = medfilereader(path, ['e', 'f'], remove_var_header = True)
discalc = distractionCalc2(onsets)

distracted, notdistracted = distractedOrNot(discalc, onsets)
distracted_bool2 = np.in1d(discalc, distracted) # Maybe don't actually need this 

whitenoise = [1, 4] # test with light differences too! 
tone = [2, 5]
combined3 = [3, 6]


dis_numeric = []
for d in distracted:
    dis_numeric.append([dis_type[idx] for idx, val in enumerate(discalc) if val == d][0])

ndis_numeric = []
for n in notdistracted:
    ndis_numeric.append([dis_type[idx] for idx, val in enumerate(discalc) if val == n][0])
    
# Distracted trials by modality
dis_numeric = [int(d) for d in dis_numeric]

# Counts to work out percentages after finding how many are each modality 
d_whitenoise_count = 0
d_tone_count = 0
d_combined_count = 0 

dis_type_text = []
for d in dis_numeric:
    if d in whitenoise:
        dis_type_text.append('whitenoise')
        d_whitenoise_count += 1
    elif d in tone:
        dis_type_text.append('tone')
        d_tone_count += 1
    elif d in combined3:
        dis_type_text.append('combined3')
        d_combined_count += 1 


d_percent_white_noise = d_whitenoise_count / (len(dis_type_text))*100
d_percent_tone = d_tone_count / (len(dis_type_text))*100
d_percent_combined = d_combined_count / (len(dis_type_text))*100  

# Sanity check = 100% 
#totSane = d_percent_white_noise + d_percent_tone + d_percent_combined       

# Non-distracted trials by modality 
ndis_numeric = [int(d) for d in ndis_numeric]

nd_whitenoise_count = 0
nd_tone_count = 0
nd_combined_count = 0 

ndis_type_text = []
for d in ndis_numeric:
    if d in whitenoise:
        ndis_type_text.append('whitenoise')
        nd_whitenoise_count += 1
    elif d in tone:
        ndis_type_text.append('tone')
        nd_tone_count += 1
    elif d in combined3:
        ndis_type_text.append('combined3')
        nd_combined_count += 1 
        
nd_percent_white_noise = nd_whitenoise_count / (len(ndis_type_text))*100
nd_percent_tone = nd_tone_count / (len(ndis_type_text))*100
nd_percent_combined =  nd_combined_count / (len(ndis_type_text))*100

# totSane = nd_percent_white_noise + nd_percent_tone + nd_percent_combined 


percent_distracted_whitenoise = d_whitenoise_count / (d_whitenoise_count + nd_whitenoise_count) *100
percent_distracted_tone = d_tone_count / (d_tone_count + nd_tone_count) *100
percent_distracted_combined = d_combined_count / (d_combined_count + nd_combined_count) *100



'''
#!#! Remember that there is duplicates here! LIghts and tones/noise always together 

houselight = [1, 2]
cuelight = [4, 5]
combined3 = [3, 6]

# Counts to work out percentages after finding how many are each modality 
d_house_count = 0
d_cue_count = 0
d_combined_count = 0  # repeated 

dis_type_text_Light = [] # to make distinct from those separated by sounds 
for d in dis_numeric:
    if d in houselight:
        dis_type_text_Light.append('whitenoise')
        d_house_count += 1
    elif d in cuelight:
        dis_type_text_Light.append('tone')
        d_cue_count += 1
    elif d in combined3:
        dis_type_text_Light.append('combined3')
        d_combined_count += 1 # exactly the same 


d_percent_house = d_house_count / (len(dis_type_text_Light))*100
d_percent_cue = d_cue_count / (len(dis_type_text_Light))*100
d_percent_combined = d_combined_count / (len(dis_type_text_Light))*100 


# Non-distracted trials by modality 
ndis_numeric = [int(d) for d in ndis_numeric]

nd_house_count = 0
nd_cue_count = 0
nd_combined_count = 0 

ndis_type_text_Light = []
for d in ndis_numeric:
    if d in houselight:
        ndis_type_text_Light.append('whitenoise')
        nd_house_count += 1
    elif d in cuelight:
        ndis_type_text_Light.append('tone')
        nd_cue_count += 1
    elif d in combined3:
        ndis_type_text_Light.append('combined3')
        nd_combined_count += 1 
        
nd_percent_house = nd_house_count / (len(ndis_type_text_Light))*100
nd_percent_cue = nd_cue_count / (len(ndis_type_text_Light))*100
nd_percent_combined =  nd_combined_count / (len(ndis_type_text_Light))*100 # same 

#totSane = nd_percent_white_noise + nd_percent_tone + nd_percent_combined 


percent_distracted_houselight = d_house_count / (d_house_count + nd_house_count) *100
percent_distracted_cue = d_cue_count / (d_cue_count + nd_cue_count) *100
percent_distracted_combined = d_combined_count / (d_combined_count + nd_combined_count) *100

'''

### Looks like combined and white noise are the most distracting in this file for this rat 

# Will run all rats with the sounds as distinct (if no difference re-run with lights - just
    #have to change the keys not the whole loops again)










'''
# Distraction code from medPC04 - check this is the same as the code used in all DPCP 

1 = white noise + house light # 3
4 = white noise + cue light # 5 
2 = tone + house light # 4
5 = tone + cue light # 6 

3 = white noise + tone + house light # probably the most salient 1
6 = white noise + tone + light cue # 2

# Could separate by (1) White noise vs tone vs massive combined 
1 and 4 - whitenoise
2 and 5 - tone
3 and 6 - combined 
# Or by (2) House light vs cue light vs massive combined 
1 and 2 - houselight
4 and 5 - cuelight
3 and 6 - combined 

# Do both ( 3 groups ) by sounds different and light different as no just sound or just light 
'''