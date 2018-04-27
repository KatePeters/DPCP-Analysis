#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 11:18:00 2018

@author: u1490431
"""

# (1) Find and extract info from the meatfile(s) 
#
metafile_males = '/Volumes/KP_HARD_DRI/kp259/DPCP_ALL/DPCP12Masterfile.csv'
metafile_females = '/Volumes/KP_HARD_DRI/kp259/DPCP_ALL/DPCP3_Metafile.csv'

#metafile_males = 'F:/kp259/DPCP_ALL/DPCP12Masterfile.csv'
#metafile_females = 'F:/kp259/DPCP_ALL/DPCP3_Metafile.csv' 

extract_males = MetaExtractor(metafile_males)
extract_females = MetaExtractor(metafile_females)
# Folder with all medfiles (DPCP1, DPCP2, DPCP3)
medfolder = '/Volumes/KP_HARD_DRI/kp259/DPCP_ALL/' # sometimes need space1 after DRI
#medfolder = 'F:/kp259/DPCP_ALL/'
# (2) - Get all lick onset/offset data for all rats/sessions 

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

# Subsetting all lick data by group (use dates to index) rat ID is saved in the list
#SALINE
# Saline last licks day    
    if extract_males['Date'][ind] == '170417' and extract_males['Drug'][ind] == 'SAL' \
    or extract_males['Date'][ind] == '171006' and extract_males['Drug'][ind] == 'SAL' :
        # Produces list of lists with 3 inner lists (onset, offset, rat ID)
        last_lick_sal_M.append([onsets, offsets, extract_males['RatID'][ind]])
# Saline distraction        
    if extract_males['Date'][ind] == '170418' and extract_males['Drug'][ind] == 'SAL' \
    or extract_males['Date'][ind] == '171007' and extract_males['Drug'][ind] == 'SAL' :
        distraction_sal_M.append([onsets, offsets, extract_males['RatID'][ind]])
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
        distraction_pcp_M.append([onsets, offsets, extract_males['RatID'][ind]])
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

# SALINE
# Saline last licks day 
    if extract_females['Date'][ind] == '171124' and extract_females['Drug'][ind] == 'SAL' :
      last_lick_sal_F.append([onsets, offsets, extract_females['RatID'][ind]])      
  # Saline distraction 
    if extract_females['Date'][ind] == '171125' and extract_females['Drug'][ind] == 'SAL' :
      distraction_sal_F.append([onsets, offsets, extract_females['RatID'][ind]])
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
      distraction_pcp_F.append([onsets, offsets, extract_females['RatID'][ind]])
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

# assign empty variables to store outputs from lick calc (to find means/groups stats)
# lists where each item is a dictionary (22) derived from lickCalc for each rat / day

# Would list comprehentions be better here, shorter more efficient??


lick_analysis_sal_M = []
lick_analysis_pcp_M = []
lick_analysis_sal_F = []
lick_analysis_pcp_F = []

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
    
# Decide which bits to access and how to average them per group, or input into SPSS/R
# Lick frequency is there, do SAL and PCP lick at different freq on average?
# take each value and store them 

# (a) Licking freuency (males) differences between PCP and SAL
# (b) Mean and median number of bursts or number of burst lengths, clusters, runs
    # ILI between bursts, or inter burst intervals 
    # ILI between runs / clusters 
    # Instantaneous licking frequency - some ratio calculation 
# (c) Distributions of burst lengths (cloud/comparisons of distributions)
  
#which variables does lickcac take? Remember the indexing with these variables, 3 lists
#
#last_lick_sal_M
#last_lick_pcp_M

# (4) Distraction calc / distracted or not for distraciton day (by group)

# Access the list structures of licks 
# Distraction calc 2 on those
# OUtput from distraction calc --> in to distracted or not 

# Stored in a master list of D or ND for each group 


# (5) Work out PDPs for all groups and store
# Produce an output and do all the statistics on these (decide tests and comparisons)






#! With the lickcalc output, add it to a master list of lists or dictionary/list 
#of dictionaries so that it can be indexed by file / rat / day 
#
#A male dictionary and a female discitonary / list of lists is probably best 
#
#
##(3)    
#for distraction days for all rats (all after the last lick, for cols with 2):
#    take that lick variable and run DistractioCalc2 (on just distraction days, and modelled?)
#    take d produced from DistractionCalc2 and run distractedOrNot on all
#    store in a list called --> distracted or not 
#
#! Sanity check that numbers are what expected (with small differences for med issue)
##(4) Sort by day, treatment and sex
## Analyse licking only 
## Metafile extractor will produce the lists of which rats are which (twice m and f)
#
#take data from last licking day only (use meta extractor to index just this day)
#
#   
#for all lists of licks :
#    do lickcalc
#    and if sal (from variable lists in metaextractor) store in one place (define earlier)
#    and if pcp store here
#    
#    #this will produce all the burst info for each rat on each day 
#    # store these values and then later, find the means / medians like THPH1 and 2
#    
#    # just last licking day, are there differences between pcp and saline here?
#    # no. bursts, runs, etc. set boundaries for cut offs 
#    
#DISTRACTION
#
##(5) Compare real and modelled distractors
#
#for last lick day do the distracted or not / access from earlier variables stored :
#    compare this to the lick day 
#    work out percentage distracted 
#    work our PDPs (all)
#    work out PDPs (distracted) and pdps (not distracted)
#    
#other metrics of distraction ?? 
#
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
