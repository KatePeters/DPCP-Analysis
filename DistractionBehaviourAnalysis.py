#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 11:18:00 2018

@author: u1490431 (kp) 
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
# MALES ***********************************************************************
# SALINE 
# assign empty list to add lists of lick onsets and offsets for all medfiles 
last_lick_sal_M, distraction_sal_M, hab1_sal_M, hab2_sal_M, amph_sal_M = [], [], [], [], []
# PCP
last_lick_pcp_M, distraction_pcp_M, hab1_pcp_M, hab2_pcp_M, amph_pcp_M = [], [], [], [], []       


# Read in MED files, extract lick onsets and offsets 
for ind, filename in enumerate(extract_males['MedFilenames']):
    path = medfolder + filename
    onsets, offsets = medfilereader(path, ['e', 'f'], remove_var_header = True)  # e onset, f offset
    med_dis_times, dis_type = medfilereader(path, ['i','j'], remove_var_header = True) # j distractor types
# Subsetting all lick data by group (use dates to index) rat ID is saved in the list
#SALINE

# Write this as a function, that takes a list of dates, conditions etc. 
# Saline last licks day    
    if extract_males['Date'][ind] == '170417' and extract_males['Drug'][ind] == 'SAL' \
    or extract_males['Date'][ind] == '171006' and extract_males['Drug'][ind] == 'SAL' :
        # Produces list of lists with 3 inner lists (onset, offset, rat ID)
        last_lick_sal_M.append([onsets, offsets, extract_males['RatID'][ind]])
# Saline distraction        
    if extract_males['Date'][ind] == '170418' and extract_males['Drug'][ind] == 'SAL' \
    or extract_males['Date'][ind] == '171007' and extract_males['Drug'][ind] == 'SAL' :
        distraction_sal_M.append([onsets, offsets, dis_type, extract_males['RatID'][ind]])
# Saline habituation 1
    if extract_males['Date'][ind] == '170419' and extract_males['Drug'][ind] == 'SAL' \
    or extract_males['Date'][ind] == '171008' and extract_males['Drug'][ind] == 'SAL' :
        hab1_sal_M.append([onsets, offsets, extract_males['RatID'][ind]])
# Saline habituation 2
    if extract_males['Date'][ind] == '170420' and extract_males['Drug'][ind] == 'SAL' \
    or extract_males['Date'][ind] == '171009' and extract_males['Drug'][ind] == 'SAL' :
        hab2_sal_M.append([onsets, offsets, extract_males['RatID'][ind]])
# Saline amphetamine IP             
    if extract_males['Date'][ind] == '170423' and extract_males['Drug'][ind] == 'SAL' \
    or extract_males['Date'][ind] == '171012' and extract_males['Drug'][ind] == 'SAL' :
        amph_sal_M.append([onsets, offsets, extract_males['RatID'][ind]])
            
# PCP 
# PCP last licks day    
    if extract_males['Date'][ind] == '170417' and extract_males['Drug'][ind] == 'PCP' \
    or extract_males['Date'][ind] == '171006' and extract_males['Drug'][ind] == 'PCP' :
        last_lick_pcp_M.append([onsets, offsets, extract_males['RatID'][ind]])
# PCP distraction        
    if extract_males['Date'][ind] == '170418' and extract_males['Drug'][ind] == 'PCP' \
    or extract_males['Date'][ind] == '171007' and extract_males['Drug'][ind] == 'PCP' :
        distraction_pcp_M.append([onsets, offsets, dis_type, extract_males['RatID'][ind]])
# PCP habituation 1
    if extract_males['Date'][ind] == '170419' and extract_males['Drug'][ind] == 'PCP' \
    or extract_males['Date'][ind] == '171008' and extract_males['Drug'][ind] == 'PCP' :
        hab1_pcp_M.append([onsets, offsets, extract_males['RatID'][ind]])
# PCP habituation 2
    if extract_males['Date'][ind] == '170420' and extract_males['Drug'][ind] == 'PCP' \
    or extract_males['Date'][ind] == '171009' and extract_males['Drug'][ind] == 'PCP' :
        hab2_pcp_M.append([onsets, offsets, extract_males['RatID'][ind]])
