#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 15:59:30 2018

@author: u1490431
"""

'''
Function to work out means and medians for lick analysis by group 
'''

## LICK DAY ANALYSIS - BY GROUP 
# Produce medians/means for individual rats and group means 
# Assign empty variables to store all data (before calc means etc.)

# Saline males
all_n_bursts_sal_M, all_n_runs_sal_M, all_mean_IBI_sal_M, all_mean_IRI_sal_M, all_mean_burst_length_sal_M, all_mean_run_length_sal_M = [], [], [], [], [], []
# Pcp males
all_n_bursts_pcp_M, all_n_runs_pcp_M, all_mean_IBI_pcp_M, all_mean_IRI_pcp_M, all_mean_burst_length_pcp_M, all_mean_run_length_pcp_M = [], [], [], [], [], []
# Saline females
all_n_bursts_sal_F, all_n_runs_sal_F, all_mean_IBI_sal_F, all_mean_IRI_sal_F, all_mean_burst_length_sal_F, all_mean_run_length_sal_F = [], [], [], [], [], []
# Pcp females 
all_n_bursts_pcp_F, all_n_runs_pcp_F, all_mean_IBI_pcp_F, all_mean_IRI_pcp_F, all_mean_burst_length_pcp_F, all_mean_run_length_pcp_F = [], [], [], [], [], []


#function :
#def Group_Lick_Analysis(dictionary, bursts=True, runs=True):
    
#    Group_Lick_Analysis - Saline Males 

# takes a list of dictionaries and loops through to find means 

def grouped_lickanalysis(groupdicts, bursts=True, runs=True):

    for dictionary in groupdicts     
        grouped_lick = []
        all_n_bursts, all_n_runs, all_mean_IBI, all_mean_burst_length, \
        all_mean_IRI, all_mean_run_length = [], [], [], [], [], []
        
        n_bursts = dictionary['bNum']
        n_runs = dictionary['rNum']
        #Mean ILI for each burst for each rat then caclulate a mean of mean for the groups
        mean_inter_burst = np.mean(dictionary['bILIs']) 
        mean_burst_length = dictionary['bMean'] # bMean uses bLicks (n licks not ILIs)
        mean_inter_run = np.mean(dictionary['rILIs'])
        mean_run_length = dictionary['rMean']
        # median burst lengths, median inter-burst-intervals (all measures with medians)
        all_n_bursts.append(n_bursts)
        all_n_runs.append(n_runs)
        all_mean_IBI.append(mean_inter_burst)
        all_mean_burst_length.append(mean_burst_length) # rename this variable 
        all_mean_IRI.append(mean_inter_run)
        all_mean_run_length.append(mean_run_length)
    # Can use these means to make plots, use the full lists to do statistics 
        # comparing saline to pcp for each variable - is there a difference between 
        # the numbers of bursts, the IBIs the runs etc. in sal and pcp (m then f)    

    mean_n_bursts = np.mean(all_n_bursts)
    mean_n_runs = np.mean(all_n_runs)
    mean_mean_IBI = np.mean(all_mean_IBI)
    mean_mean_IRI = np.mean(all_mean_IRI)
    
    return mean_n_bursts, mean_n_runs, mean_mean_IBI, mean_mean_IRI,\
    all_n_bursts, all_n_runs, all_mean_IBI, all_mean_IRI, all_mean_burst_length, all_mean_run_length 










