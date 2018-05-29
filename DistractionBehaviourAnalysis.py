#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 11:18:00 2018
@author: u1490431 (kp) 

DATA EXTRACTION - DISTRACTION BEHAVIOUR PAPER PETERS ET AL. 

Information on what this script does start to finish and which other 
functions need to be run first 

(1) Reads in metafiles from filepath, contains information on filenames and basic descriptives
(2) Extracts lick data from MED files. Uses the names files in metafile and stores licking 
    data into variables by chosen day (ie. last lick day / distraction day). Stores lick data
    by group as large list of lists. Eg. last_lick_sal_M contains 16 lists of lick onsets for 
    just the last day of licking, each list is a rat, with onsets and offsets stored.
(3) Lick analysis - 
(4) Distraction analysis -  
(5) Post distractor pauses and predistractor pauses - calculates the time periods 
    for both distracted and non distracted trials separately for all groups

"""
################################################################################

# LICK ANALYSIS DPCP (1,2,3)

################################################################################

# (1) Find and extract info from the metafile(s) 
#
metafile_males = '/Volumes/KP_HARD_DRI/kp259/DPCP_ALL/DPCP12Masterfile.csv'
metafile_females = '/Volumes/KP_HARD_DRI/kp259/DPCP_ALL/DPCP3_Metafile.csv'
extract_males = MetaExtractor(metafile_males)
extract_females = MetaExtractor(metafile_females)
# Folder with all medfiles (DPCP1, DPCP2, DPCP3)
medfolder = '/Volumes/KP_HARD_DRI/kp259/DPCP_ALL/' # sometimes need space1 after DRI


# (2) - Get all lick onset/offset data for all rats/sessions (make this a function later)

''' 
  Info DPCP1(16) and DPCP2(16) males, DPCP3(24) females :
  DPCP1  DPCP2   DPCP3  - CONDITION 
  170417 171006  171124 - last lick
  170418 171007  171125 - dis
  170419 171008  171126 - hab 1
  170420 171009  171127 - hab 2
  170423 171012  171128 - amphetamine

'''
# Subsetting all data by day / drug 
# MALES ***********************************************************************
# SALINE 

last_lick_sal_M = subsetter(extract_males, ['170417','171006'], 'SAL')
distraction_sal_M = subsetter(extract_males, ['170418','171007'], 'SAL', dis=True)
hab1_sal_M = subsetter(extract_males, ['170419','171008'], 'SAL')
hab2_sal_M = subsetter(extract_males, ['170420','171009'], 'SAL')
amph_sal_M = subsetter(extract_males, ['170423','171012'], 'SAL')
# PCP
last_lick_pcp_M = subsetter(extract_males, ['170417','171006'], 'PCP')
distraction_pcp_M = subsetter(extract_males, ['170418','171007'], 'PCP', dis=True)
hab1_pcp_M = subsetter(extract_males, ['170419','171008'], 'PCP')
hab2_pcp_M = subsetter(extract_males, ['170420','171009'], 'PCP')
amph_pcp_M = subsetter(extract_males, ['170423','171012'], 'PCP')


# FEMALES **********************************************************************
# SALINE
last_lick_sal_F = subsetter(extract_females, ['171124'], 'SAL')
distraction_sal_F = subsetter(extract_females, ['171125'], 'SAL',dis=True)
hab1_sal_F = subsetter(extract_females, ['171126'], 'SAL')
hab2_sal_F = subsetter(extract_females, ['171127'], 'SAL')
amph_sal_F = subsetter(extract_females, ['171128'], 'SAL')
# PCP
last_lick_pcp_F = subsetter(extract_females, ['171124'], 'PCP')
distraction_pcp_F = subsetter(extract_females, ['171125'], 'PCP',dis=True)
hab1_pcp_F = subsetter(extract_females, ['171126'], 'PCP')
hab2_pcp_F = subsetter(extract_females, ['171127'], 'PCP')
amph_pcp_F = subsetter(extract_females, ['171128'], 'PCP')

  
# (3) Lick calc for last lick day (by group) for male PCP and SAL, for female PCP and SAL
# Licking analysis section, just last lick day 
# assign empty variables to store outputs from lick calc (to find means/groups stats)
# lists where each item is a dictionary (25) derived from lickCalc for each rat / day

lick_analysis_sal_M = lickanalysis(last_lick_sal_M)
lick_analysis_pcp_M = lickanalysis(last_lick_pcp_M)
lick_analysis_sal_F = lickanalysis(last_lick_sal_F)
lick_analysis_pcp_F = lickanalysis(last_lick_pcp_F)


# ***********************************************************************************!!!!!    
''' 
Each is a list of dictionaries, each dictionary is for a LickCalc on a single rat 

lick_analysis_sal_M = [] 
lick_analysis_pcp_M = []
lick_analysis_sal_F = []
lick_analysis_pcp_F = []

'''
## LICK DAY ANALYSIS - BY GROUP 
# Produce medians/means for individual rats and group means 
# Assign empty variables to store all data (before calc means etc.)


## Could store these as dictionary, either by defining here or within the function 
## Need to consider how to access (and if already used) later 
# Males
# Saline
sal_M_mean_n_bursts, sal_M_mean_n_runs, sal_M_mean_mean_IBI, sal_M_mean_mean_IRI,\
all_n_bursts_sal_M, all_n_runs_sal_M, all_mean_IBI_sal_M, all_mean_IRI_sal_M, \
all_mean_burst_length_sal_M, all_mean_run_length_sal_M = grouped_lickanalysis(lick_analysis_sal_M)
# PCP
pcp_M_mean_n_bursts, pcp_M_mean_n_runs, pcp_M_mean_mean_IBI, pcp_M_mean_mean_IRI,\
all_n_bursts_pcp_M, all_n_runs_pcp_M, all_mean_IBI_pcp_M, all_mean_IRI_pcp_M, \
all_mean_burst_length_pcp_M, all_mean_run_length_pcp_M = grouped_lickanalysis(lick_analysis_pcp_M)

# Females
# Saline
sal_F_mean_n_bursts, sal_F_mean_n_runs, sal_F_mean_mean_IBI, sal_F_mean_mean_IRI,\
all_n_bursts_sal_F, all_n_runs_sal_F, all_mean_IBI_sal_F, all_mean_IRI_sal_F, \
all_mean_burst_length_sal_F, all_mean_run_length_sal_F = grouped_lickanalysis(lick_analysis_sal_F)
# PCP
pcp_F_mean_n_bursts, pcp_F_mean_n_runs, pcp_F_mean_mean_IBI, pcp_F_mean_mean_IRI,\
all_n_bursts_pcp_F, all_n_runs_pcp_F, all_mean_IBI_pcp_F, all_mean_IRI_pcp_F, \
all_mean_burst_length_pcp_F, all_mean_run_length_pcp_F = grouped_lickanalysis(lick_analysis_pcp_F)

################################################################################

# DISTRACTION ANALYSIS DPCP (1,2,3)

################################################################################

# Distraction day analysis 

''' Licking data already subset earlier '''

## Add percentage distracted and other information here too 
#def Group_Distraction_Analysis(licksbygroup, lickday, distractionday):
''' Add in distraction modality calculator here to the main loop '''
whitenoise = [1, 4] # test with light differences too! 
tone = [2, 5]
combined3 = [3, 6]   
    
discalc_sal_M, discalc_pcp_M, discalc_sal_F, discalc_pcp_F = [], [], [], [] 

percent_dis_whitenoise_sal_M, percent_dis_whitenoise_pcp_M, percent_dis_whitenoise_sal_F, percent_dis_whitenoise_pcp_F = [], [], [], []   
percent_dis_tone_sal_M, percent_dis_tone_pcp_M, percent_dis_tone_sal_F, percent_dis_tone_pcp_F = [], [], [], []
percent_dis_combined_sal_M, percent_dis_combined_pcp_M, percent_dis_combined_sal_F, percent_dis_combined_pcp_F = [], [], [], []  


## SAL MALES - DISTRACTION DAY ONLY - DISTRACTOR TYPE ANALYSIS INCLUDED
# Finds distracted or not (corrects for med slipping issue)
for rat in distraction_sal_M:
    discalc = distractionCalc2(rat[0])
    distracted, notdistracted = distractedOrNot(discalc, rat[0])
  #  work out percentage and add this too 
    discalc_sal_M.append([distracted, notdistracted])

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
    
    percent_distracted_whitenoise = d_whitenoise_count / (d_whitenoise_count + nd_whitenoise_count) *100
    percent_distracted_tone = d_tone_count / (d_tone_count + nd_tone_count) *100
    percent_distracted_combined = d_combined_count / (d_combined_count + nd_combined_count) *100  
    
    percent_dis_whitenoise_sal_M.append(percent_distracted_whitenoise)
    percent_dis_tone_sal_M.append(percent_distracted_tone)
    percent_dis_combined_sal_M.append(percent_distracted_combined)
  
mean_percent_WHITENOISE_sal_M = np.mean(percent_dis_whitenoise_sal_M) # the average percentage of JUST whitenoise trials that rats are distracted on 
mean_percent_TONE_sal_M = np.mean(percent_dis_tone_sal_M)
mean_percent_COMBINED_sal_M = np.mean(percent_dis_combined_sal_M)

## PCP MALES - DISTRACTION DAY ONLY - DISTRACTOR TYPE ANALYSIS INCLUDED

for rat in distraction_pcp_M:
    discalc = distractionCalc2(rat[0])
    distracted, notdistracted = distractedOrNot(discalc, rat[0])
    discalc_pcp_M.append([distracted, notdistracted])

    dis_numeric = []
    ndis_numeric = []
    for d in distracted:
        dis_numeric.append([rat[2][idx] for idx, val in enumerate(discalc) if val == d][0])
    for nd in notdistracted:
        ndis_numeric.append([rat[2][idx] for idx, val in enumerate(discalc) if val == nd][0])   
 
    dis_numeric = [int(d) for d in dis_numeric]

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
    
    percent_distracted_whitenoise = d_whitenoise_count / (d_whitenoise_count + nd_whitenoise_count) *100
    percent_distracted_tone = d_tone_count / (d_tone_count + nd_tone_count) *100
    percent_distracted_combined = d_combined_count / (d_combined_count + nd_combined_count) *100  
    
    percent_dis_whitenoise_pcp_M.append(percent_distracted_whitenoise)
    percent_dis_tone_pcp_M.append(percent_distracted_tone)
    percent_dis_combined_pcp_M.append(percent_distracted_combined)
  
mean_percent_WHITENOISE_pcp_M = np.mean(percent_dis_whitenoise_pcp_M) 
mean_percent_TONE_pcp_M = np.mean(percent_dis_tone_pcp_M)
mean_percent_COMBINED_pcp_M = np.mean(percent_dis_combined_pcp_M)

## SAL FEMALES - DISTRACTION DAY ONLY - DISTRACTOR TYPE ANALYSIS INCLUDED
for rat in distraction_sal_F:
    discalc = distractionCalc2(rat[0])
    distracted, notdistracted = distractedOrNot(discalc, rat[0])
    discalc_sal_F.append([distracted, notdistracted])

    dis_numeric = []
    ndis_numeric = []
    for d in distracted:
        dis_numeric.append([rat[2][idx] for idx, val in enumerate(discalc) if val == d][0])
    for nd in notdistracted:
        ndis_numeric.append([rat[2][idx] for idx, val in enumerate(discalc) if val == nd][0])   
    dis_numeric = [int(d) for d in dis_numeric]
   
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
    
    percent_distracted_whitenoise = d_whitenoise_count / (d_whitenoise_count + nd_whitenoise_count) *100
    percent_distracted_tone = d_tone_count / (d_tone_count + nd_tone_count) *100
    percent_distracted_combined = d_combined_count / (d_combined_count + nd_combined_count) *100  
    
    percent_dis_whitenoise_sal_F.append(percent_distracted_whitenoise)
    percent_dis_tone_sal_F.append(percent_distracted_tone)
    percent_dis_combined_sal_F.append(percent_distracted_combined)
  
mean_percent_WHITENOISE_sal_F = np.mean(percent_dis_whitenoise_sal_F) # the average percentage of JUST whitenoise trials that rats are distracted on 
mean_percent_TONE_sal_F = np.mean(percent_dis_tone_sal_F)
mean_percent_COMBINED_sal_F = np.mean(percent_dis_combined_sal_F)

## PCP FEMALES - DISTRACTION DAY ONLY - DISTRACTOR TYPE ANALYSIS INCLUDED
for rat in distraction_pcp_F:
    discalc = distractionCalc2(rat[0])
    distracted, notdistracted = distractedOrNot(discalc, rat[0])
    discalc_pcp_F.append([distracted, notdistracted])

    dis_numeric = []
    ndis_numeric = []
    for d in distracted:
        dis_numeric.append([rat[2][idx] for idx, val in enumerate(discalc) if val == d][0])
    for nd in notdistracted:
        ndis_numeric.append([rat[2][idx] for idx, val in enumerate(discalc) if val == nd][0])   
 
    dis_numeric = [int(d) for d in dis_numeric]

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
    
    percent_distracted_whitenoise = d_whitenoise_count / (d_whitenoise_count + nd_whitenoise_count) *100
    percent_distracted_tone = d_tone_count / (d_tone_count + nd_tone_count) *100
    percent_distracted_combined = d_combined_count / (d_combined_count + nd_combined_count) *100  
    
    percent_dis_whitenoise_pcp_F.append(percent_distracted_whitenoise)
    percent_dis_tone_pcp_F.append(percent_distracted_tone)
    percent_dis_combined_pcp_F.append(percent_distracted_combined)
  
mean_percent_WHITENOISE_pcp_F = np.mean(percent_dis_whitenoise_pcp_F) 
mean_percent_TONE_pcp_F = np.mean(percent_dis_tone_pcp_F)
mean_percent_COMBINED_pcp_F = np.mean(percent_dis_combined_pcp_F) 


# Modelled distractors ˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚

mod_dis_sal_M, mod_dis_pcp_M, mod_dis_sal_F, mod_dis_pcp_F = [], [], [], []

# last_lick_sal_M, last_lick_pcp_M, last_lick_pcp_F, last_lick_sal_F  ---- variables

for rat in last_lick_sal_M:
    discalc = distractionCalc2(rat[0])
    distracted, notdistracted = distractedOrNot(discalc, rat[0])
    mod_dis_sal_M.append([distracted, notdistracted])

for rat in last_lick_pcp_M:
    discalc = distractionCalc2(rat[0])
    distracted, notdistracted = distractedOrNot(discalc, rat[0])
    mod_dis_pcp_M.append([distracted, notdistracted])
    
for rat in last_lick_sal_F:
    discalc = distractionCalc2(rat[0])
    distracted, notdistracted = distractedOrNot(discalc, rat[0])
    mod_dis_sal_F.append([distracted, notdistracted])
    
for rat in last_lick_pcp_F:
    discalc = distractionCalc2(rat[0])
    distracted, notdistracted = distractedOrNot(discalc, rat[0])
    mod_dis_pcp_F.append([distracted, notdistracted])

# Habituation days and amphetamine days SAL M ONLY ˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚
# Calculate percentage distracted later
hab1_dis_sal_M, hab2_dis_sal_M, amph_dis_sal_M = [], [], []
hab1_dis_pcp_M, hab2_dis_pcp_M, amph_dis_pcp_M = [], [], []

for rat in hab1_sal_M:
    discalc = distractionCalc2(rat[0])
    distracted, notdistracted = distractedOrNot(discalc, rat[0])
    hab1_dis_sal_M.append([distracted, notdistracted])
     
for rat in hab2_sal_M:
    discalc = distractionCalc2(rat[0])
    distracted, notdistracted = distractedOrNot(discalc, rat[0])
    hab2_dis_sal_M.append([distracted, notdistracted])
    
for rat in amph_sal_M:
    discalc = distractionCalc2(rat[0])
    distracted, notdistracted = distractedOrNot(discalc, rat[0])
    amph_dis_sal_M.append([distracted, notdistracted]) 
    
for rat in hab1_pcp_M:
    discalc = distractionCalc2(rat[0])
    distracted, notdistracted = distractedOrNot(discalc, rat[0])
    hab1_dis_pcp_M.append([distracted, notdistracted])
     
for rat in hab2_pcp_M:
    discalc = distractionCalc2(rat[0])
    distracted, notdistracted = distractedOrNot(discalc, rat[0])
    hab2_dis_pcp_M.append([distracted, notdistracted])
    
for rat in amph_pcp_M:
    discalc = distractionCalc2(rat[0])
    distracted, notdistracted = distractedOrNot(discalc, rat[0])
    amph_dis_pcp_M.append([distracted, notdistracted]) 
    
#### REPEATED FOR FEMALSE SALINE AND PCP    
hab1_dis_sal_F, hab2_dis_sal_F, amph_dis_sal_F = [], [], []
hab1_dis_pcp_F, hab2_dis_pcp_F, amph_dis_pcp_F = [], [], []

for rat in hab1_sal_F:
    discalc = distractionCalc2(rat[0])
    distracted, notdistracted = distractedOrNot(discalc, rat[0])
    hab1_dis_sal_F.append([distracted, notdistracted])
     
for rat in hab2_sal_F:
    discalc = distractionCalc2(rat[0])
    distracted, notdistracted = distractedOrNot(discalc, rat[0])
    hab2_dis_sal_F.append([distracted, notdistracted])
    
for rat in amph_sal_F:
    discalc = distractionCalc2(rat[0])
    distracted, notdistracted = distractedOrNot(discalc, rat[0])
    amph_dis_sal_F.append([distracted, notdistracted]) 
    
for rat in hab1_pcp_F:
    discalc = distractionCalc2(rat[0])
    distracted, notdistracted = distractedOrNot(discalc, rat[0])
    hab1_dis_pcp_F.append([distracted, notdistracted])
     
for rat in hab2_pcp_F:
    discalc = distractionCalc2(rat[0])
    distracted, notdistracted = distractedOrNot(discalc, rat[0])
    hab2_dis_pcp_F.append([distracted, notdistracted])

### SOMETHING WRONG HERE, LIST INDEX OUT OF RANGE (LAST RAT IN FEMALES, ISSUE?)    
for rat in amph_pcp_F:
    discalc = distractionCalc2(rat[0])
    distracted, notdistracted = distractedOrNot(discalc, rat[0])
    amph_dis_pcp_F.append([distracted, notdistracted])    
# fixed issue by adding if statement to distractionCalc2 (if len(d) is not > 1)    
# got zero distractors, consider how to deal with these situations



# POST DISTRACTION PAUSES 
# For both distracted and non-distracted trials 

###################################################################################

'''
Info: Structure of the calculated distractors lists 

discalc_sal_M[0][0][0] # [rat][list][licktimestamp]

'''

# CALCULATE THE PDP FOR SPECIFIC GROUPS - finds where in the licks the distractor 
# occurred and then finds the pause before the next lick (ignoring distractors occurring
# on the final lick in a session)

# SALINE MALES 
# Distracted PDPs  / and preDPs
pdps_dis_sal_M, pdps_notdis_sal_M = [], [] 
preDPs_dis_sal_M, preDPs_notdis_sal_M = [], [] 

med_pdps_dis_sal_M, med_pdps_notdis_sal_M = [], []


for index, rat in enumerate(discalc_sal_M):
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
    pdps_dis_sal_M.append(pdps_dis)
    med_pdps_dis_sal_M.append(np.mean(pdps_dis))
    preDPs_dis_sal_M.append(preDPs_dis)

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
    pdps_notdis_sal_M.append(pdps_notdis)
    med_pdps_notdis_sal_M.append(np.mean(pdps_notdis))
    preDPs_notdis_sal_M.append(preDPs_notdis)

# PCP MALES =============================================================================
# Cross check for number of distracted and not distracted trials in each group 
pdps_dis_pcp_M, pdps_notdis_pcp_M = [], []
preDPs_dis_pcp_M, preDPs_notdis_pcp_M = [], [] 

med_pdps_dis_pcp_M, med_pdps_notdis_pcp_M = [], []

for index, rat in enumerate(discalc_pcp_M):
    pdps_dis = []
    preDPs_dis = []
    for distractorlick in rat[0]:
        
        if distractorlick in distraction_pcp_M[index][0] and distractorlick != distraction_pcp_M[index][0][-1]:
            lick_index = distraction_pcp_M[index][0].index(distractorlick) 
            lick_index_plus1 = lick_index+1
            lick_index_minus3 = lick_index-3
            distracted_PDP = distraction_pcp_M[index][0][lick_index_plus1] - distraction_pcp_M[index][0][lick_index]
            distracted_preDP = distraction_pcp_M[index][0][lick_index] - distraction_pcp_M[index][0][lick_index_minus3]
        
        pdps_dis.append(distracted_PDP)
        preDPs_dis.append(distracted_preDP)
    pdps_dis_pcp_M.append(pdps_dis)
    med_pdps_dis_pcp_M.append(np.mean(pdps_dis))
    preDPs_dis_pcp_M.append(preDPs_dis)

# Not distracted PDPs 

for index, rat in enumerate(discalc_pcp_M):
    pdps_notdis = []
    preDPs_notdis = []
    for notdistractedlick in rat[1]:
        if notdistractedlick in distraction_pcp_M[index][0] and notdistractedlick != distraction_pcp_M[index][0][-1]:
            lick_index = distraction_pcp_M[index][0].index(notdistractedlick) 
            lick_index_plus1 = lick_index+1
            lick_index_minus3 = lick_index-3
            notdistracted_PDP = distraction_pcp_M[index][0][lick_index_plus1] - distraction_pcp_M[index][0][lick_index]
            notdistracted_preDP = distraction_pcp_M[index][0][lick_index] - distraction_pcp_M[index][0][lick_index_minus3]
        
        pdps_notdis.append(notdistracted_PDP)
        preDPs_notdis.append(notdistracted_preDP)
    pdps_notdis_pcp_M.append(pdps_notdis)
    med_pdps_notdis_pcp_M.append(np.mean(pdps_notdis))
    preDPs_notdis_pcp_M.append(preDPs_notdis)


# SALINE FEMALES

# Distracted pdps
pdps_dis_sal_F, pdps_notdis_sal_F = [], [] 
preDPs_dis_sal_F, preDPs_notdis_sal_F = [], [] 
med_pdps_dis_sal_F, med_pdps_notdis_sal_F = [], []

for index, rat in enumerate(discalc_sal_F):
    pdps_dis = []
    preDPs_dis = []
    for distractorlick in rat[0]:
        
        if distractorlick in distraction_sal_F[index][0] and distractorlick != distraction_sal_F[index][0][-1]:
            lick_index = distraction_sal_F[index][0].index(distractorlick) 
            lick_index_plus1 = lick_index+1
            lick_index_minus3 = lick_index-3
            distracted_PDP = distraction_sal_F[index][0][lick_index_plus1] - distraction_sal_F[index][0][lick_index]
            distracted_preDP = distraction_sal_F[index][0][lick_index] - distraction_sal_F[index][0][lick_index_minus3]
        
        pdps_dis.append(distracted_PDP)
        preDPs_dis.append(distracted_preDP)
    pdps_dis_sal_F.append(pdps_dis)
    med_pdps_dis_sal_F.append(np.mean(pdps_dis))
    preDPs_dis_sal_F.append(preDPs_dis)

# Not distracted PDPs 

for index, rat in enumerate(discalc_sal_F):
    pdps_notdis = []
    preDPs_notdis = []
    for notdistractedlick in rat[1]:
        if notdistractedlick in distraction_sal_F[index][0] and notdistractedlick != distraction_sal_F[index][0][-1]:
            lick_index = distraction_sal_F[index][0].index(notdistractedlick) 
            lick_index_plus1 = lick_index+1
            lick_index_minus3 = lick_index-3
            notdistracted_PDP = distraction_sal_F[index][0][lick_index_plus1] - distraction_sal_F[index][0][lick_index]
            notdistracted_preDP = distraction_sal_F[index][0][lick_index] - distraction_sal_F[index][0][lick_index_minus3]
        
        pdps_notdis.append(notdistracted_PDP)
        preDPs_notdis.append(notdistracted_preDP)
    pdps_notdis_sal_F.append(pdps_notdis)
    med_pdps_notdis_sal_F.append(np.mean(pdps_notdis))
    preDPs_notdis_sal_F.append(preDPs_notdis)

# PCP FEMALES 

pdps_dis_pcp_F, pdps_notdis_pcp_F = [], []
preDPs_dis_pcp_F, preDPs_notdis_pcp_F = [], []
med_pdps_dis_pcp_F, med_pdps_notdis_pcp_F = [], []

for index, rat in enumerate(discalc_pcp_F):
    pdps_dis = []
    preDPs_dis = []
    for distractorlick in rat[0]:
        
        if distractorlick in distraction_pcp_F[index][0] and distractorlick != distraction_pcp_F[index][0][-1]:
            lick_index = distraction_pcp_F[index][0].index(distractorlick) 
            lick_index_plus1 = lick_index+1
            lick_index_minus3 = lick_index-3
            distracted_PDP = distraction_pcp_F[index][0][lick_index_plus1] - distraction_pcp_F[index][0][lick_index]
            distracted_preDP = distraction_pcp_F[index][0][lick_index] - distraction_pcp_F[index][0][lick_index_minus3]
        
        pdps_dis.append(distracted_PDP)
        preDPs_dis.append(distracted_preDP)
    pdps_dis_pcp_F.append(pdps_dis)
    med_pdps_dis_pcp_F.append(np.mean(pdps_dis))
    preDPs_dis_pcp_F.append(preDPs_dis)

# Not distracted PDPs 

for index, rat in enumerate(discalc_pcp_F):
    pdps_notdis = []
    preDPs_notdis = []
    for notdistractedlick in rat[1]:
        if notdistractedlick in distraction_pcp_F[index][0] and notdistractedlick != distraction_pcp_F[index][0][-1]:
            lick_index = distraction_pcp_F[index][0].index(notdistractedlick) 
            lick_index_plus1 = lick_index+1
            lick_index_minus3 = lick_index-3
            notdistracted_PDP = distraction_pcp_F[index][0][lick_index_plus1] - distraction_pcp_F[index][0][lick_index]
            notdistracted_preDP = distraction_pcp_F[index][0][lick_index] - distraction_pcp_F[index][0][lick_index_minus3]
        
        pdps_notdis.append(notdistracted_PDP)
        preDPs_notdis.append(notdistracted_preDP)
    pdps_notdis_pcp_F.append(pdps_notdis)
    med_pdps_notdis_pcp_F.append(np.mean(pdps_notdis))
    preDPs_notdis_pcp_F.append(preDPs_notdis)
   
'''
# Corelations 

Find mean for each list of pre / post DPs and then correlate and plot 
using the sb.jointplot(x='Attack', y='Defense', data=df) seaborn joint plots
(find out how to get distributions too
 
sb.jointplot(x=df['nRuns'], y=df['nRuns'], kind='hex')) or type 'reg' for kernel estimation and regression

plt.plot()

How to plot different colours? If values in the plotted points 
Meet certain condition point should be blue 
Else it should be black 

OR separate them by condition first and add 2 plots, the blue and black 

for index, value in enumerate(salMdistractors):
    if value > 1 :
        add the pdp / predp to this list
        and add the predp to this list too (of the same index)
        
        else:
            add to this list
            
            Not sure if this works yet - 2 variables to compare so do i need
            both in the list or just one indices???

###################################################################################
'''

##################################################################
# Percentage distracted    ##################################################################

# SALINE and PCP for males only 

# Cross checked and correct percentage on distraction day for all sal. 
percent_dis_dis_sal_M = []
for rat in discalc_sal_M: 
    percentage = len(rat[0]) / (len(rat[0])+len(rat[1])) * 100
    percent_dis_dis_sal_M.append(percentage)

percent_dis_modelled_sal_M = []
for rat in mod_dis_sal_M: 
    percentage = len(rat[0]) / (len(rat[0])+len(rat[1])) * 100
    percent_dis_modelled_sal_M.append(percentage)
    
percent_dis_hab1_sal_M = []
for rat in hab1_dis_sal_M: 
    percentage = len(rat[0]) / (len(rat[0])+len(rat[1])) * 100
    percent_dis_hab1_sal_M.append(percentage)
    
percent_dis_hab2_sal_M = []
for rat in hab2_dis_sal_M: 
    percentage = len(rat[0]) / (len(rat[0])+len(rat[1])) * 100
    percent_dis_hab2_sal_M.append(percentage)

percent_dis_amph_sal_M = []
for rat in amph_dis_sal_M: 
    percentage = len(rat[0]) / (len(rat[0])+len(rat[1])) * 100
    percent_dis_amph_sal_M.append(percentage)



## PCP
percent_dis_dis_pcp_M = []
for rat in discalc_pcp_M: 
    percentage = len(rat[0]) / (len(rat[0])+len(rat[1])) * 100
    percent_dis_dis_pcp_M.append(percentage)

percent_dis_modelled_pcp_M = []
for rat in mod_dis_pcp_M: 
    percentage = len(rat[0]) / (len(rat[0])+len(rat[1])) * 100
    percent_dis_modelled_pcp_M.append(percentage)
    
percent_dis_hab1_pcp_M = []
for rat in hab1_dis_pcp_M: 
    percentage = len(rat[0]) / (len(rat[0])+len(rat[1])) * 100
    percent_dis_hab1_pcp_M.append(percentage)
    
percent_dis_hab2_pcp_M = []
for rat in hab2_dis_pcp_M: 
    percentage = len(rat[0]) / (len(rat[0])+len(rat[1])) * 100
    percent_dis_hab2_pcp_M.append(percentage)

percent_dis_amph_pcp_M = []
for rat in amph_dis_pcp_M: 
    percentage = len(rat[0]) / (len(rat[0])+len(rat[1])) * 100
    percent_dis_amph_pcp_M.append(percentage)



############# FEMALES - percent distracted 
## Remember might have an issue with the last PCP rat on amphetamine day
# division by zero potential problem 

# Might remove this rat from ALL days for the plots?? 

percent_dis_dis_sal_F = []
for rat in discalc_sal_F: 
    percentage = len(rat[0]) / (len(rat[0])+len(rat[1])) * 100
    percent_dis_dis_sal_F.append(percentage)

percent_dis_modelled_sal_F = []
for rat in mod_dis_sal_F: 
    percentage = len(rat[0]) / (len(rat[0])+len(rat[1])) * 100
    percent_dis_modelled_sal_F.append(percentage)
    
percent_dis_hab1_sal_F = []
for rat in hab1_dis_sal_F: 
    percentage = len(rat[0]) / (len(rat[0])+len(rat[1])) * 100
    percent_dis_hab1_sal_F.append(percentage)
    
percent_dis_hab2_sal_F = []
for rat in hab2_dis_sal_F: 
    percentage = len(rat[0]) / (len(rat[0])+len(rat[1])) * 100
    percent_dis_hab2_sal_F.append(percentage)

percent_dis_amph_sal_F = []
for rat in amph_dis_sal_F: 
    percentage = len(rat[0]) / (len(rat[0])+len(rat[1])) * 100
    percent_dis_amph_sal_F.append(percentage)



## PCP
percent_dis_dis_pcp_F = []
for rat in discalc_pcp_F[:-1]:  ## Exclude last rat, zero distracted and zero not dis 
    percentage = len(rat[0]) / (len(rat[0])+len(rat[1])) * 100
    percent_dis_dis_pcp_F.append(percentage)

percent_dis_modelled_pcp_F = []
for rat in mod_dis_pcp_F[:-1]: 
    percentage = len(rat[0]) / (len(rat[0])+len(rat[1])) * 100
    percent_dis_modelled_pcp_F.append(percentage)
    
percent_dis_hab1_pcp_F = []
for rat in hab1_dis_pcp_F[:-1]: 
    percentage = len(rat[0]) / (len(rat[0])+len(rat[1])) * 100
    percent_dis_hab1_pcp_F.append(percentage)
    
percent_dis_hab2_pcp_F = []
for rat in hab2_dis_pcp_F[:-1]: 
    percentage = len(rat[0]) / (len(rat[0])+len(rat[1])) * 100
    percent_dis_hab2_pcp_F.append(percentage)


percent_dis_amph_pcp_F = []
for rat in amph_dis_pcp_F[:-1]: 
    percentage = len(rat[0]) / (len(rat[0])+len(rat[1])) * 100
    percent_dis_amph_pcp_F.append(percentage)
    
    
    
######################### INDIVIDUAL DIFFERENCES #######################

# Flatten lists and plot EVERYTHING (check you haven't removed anything)

# Can pre-distraction pause predict chances of distracted or not?
    # Logistic regression 
    
# Do numbers of runs/bursts predict distractedness?


#GROUP DATA (ways to subset)
#
#MALES 
#PCP lick day mean PDP, mean percentage distracted, mean/median bursts
#PCP distraction day mean PDP, mean percentage distracted, mean/median bursts
#PCP habituation day mean PDP, mean percentage distracted, mean/median bursts
#PCP salineIP day mean PDP, mean percentage distracted, mean/median bursts
#PCP amphetamineIP day mean PDP, mean percentage distracted, mean/median bursts
#
#SAL lick day mean PDP, mean percentage distracted, mean/median bursts
#SAL distraction day mean PDP, mean percentage distracted, mean/median bursts
#SAL habituation day mean PDP, mean percentage distracted, mean/median bursts
#SAL salineIP day mean PDP, mean percentage distracted, mean/median bursts
#SAL amphetamineIP day mean PDP, mean percentage distracted, mean/median bursts
#
#FEMALES 
#PCP lick day mean PDP, mean percentage distracted, mean/median bursts
#PCP distraction day mean PDP, mean percentage distracted, mean/median bursts
#PCP habituation day mean PDP, mean percentage distracted, mean/median bursts
#PCP salineIP day mean PDP, mean percentage distracted, mean/median bursts
#PCP amphetamineIP day mean PDP, mean percentage distracted, mean/median bursts
#
#SAL lick day mean PDP, mean percentage distracted, mean/median bursts
#SAL distraction day mean PDP, mean percentage distracted, mean/median bursts
#SAL habituation day mean PDP, mean percentage distracted, mean/median bursts
#SAL salineIP day mean PDP, mean percentage distracted, mean/median bursts
#SAL amphetamineIP day mean PDP, mean percentage distracted, mean/median bursts


#sb.jointplot(x=df['nRuns'], y=df['nBursts'], kind='hex')) #or type 'reg' for kernel estimation and regression