# PCP amphetamine IP             
    if extract_males['Date'][ind] == '170423' and extract_males['Drug'][ind] == 'PCP' \
    or extract_males['Date'][ind] == '171012' and extract_males['Drug'][ind] == 'PCP' :
        amph_pcp_M.append([onsets, offsets, extract_males['RatID'][ind]])    


#FEMALES **********************************************************************

# assign empty list to add lists of lick onsets and offsets for all medfiles 
# SALINE
last_lick_sal_F, distraction_sal_F, hab1_sal_F, hab2_sal_F, amph_sal_F = [], [], [], [], []
# PCP
last_lick_pcp_F, distraction_pcp_F, hab1_pcp_F, hab2_pcp_F, amph_pcp_F = [], [], [], [], []

 
for ind, filename in enumerate(extract_females['MedFilenames']):
    path = medfolder + filename
    onsets, offsets = medfilereader(path, ['e', 'f'], remove_var_header = True)  # e onset, f offset
    med_dis_times, dis_type = medfilereader(path, ['i','j'], remove_var_header = True)
# SALINE
# Saline last licks day 
    if extract_females['Date'][ind] == '171124' and extract_females['Drug'][ind] == 'SAL' :
      last_lick_sal_F.append([onsets, offsets, extract_females['RatID'][ind]])      
  # Saline distraction 
    if extract_females['Date'][ind] == '171125' and extract_females['Drug'][ind] == 'SAL' :
      distraction_sal_F.append([onsets, offsets, dis_type, extract_females['RatID'][ind]])
  # Saline habituation 1
    if extract_females['Date'][ind] == '171126' and extract_females['Drug'][ind] == 'SAL' :
      hab1_sal_F.append([onsets, offsets, extract_females['RatID'][ind]])
  # Saline habituation 2
    if extract_females['Date'][ind] == '171127' and extract_females['Drug'][ind] == 'SAL' :
      hab2_sal_F.append([onsets, offsets, extract_females['RatID'][ind]]) 
  # Saline amphetamine IP
    if extract_females['Date'][ind] == '171128' and extract_females['Drug'][ind] == 'SAL' :
      amph_sal_F.append([onsets, offsets, extract_females['RatID'][ind]])
     
  # PCP
  # PCP last licks day 
    if extract_females['Date'][ind] == '171124' and extract_females['Drug'][ind] == 'PCP' :
      last_lick_pcp_F.append([onsets, offsets, extract_females['RatID'][ind]])   
  # PCP distraction 
    if extract_females['Date'][ind] == '171125' and extract_females['Drug'][ind] == 'PCP' :
      distraction_pcp_F.append([onsets, offsets, dis_type, extract_females['RatID'][ind]])
  # PCP habituation 1
    if extract_females['Date'][ind] == '171126' and extract_females['Drug'][ind] == 'PCP' :
      hab1_pcp_F.append([onsets, offsets, extract_females['RatID'][ind]])
  # PCP habituation 2
    if extract_females['Date'][ind] == '171127' and extract_females['Drug'][ind] == 'PCP' :
      hab2_pcp_F.append([onsets, offsets, extract_females['RatID'][ind]])
  # PCP amphetamine IP 
    if extract_females['Date'][ind] == '171128' and extract_females['Drug'][ind] == 'PCP' :
      amph_pcp_F.append([onsets, offsets, extract_females['RatID'][ind]])
    
# (3) Lick calc for last lick day (by group) for male PCP and SAL, for female PCP and SAL
# Licking analysis section, just last lick day 
# assign empty variables to store outputs from lick calc (to find means/groups stats)
# lists where each item is a dictionary (25) derived from lickCalc for each rat / day

lick_analysis_sal_M, lick_analysis_pcp_M,lick_analysis_sal_F, lick_analysis_pcp_F = [], [], [], []

for lists in last_lick_sal_M:
    licks = lists[0]
    offset = lists[1]    
    lick_analysis = lickCalc(licks, offset, burstThreshold = 0.25, runThreshold = 10)
    lick_analysis_sal_M.append(lick_analysis)

