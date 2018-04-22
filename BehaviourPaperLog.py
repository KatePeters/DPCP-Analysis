#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 11:18:01 2018

@author: u1490431
"""

''' 16/04/18 '''

# Made new script and added ideas / instructions for analysis 
# Try to make documentation very clear as you go along 
# Eventually transfer all of this to a Jupyter notebook 

Medfilereader
Check what it extracts then make huge meta file for ALL dpcp data (split by sal/pcp)

''' 21/04/18 ''' 

# Instructions 

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 11:18:00 2018

@author: u1490431
"""

###


1) Read in all 3 cohorts (individually) DPCP1, DPCP2, DPCP3 
2) Separate into PCP and SALINE animals (possible to just look at saline)
3) Separate into lick day data (all and last) and distraction day data (main and hab)

4) Work out basic parameters for groups and days
    (a) Number of bursts, clusters, runs 
    (b) Palatability for saccharin score based on these 
    (c) Mean. median number and length of bursts/etc

5) Predictive correlations or linear regression 
6) Machine learning, support vector machines (with scores from lick day to predict distractedness)
7) Scores from distraction day to predict group membership (are they PCP or SAL)

8) Subtle differences in PCP, timings and intervals of licks on licks day 

9) Different classifications of distracted or not? 

10) Variables for statistical comparison

11) If no PCP effect, clear analysis of distraction behaviour
    (a) What it does to bursts and licks 
    (b) How it affects consumption in general (is this still stable but structurally different)
 
    
# All data on R drive, move to hard drive for access and add the med files to git 
# in 3 folders of DPCP1, DPCP2, DPCP3 

# No metafile dor DPCP3!! 

# Which is male and female? Checking over "sheets"


Medfilereader
Check what it extracts then make huge meta file for ALL dpcp data (split by sal/pcp)


N = 16 - amphetamine effect, NOR 
N = 16 - amphetamine effects, NOR 
N = 24 (female) - amphetamine effects, NOR 

Percentage distracted
Number of bursts, number of clusters analysis 
Metrics for means, medians, etc. 

Literature searching 



For each rat scores: NOR deficit or NOR DI (sal and pcp) 
For each rat - number of bursts, clusters and licks on last lick day
For each rat - percentage distracted
For each rat - mean PDP 
For each rat - short, medium, long bursts 
For each rat - percent distracted amphetamine day 
For each rat - lick behaviour amphetamine day (numbers of bursts, clusters)

REALLY DEFINE BURSTS, CLUSTERS, RUNS ETC. and come up with a "score" for 
distraction. Percent distracted, pause length (on distracted trials and non-dis)
mean pause length for each rat ! Mean pause length as a whole and mean pause length
for JUST distracted and JUST non-distracted trials in EACH RAT :
    
    Then an average of these for groups saline, pcp (can aggregate 2 cohorts)
    Then show the females also (separate cohort with different treatment)
    
    On distraction day, habituation day and AMPHETAMINE! Show no effects on saline 
    Can we reverse, dehabituate the habituation effect with dopamnergic drugs???
    In saline and PCP animals 
    
Licking frequency within the bursts (expecting 6Hz) see if this is different 
in PCP 

INDIVIDUAL DIFFERENCES - saline only here (for now)
    Correlations of individual features (could make an aggregated "score") 
    Can these descriptors accurately predict (1)  Distraction, (2)  PCP/SAL 
    Rats preference or palatability of saccharin and the distractibility in later trials 
    AND habituation level


For all rats (sal) - mean number of bursts, clusters, last lick day 
For all rats (pcp) - mean number of bursts, clusters, last lick day 
For all rats (sal) - percentage distracted

PDPs mean as group 

Modelled distractors whether they would be distracted or not individual and as 
groups 

General licking patterns, microstructure differences on lick days 
How do we know it isnt just licking difference rather than distractability? 

''' 22/04/18 '''

# Edited Metafiles to fix issues 
# Replaced rat dpcp2.5 day 4 (lick train) data with day 3 (as missing file)

# Double check the files can be very easily indexed (file licks linked to ratID and day)

# Editing MetaExtractor to read correct cols in Metafiles as saved










    
    