# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:07:27 2018

@author: James Rig
"""


metafile_males = 'G:\kp259/DPCP_ALL\DPCP12Masterfile.csv'
metafile_females = 'G:\kp259\DPCP_ALL\DPCP3_Metafile.csv'
extract_males = MetaExtractor(metafile_males)
extract_females = MetaExtractor(metafile_females)
# Folder with all medfiles (DPCP1, DPCP2, DPCP3)
medfolder = 'G://kp259//DPCP_ALL//'


"""dates and drug should be lists"""
def subsetter(dictionary, dates, drug, verbose=False):
    subset = []
    for ind, filename in enumerate(dictionary['MedFilenames']):
        path = medfolder + filename
        onsets, offsets, med_dis_times, dis_type = medfilereader(path, ['e', 'f', 'i', 'j'], remove_var_header = True)  # e onset, f offset

        if dictionary['Date'][ind] in dates and dictionary['Drug'][ind] == drug:
            subset.append([onsets, offsets, dictionary['RatID'][ind]])
            if verbose: #assumes true
                print('filename, or comment ...') 
    return subset
    
#last_lick_pcp_F = subsetter(extract_females, ['171125'], 'PCP', verbose=True)    

## Could have 2 funcs, one for the for to give onsets/offsets that takes a dict 


def lickanalysis(lickdata, burstThreshold=0.25, runThreshold=10):
    analysis = []
    
    for lists in lickdata:
        lickon = lists[0]
        offset = lists[1]
        lick_analysis = lickCalc(lickon, offset, burstThreshold=burstThreshold, runThreshold=runThreshold)
        analysis.append(lick_analysis)
    return analysis


lick_analysis_sal_M = lickanalysis(last_lick_sal_M)

#for lists in last_lick_sal_M:
#    licks = lists[0]
#    offset = lists[1]    
#    
#    lick_analysis_sal_M.append(lick_analysis)