for lists in last_lick_pcp_M:
    licks = lists[0]
    offset = lists[1]    
    lick_analysis = lickCalc(licks, offset, burstThreshold = 0.25, runThreshold = 10)
    lick_analysis_pcp_M.append(lick_analysis)

for lists in last_lick_sal_F:
    licks = lists[0]
    offset = lists[1]    
    lick_analysis = lickCalc(licks, offset, burstThreshold = 0.25, runThreshold = 10)
    lick_analysis_sal_F.append(lick_analysis)

for lists in last_lick_pcp_F:
    licks = lists[0]
    offset = lists[1]    
    lick_analysis = lickCalc(licks, offset, burstThreshold = 0.25, runThreshold = 10)
    lick_analysis_pcp_F.append(lick_analysis)

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

# Saline males
all_n_bursts_sal_M, all_n_runs_sal_M, all_mean_IBI_sal_M, all_mean_IRI_sal_M, all_mean_burst_length_sal_M, all_mean_run_length_sal_M = [], [], [], [], [], []
# Pcp males
all_n_bursts_sal_M, all_n_runs_sal_M, all_mean_IBI_sal_M, all_mean_IRI_sal_M, all_mean_burst_length_sal_M, all_mean_run_length_sal_M = [], [], [], [], [], []
# Saline females
all_n_bursts_sal_M, all_n_runs_sal_M, all_mean_IBI_sal_M, all_mean_IRI_sal_M, all_mean_burst_length_sal_M, all_mean_run_length_sal_M = [], [], [], [], [], []
# Pcp females 
all_n_bursts_sal_M, all_n_runs_sal_M, all_mean_IBI_sal_M, all_mean_IRI_sal_M, all_mean_burst_length_sal_M, all_mean_run_length_sal_M = [], [], [], [], [], []


#function :
#def Group_Lick_Analysis(dictionary, bursts=True, runs=True):
    
#    Group_Lick_Analysis - Saline Males 

for dictionary in lick_analysis_sal_M: # reapeat for pcp and for the female data 
   
    n_bursts = dictionary['bNum']
    n_runs = dictionary['rNum']
    #Mean ILI for each burst for each rat then caclulate a mean of mean for the groups
    mean_inter_burst = np.mean(dictionary['bILIs']) 
    mean_burst_length = dictionary['bMean'] # bMean uses bLicks (n licks not ILIs)
    mean_inter_run = np.mean(dictionary['rILIs'])
    mean_run_length = dictionary['rMean']
    # median burst lengths, median inter-burst-intervals (all measures with medians)
    all_n_bursts_sal_M.append(n_bursts)
    all_n_runs_sal_M.append(n_runs)
    all_mean_IBI_sal_M.append(mean_inter_burst)
    all_mean_burst_length_sal_M.append(mean_burst_length) # rename this variable 
    all_mean_IRI_sal_M.append(mean_inter_run)
    all_mean_run_length_sal_M.append(mean_run_length)
# Can use these means to make plots, use the full lists to do statistics 
    # comparing saline to pcp for each variable - is there a difference between 
    # the numbers of bursts, the IBIs the runs etc. in sal and pcp (m then f)    
sal_M_mean_n_bursts = np.mean(all_n_bursts_sal_M)
sal_M_mean_n_runs = np.mean(all_n_runs_sal_M)
sal_M_mean_mean_IBI = np.mean(all_mean_IBI_sal_M)
sal_M_mean_mean_IRI = np.mean(all_mean_IRI_sal_M)

#    Group_Lick_Analysis - Pcp Males 
#    Group_Lick_Analysis - Sal Females 
#    Group_Lick_Analysis - Pcp Females 


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


###################################################################################

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

