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
# Produce medians/means for individual rats and group means 
# Assign empty variables to store all data (before calc means etc.)

all_n_bursts_sal_M, all_n_runs_sal_M, all_mean_IBI_sal_M, all_mean_IRI_sal_M = [], [], [], []

for dictionary in lick_analysis_sal_M: # reapeat for pcp and for the female data 
    
    n_bursts = dictionary['bNum']
    n_runs = dictionary['rNum']
    #Mean ILI for each rat then caclulate a mean of mean for the groups
    mean_inter_burst = np.mean(dictionary['bILIs'])   
    mean_inter_run = np.mean(dictionary['rILIs'])
 #   bMean, rMean (mean rILI which is the IRI) 

    all_n_bursts_sal_M.append(n_bursts)
    all_n_runs_sal_M.append(n_runs)
    all_mean_IBI_sal_M.append(mean_inter_burst)
    
# Can use these means to make plots, use the full lists to do statistics 
    # comparing saline to pcp for each variable - is there a difference between 
    # the numbers of bursts, the IBIs the runs etc. in sal and pcp (m then f)
    
sal_M_mean_n_bursts = np.mean(all_n_bursts_sal_M)
sal_M_mean_n_runs = np.mean(all_n_runs_sal_M)
sal_M_mean_mean_IBI = np.mean(all_mean_IBI_sal_M)
sal_M_mean_mean_IRI = np.mean(all_mean_IRI_sal_M)


 #! Thought - measure of variability in the data, are saline tighter than PCP?
    # If so, what does this mean and how can I quantify it? Distribution comparisons and 
    # Violin plots as comparison 
    
    # number of bursts, number of runs 
    # median burst length (np.median) - add this to lick calc (median)
    
    # add median inter-burst interval to lick calc 
    # groups analysis (1) then individual differences (logistc or linear regressions/correlations 
                      # machine learning)
    
    
    # can access anything in the dictionaries by the keys here 



# (a) Licking freuency (males) differences between PCP and SAL
#calculate mean lick frequency (all lick around 7) compare saline and pcp (M)
#calculate mean lick frequency (females)

# what is the mean length of bursts? or median ?
# what is the mean number of bursts? - for groups (get the individual data into variables/excel)
# (b) Mean and median number of bursts or number of burst lengths, clusters, runs
    # ILI between bursts, or inter burst intervals 
    # ILI between runs / clusters 
    # Instantaneous licking frequency - some ratio calculation 
# (c) Distributions of burst lengths (cloud/comparisons of distributions)
# (d) Compare actual number of bursts and then mean length of the bursts
    # Group comparisons for PCP/SAL in males and females  


################################################################################

# DISTRACTION ANALYSIS DPCP (1,2,3)

################################################################################

# Distraction day analysis 

''' Licking data already subset earlier '''

discalc_sal_M, discalc_pcp_M, discalc_sal_F, discalc_pcp_F = [], [], [], []  

for rat in distraction_sal_M:
    discalc = distractionCalc2(rat[0])
    distracted, notdistracted = distractedOrNot(discalc, rat[0])
  #  work out percentage and add this too 
    discalc_sal_M.append([distracted, notdistracted])
  # Work out pdp for distracted and not distracted for each rat
  # Then find means from the lists inside the master list 

for rat in distraction_pcp_M:
    discalc = distractionCalc2(rat[0])
    distracted, notdistracted = distractedOrNot(discalc, rat[0])
    discalc_pcp_M.append([distracted, notdistracted])

for rat in distraction_sal_F:
    discalc = distractionCalc2(rat[0])
    distracted, notdistracted = distractedOrNot(discalc, rat[0])
    discalc_sal_F.append([distracted, notdistracted])

for rat in distraction_pcp_F:
    discalc = distractionCalc2(rat[0])
    distracted, notdistracted = distractedOrNot(discalc, rat[0])
    discalc_pcp_F.append([distracted, notdistracted])


# Modelled distractors ˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚

mod_dis_sal_M, mod_dis_pcp_M, mod_dis_sal_F, mod_dis_pcp_F = [], [], [], []

# last_lick_sal_M, last_lick_pcp_M, last_lick_pcp_F, last_lick_sal_F 

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

''' Previous PDP code '''

for distractedtrials and for non distraxged (lists) find the lick which this :
    distractor was presented and then find the pdp 
    
    see previous code for how I did this earlier??

for ind, lists in enumerate(adjustedDistractors):
    pdp = []
    for value in lists:
        if value in allLickDataArray[ind] and value != allLickDataArray[ind][-1]: #if the value is in this list of licks (from all)
            index = allLickDataArray[ind].index(value)
            pdp.append(allLickDataArray[ind][index+1] - allLickDataArray[ind][index])
    pdpAll.append(pdp)    

# (5) Work out PDPs for all groups and store
# Produce an output and do all the statistics on these (decide tests and comparisons)



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
