#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 11:18:00 2018

@author: u1490431
"""

#(1) Find and extract info from the meatfile(s) 
! Fix or delete missing files problem 
¡ Save metafiles as .csvs not xlxs (move them to the assigned folder)

# insert PC filepath here also for easy switching between PC and MAC 

matafile_males = '/Volumes/KP_HARD_DRI/kp259/DPCP_ALL/DPCP1&2Masterfile.csv'
metafile_females = '/Volumes/KP_HARD_DRI/kp259/DPCP_ALL/DPCP3_Metafile.csv'

extract_males = MetaExtractor(metafile_males)
extract_females = MetaExtractor(metafile_females)

# Useful info for sanity checks, and stored list of file names easy to access
folder = '/Volumes/KP_HARD_DRI/kp259/DPCP_ALL/'
# Folder with ALL files inside it - add them all to this folder 


#(2) - get all lick data for all rats, variables extracted from metafile 
#    - need licks onset and licks offset values from the med files for all
MALES

for each filename in the names (produced from metafilereader output):
    if include = 1 then index the same bit and run
    filename = folder + filename from loop 
    only those that are included in col (1)
    open the file, medfilereader it 
    produce the lick variable 
    
    = lickday data for all rats, do this twice. Once for the males (combined)
    and once for the females (total)

FEMALES


! With the lickcalc output, add it to a master list of lists or dictionary/list 
of dictionaries so that it can be indexed by file / rat / day 

A male dictionary and a female discitonary / list of lists is probably best 


#(3)    
for distraction days for all rats (all after the last lick, for cols with 2):
    take that lick variable and run DistractioCalc2 (on just distraction days, and modelled?)
    take d produced from DistractionCalc2 and run distractedOrNot on all
    store in a list called --> distracted or not 

! Sanity check that numbers are what expected (with small differences for med issue)
#(4) Sort by day, treatment and sex
# Analyse licking only 
# Metafile extractor will produce the lists of which rats are which (twice m and f)

take data from last licking day only (use meta extractor to index just this day)

   
for all lists of licks :
    do lickcalc
    and if sal (from variable lists in metaextractor) store in one place (define earlier)
    and if pcp store here
    
    #this will produce all the burst info for each rat on each day 
    # store these values and then later, find the means / medians like THPH1 and 2
    
    # just last licking day, are there differences between pcp and saline here?
    # no. bursts, runs, etc. set boundaries for cut offs 
    
DISTRACTION

#(5) Compare real and modelled distractors

for last lick day do the distracted or not / access from earlier variables stored :
    compare this to the lick day 
    work out percentage distracted 
    work our PDPs (all)
    work out PDPs (distracted) and pdps (not distracted)
    
other metrics of distraction ?? 

compare ALL rats distraction and habituation 

compare all rats habituation and SAL and AMPH 

for amphetamine, PDPs, percentage etc. 
  

GROUP DATA (ways to subset)

MALES 
PCP lick day mean PDP, mean percentage distracted, mean/median bursts
PCP distraction day mean PDP, mean percentage distracted, mean/median bursts
PCP habituation day mean PDP, mean percentage distracted, mean/median bursts
PCP salineIP day mean PDP, mean percentage distracted, mean/median bursts
PCP amphetamineIP day mean PDP, mean percentage distracted, mean/median bursts

SAL lick day mean PDP, mean percentage distracted, mean/median bursts
SAL distraction day mean PDP, mean percentage distracted, mean/median bursts
SAL habituation day mean PDP, mean percentage distracted, mean/median bursts
SAL salineIP day mean PDP, mean percentage distracted, mean/median bursts
SAL amphetamineIP day mean PDP, mean percentage distracted, mean/median bursts

FEMALES 
PCP lick day mean PDP, mean percentage distracted, mean/median bursts
PCP distraction day mean PDP, mean percentage distracted, mean/median bursts
PCP habituation day mean PDP, mean percentage distracted, mean/median bursts
PCP salineIP day mean PDP, mean percentage distracted, mean/median bursts
PCP amphetamineIP day mean PDP, mean percentage distracted, mean/median bursts

SAL lick day mean PDP, mean percentage distracted, mean/median bursts
SAL distraction day mean PDP, mean percentage distracted, mean/median bursts
SAL habituation day mean PDP, mean percentage distracted, mean/median bursts
SAL salineIP day mean PDP, mean percentage distracted, mean/median bursts
SAL amphetamineIP day mean PDP, mean percentage distracted, mean/median bursts


Statistics (probably not in Python, probably use SPSS or R)

ANOVA - effects of day, effects of PCP (in males and in females)
ANOVA - effects of sex on distraction OR 3 way ANOVA (although 2 cohorts far appart)


# NOR

# Add in NOR scores for each rat too, the DI and then calculate group info 

# (1) Is there a NOR deficit when all male data are combined, is there a deficit in females

# (2) Does the individual NOR score correlate with any distraction measure??

# Correlations 

# Individual variations in burst number, cluster number and mean INTERBURST INTERVAL
    # compared (correlation or regression) to PDP and distracted percentage 
    
    # Saline 
    
    
    
    