for index, rat in enumerate(discalc_sal_M):
    pdps_dis = []
    for distractorlick in rat[0]:
        
        if distractorlick in distraction_sal_M[index][0] and distractorlick != distraction_sal_M[index][0][-1]:
            lick_index = distraction_sal_M[index][0].index(distractorlick) 
            lick_index_plus1 = lick_index+1
            lick_index_minus3 = lick_index-3
            distracted_PDP = distraction_sal_M[index][0][lick_index_plus1] - distraction_sal_M[index][0][lick_index]

# NEED TO ADD STORAGE OF THESE PRE-DPS HERE (WITH THE APPEND)
            distracted_preDP = distraction_sal_M[index][0][lick_index] - distraction_sal_M[index][0][lick_index_minus3]
        
        pdps_dis.append(distracted_PDP)
    pdps_dis_sal_M.append([pdps_dis])

# Not distracted PDPs 

for index, rat in enumerate(discalc_sal_M):
    pdps_notdis = []
    for notdistractedlick in rat[1]:
        if notdistractedlick in distraction_sal_M[index][0] and notdistractedlick != distraction_sal_M[index][0][-1]:
            lick_index = distraction_sal_M[index][0].index(notdistractedlick) 
            lick_index_plus1 = lick_index+1
            lick_index_minus3 = lick_index-3
            notdistracted_PDP = distraction_sal_M[index][0][lick_index_plus1] - distraction_sal_M[index][0][lick_index]

            notdistracted_preDP = distraction_sal_M[index][0][lick_index] - distraction_sal_M[index][0][lick_index_minus3]
        
        pdps_notdis.append(notdistracted_PDP)
    pdps_notdis_sal_M.append([pdps_notdis])

# PCP MALES =============================================================================
# Cross check for number of distracted and not distracted trials in each group 
pdps_dis_pcp_M, pdps_notdis_pcp_M = [], []
for index, rat in enumerate(discalc_pcp_M):
    pdps_dis = []
    for distractorlick in rat[0]:
        
        if distractorlick in distraction_pcp_M[index][0] and distractorlick != distraction_pcp_M[index][0][-1]:
            lick_index = distraction_pcp_M[index][0].index(distractorlick) 
            lick_index_plus1 = lick_index+1
            lick_index_minus3 = lick_index-3
            distracted_PDP = distraction_pcp_M[index][0][lick_index_plus1] - distraction_pcp_M[index][0][lick_index]

            distracted_preDP = distraction_pcp_M[index][0][lick_index] - distraction_pcp_M[index][0][lick_index_minus3]
        
        pdps_dis.append(distracted_PDP)
    pdps_dis_pcp_M.append([pdps_dis])

# Not distracted PDPs 

for index, rat in enumerate(discalc_pcp_M):
    pdps_notdis = []
    for notdistractedlick in rat[1]:
        if notdistractedlick in distraction_pcp_M[index][0] and notdistractedlick != distraction_pcp_M[index][0][-1]:
            lick_index = distraction_pcp_M[index][0].index(notdistractedlick) 
            lick_index_plus1 = lick_index+1
            lick_index_minus3 = lick_index-3
            notdistracted_PDP = distraction_pcp_M[index][0][lick_index_plus1] - distraction_pcp_M[index][0][lick_index]

            notdistracted_preDP = distraction_pcp_M[index][0][lick_index] - distraction_pcp_M[index][0][lick_index_minus3]
        
        pdps_notdis.append(notdistracted_PDP)
    pdps_notdis_pcp_M.append([pdps_notdis])


# SALINE FEMALES

# Distracted pdps
pdps_dis_sal_F, pdps_notdis_sal_F = [], [] 

for index, rat in enumerate(discalc_sal_F):
    pdps_dis = []
    for distractorlick in rat[0]:
        
        if distractorlick in distraction_sal_F[index][0] and distractorlick != distraction_sal_F[index][0][-1]:
            lick_index = distraction_sal_F[index][0].index(distractorlick) 
            lick_index_plus1 = lick_index+1
            lick_index_minus3 = lick_index-3
            distracted_PDP = distraction_sal_F[index][0][lick_index_plus1] - distraction_sal_F[index][0][lick_index]

            distracted_preDP = distraction_sal_F[index][0][lick_index] - distraction_sal_F[index][0][lick_index_minus3]
        
        pdps_dis.append(distracted_PDP)
    pdps_dis_sal_F.append([pdps_dis])

