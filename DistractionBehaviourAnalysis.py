#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 11:18:00 2018
@author: u1490431 (kp) 

DATA EXTRACTION - DISTRACTION BEHAVIOUR PAPER PETERS ET AL. 
DATA EXTRACTION - CHAPTER 3 PCPvSAL 

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

# Distraction day analysis (including modalities)

modalitykey = {'whitenoise':[1,4], 'tone':[2,5], 'combined3':[3,6]}
# MALES
# Saline
discalc_sal_M, percent_dis_whitenoise_sal_M, percent_dis_tone_sal_M,\
percent_dis_combined_sal_M, mean_percent_WHITENOISE_sal_M, mean_percent_TONE_sal_M,\
mean_percent_COMBINED_sal_M = discalc_modalities(distraction_sal_M, modalitykey)
# PCP
discalc_pcp_M, percent_dis_whitenoise_pcp_M, percent_dis_tone_pcp_M,\
percent_dis_combined_pcp_M, mean_percent_WHITENOISE_pcp_M, mean_percent_TONE_pcp_M,\
mean_percent_COMBINED_pcp_M = discalc_modalities(distraction_pcp_M, modalitykey)

# FEMALES
# Saline 
discalc_sal_F, percent_dis_whitenoise_sal_F, percent_dis_tone_sal_F,\
percent_dis_combined_sal_F, mean_percent_WHITENOISE_sal_F, mean_percent_TONE_sal_F,\
mean_percent_COMBINED_sal_F = discalc_modalities(distraction_sal_F, modalitykey)
# PCP
discalc_pcp_F, percent_dis_whitenoise_pcp_F, percent_dis_tone_pcp_F,\
percent_dis_combined_pcp_F, mean_percent_WHITENOISE_pcp_F, mean_percent_TONE_pcp_F,\
mean_percent_COMBINED_pcp_F = discalc_modalities(distraction_pcp_F, modalitykey)

# Modelled distractors ˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚
# Not including modalities 
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

pdps_dis_sal_M, med_pdps_dis_sal_M, preDPs_dis_sal_M,\
pdps_notdis_sal_M, med_pdps_notdis_sal_M, preDPs_notdis_sal_M,\
 = pdpbygroup(discalc_sal_M, distraction_sal_M) 

# PCP MALES
pdps_dis_pcp_M, med_pdps_dis_pcp_M, preDPs_dis_pcp_M,\
pdps_notdis_pcp_M, med_pdps_notdis_pcp_M, preDPs_notdis_pcp_M,\
 = pdpbygroup(discalc_pcp_M, distraction_pcp_M) 

# SALINE FEMALES
pdps_dis_sal_F, med_pdps_dis_sal_F, preDPs_dis_sal_F,\
pdps_notdis_sal_F, med_pdps_notdis_sal_F, preDPs_notdis_sal_F,\
 = pdpbygroup(discalc_sal_F, distraction_sal_F) 

# PCP FEMALES 
pdps_dis_pcp_F, med_pdps_dis_pcp_F, preDPs_dis_pcp_F,\
pdps_notdis_pcp_F, med_pdps_notdis_pcp_F, preDPs_notdis_pcp_F,\
 = pdpbygroup(discalc_pcp_F, distraction_pcp_F) 


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

percent_dis_dis_sal_M = percentdisgroup(discalc_sal_M)
percent_dis_modelled_sal_M = percentdisgroup(mod_dis_sal_M)
percent_dis_hab1_sal_M = percentdisgroup(hab1_dis_sal_M)
percent_dis_hab2_sal_M = percentdisgroup(hab2_dis_sal_M)
percent_dis_amph_sal_M = percentdisgroup(amph_dis_sal_M)

## PCP
percent_dis_dis_pcp_M = percentdisgroup(discalc_pcp_M)
percent_dis_modelled_pcp_M = percentdisgroup(mod_dis_pcp_M)
percent_dis_hab1_pcp_M = percentdisgroup(hab1_dis_pcp_M)
percent_dis_hab2_pcp_M = percentdisgroup(hab2_dis_pcp_M)
percent_dis_amph_pcp_M = percentdisgroup(amph_dis_pcp_M)

############# FEMALES - percent distracted 
## Remember might have an issue with the last PCP rat on amphetamine day
# division by zero potential problem/ Might remove this rat from ALL days for the plots?? 
# SALINE
percent_dis_dis_sal_F = percentdisgroup(discalc_sal_F)
percent_dis_modelled_sal_F = percentdisgroup(mod_dis_sal_F)
percent_dis_hab1_sal_F = percentdisgroup(hab1_dis_sal_F)
percent_dis_hab2_sal_F = percentdisgroup(hab2_dis_sal_F)
percent_dis_amph_sal_F = percentdisgroup(amph_dis_sal_F)

# PCP
percent_dis_dis_pcp_F = percentdisgroup(discalc_pcp_F[0:-1])
percent_dis_modelled_pcp_F = percentdisgroup(mod_dis_pcp_F[0:-1])
percent_dis_hab1_pcp_F = percentdisgroup(hab1_dis_pcp_F[0:-1])
percent_dis_hab2_pcp_F = percentdisgroup(hab2_dis_pcp_F[0:-1])
percent_dis_amph_pcp_F = percentdisgroup(amph_dis_pcp_F[0:-1]) 
######################### INDIVIDUAL DIFFERENCES #######################
#sb.jointplot(x=df['nRuns'], y=df['nBursts'], kind='hex')) #or type 'reg' for kernel estimation and regression
