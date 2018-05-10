#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 19:16:10 2018

@author: u1490431
"""

import matplotlib.pyplot as plt

filename = '!2017-04-18_08h50m.Subject dpcp1.7'
path = medfolder + filename
#allvars = medfilereader(path, remove_var_header = True)


med_dis_times, dis_type = medfilereader(path, varsToExtract = ['i','j'], remove_var_header = True)

onsets, offsets = medfilereader(path, ['e', 'f'], remove_var_header = True)

discalc = distractionCalc2(onsets)

# Checking that med distractor times match calculated distractors
#plt.scatter(med_dis_times, discalc)
#
#diffs = [x for x in med_dis_times if x not in discalc]
#
#diff_between = np.asarray(med_dis_times) - np.asarray(discalc)



distracted, notdistracted = distractedOrNot(discalc, onsets)


distracted_bool2 = np.in1d(discalc, distracted)

auditory = [1, 2]
visual = [3, 4]
mixed = [5, 6]


dis_numeric = []
for d in distracted:
    dis_numeric.append([dis_type[idx] for idx, val in enumerate(discalc) if val == d][0])

ndis_numeric = []
for n in notdistracted:
    ndis_numeric.append([dis_type[idx] for idx, val in enumerate(discalc) if val == n][0])
    

dis_numeric = [int(d) for d in dis_numeric]

dis_type_text = []
for d in dis_numeric:
    if d in auditory:
        dis_type_text.append('auditory')
    elif d in visual:
        dis_type_text.append('visual')
    elif d in mixed:
        dis_type_text.append('mixed')
        

# Distraction code from medPC04 - check this is the same as the code used in all DPCP 

1 = white noise + house light # 3
4 = white noise + cue light # 5 
2 = tone + house light # 4
5 = tone + cue light # 6 

3 = white noise + tone + house light # probably the most salient 1
6 = white noise + tone + light cue # 2

# Could separate by (1) White noise vs tone vs massive combined 
1 and 4
2 and 5
3 and 6 
# Or by (2) House light vs cue light vs massive combined 
1 and 2
4 and 5
3 and 6 

# Do both ( 3 groups ) by sounds different and light different as no just sound or just light 