# Not distracted PDPs 

for index, rat in enumerate(discalc_sal_F):
    pdps_notdis = []
    for notdistractedlick in rat[1]:
        if notdistractedlick in distraction_sal_F[index][0] and notdistractedlick != distraction_sal_F[index][0][-1]:
            lick_index = distraction_sal_F[index][0].index(notdistractedlick) 
            lick_index_plus1 = lick_index+1
            lick_index_minus3 = lick_index-3
            notdistracted_PDP = distraction_sal_F[index][0][lick_index_plus1] - distraction_sal_F[index][0][lick_index]

            notdistracted_preDP = distraction_sal_F[index][0][lick_index] - distraction_sal_F[index][0][lick_index_minus3]
        
        pdps_notdis.append(notdistracted_PDP)
    pdps_notdis_sal_F.append([pdps_notdis])

# PCP FEMALES 

pdps_dis_pcp_F, pdps_notdis_pcp_F = [], []
for index, rat in enumerate(discalc_pcp_F):
    pdps_dis = []
    for distractorlick in rat[0]:
        
        if distractorlick in distraction_pcp_F[index][0] and distractorlick != distraction_pcp_F[index][0][-1]:
            lick_index = distraction_pcp_F[index][0].index(distractorlick) 
            lick_index_plus1 = lick_index+1
            lick_index_minus3 = lick_index-3
            distracted_PDP = distraction_pcp_F[index][0][lick_index_plus1] - distraction_pcp_F[index][0][lick_index]

            distracted_preDP = distraction_pcp_F[index][0][lick_index] - distraction_pcp_F[index][0][lick_index_minus3]
        
        pdps_dis.append(distracted_PDP)
    pdps_dis_pcp_F.append([pdps_dis])

# Not distracted PDPs 

for index, rat in enumerate(discalc_pcp_F):
    pdps_notdis = []
    for notdistractedlick in rat[1]:
        if notdistractedlick in distraction_pcp_F[index][0] and notdistractedlick != distraction_pcp_F[index][0][-1]:
            lick_index = distraction_pcp_F[index][0].index(notdistractedlick) 
            lick_index_plus1 = lick_index+1
            lick_index_minus3 = lick_index-3
            notdistracted_PDP = distraction_pcp_F[index][0][lick_index_plus1] - distraction_pcp_F[index][0][lick_index]

            notdistracted_preDP = distraction_pcp_F[index][0][lick_index] - distraction_pcp_F[index][0][lick_index_minus3]
        
        pdps_notdis.append(notdistracted_PDP)
    pdps_notdis_pcp_F.append([pdps_notdis])
   
###################################################################################
###################################################################################
###################################################################################

# PRE DISTRACTOR PAUSES (then later for individual differences find correlation between
# pre pause and post pause, with different colours for points that are distracted
# or not)
            
 # Add in here loop to make list of PDPs for each rats and each for distracted and not

### Maybe add pre distraction pause to the post distraction pause code loops so it
# is all computed at the same tiem 

## DID YOU ACCESS THE AMPHETAMINE DAY???????????

#compare ALL rats distraction and habituation 
#
#compare all rats habituation and SAL and AMPH 
#
#for amphetamine, PDPs, percentage etc. 
#  
#
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
#
#
#Statistics (probably not in Python, probably use SPSS or R)
#
#ANOVA - effects of day, effects of PCP (in males and in females)
#ANOVA - effects of sex on distraction OR 3 way ANOVA (although 2 cohorts far appart)
#
#
## NOR
#
## Add in NOR scores for each rat too, the DI and then calculate group info 
#
## (1) Is there a NOR deficit when all male data are combined, is there a deficit in females
#
## (2) Does the individual NOR score correlate with any distraction measure??
#
## Correlations 
#
## Individual variations in burst number, cluster number and mean INTERBURST INTERVAL
#    # compared (correlation or regression) to PDP and distracted percentage 
#    
#    # Saline 
#    
#    
#    
#    
