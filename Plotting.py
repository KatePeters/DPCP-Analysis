#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 10:12:21 2018

@author: u1490431
"""

''' Contains code for plotting Distraction Behaviour '''

# (1) Bar scatter plots for licking 

MALES

which groups? 
what variables?
individual data points with means 


barscatter(data)


  (2)  data - lick day not paired. Bursts, lengths 
  Bursts IBIs
  Runs 
  
  BY GROUP - saline and pcp (male and female )
    
    AND 
    
  (1)  percent distracted lick day, distraction, habituation, hab2, apmetamine IP 
    
    
    
DATA FORMAT :


'''
data = [all_mean_IBI_sal_M, all_mean_IBI_sal_M]
distractionData = np.empty((2,), dtype=np.object)
distractionData[0] = np.array(all_mean_IBI_sal_M)
distractionData[1] = np.array(all_mean_IBI_sal_M)
'''


meanburstlength = np.empty((2,), dtype=np.object)
meanburstlength[0] = np.array(all_mean_burst_length_sal_M)
meanburstlength[1] = np.array(all_mean_burst_length_pcp_M)
#meanburstlength[2] = np.array(all_mean_burst_length_sal_F)
#meanburstlength[3] = np.array(all_mean_burst_length_pcp_F)

meanrunlength = np.empty((2,), dtype=np.object)
meanrunlength[0] = np.array(all_mean_run_length_sal_M)
meanrunlength[1] = np.array(all_mean_run_length_pcp_M)
#meanrunlength[2] = np.array(all_mean_run_length_sal_F)
#meanrunlength[3] = np.array(all_mean_run_length_pcp_F)

nbursts = np.empty((2,), dtype=np.object)
nbursts[0] = np.array(all_n_bursts_sal_M)
nbursts[1] = np.array(all_n_bursts_pcp_M)
#nbursts[2] = np.array(all_n_bursts_sal_F)
#nbursts[3] = np.array(all_n_bursts_pcp_F)

nruns = np.empty((4,), dtype=np.object)
nruns[0] = np.array(all_n_runs_sal_M)
nruns[1] = np.array(all_n_runs_pcp_M)
#nruns[2] = np.array(all_n_runs_sal_F)
#nruns[3] = np.array(all_n_runs_pcp_F)

meanIBI = np.empty((2,), dtype=np.object)
meanIBI[0] = np.array(all_mean_IBI_sal_M)
meanIBI[1] = np.array(all_mean_IBI_pcp_M)
#meanIBI[2] = np.array(all_mean_IBI_sal_F)
#meanIBI[3] = np.array(all_mean_IBI_pcp_F)

meanIRI = np.empty((2,), dtype=np.object)
meanIRI[0] = np.array(all_mean_IRI_sal_M)
meanIRI[1] = np.array(all_mean_IRI_pcp_M)
#meanIRI[2] = np.array(all_mean_IRI_sal_F)
#meanIRI[3] = np.array(all_mean_IRI_pcp_F)



a = []
a.extend(nruns[0])
a.extend(nruns[1])

b = ['sal','sal','sal','sal','sal','sal','sal','sal','sal','sal','sal','sal','sal',\
     'sal','sal','sal','pcp','pcp','pcp','pcp','pcp','pcp','pcp','pcp','pcp','pcp',\
     'pcp','pcp','pcp','pcp','pcp','pcp']


c = ['a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a',]

d = [15]
e = [-15]
df = pd.DataFrame()
df['nRuns'] = a
df['Group'] = b
df['all'] = c

# Should make PANDAS dataframe here so you can access labels with col names 

fig, ax = plt.subplots(1,1)

plt.yticks()
ax = sb.violinplot(hue=df['Group'], x=df['nRuns'], y=df['all'], bw = 0.4, palette=['orange', 'lightblue'], split=True, scale="width", inner=None)
ax = sb.swarmplot(x=df['nRuns'][0:16], y=df['all'], color="orange", edgecolor="orange", split=True)
ax = sb.swarmplot(x=df['nRuns'][16:32], y=df['all'], color="lightblue", edgecolor="lightblue", split=True)
ax.bar(15,0.1) # USE THIS TO ADD IN MEAN/MEDIAN  - MAKE BARS NARROW AND CLEANER

## HOW DO I FIX OVERLAPPING POINTS ON PLOT, for 2 data sets???? 

# d is the position on X axis, first arg. e if negative is up if pos is down make them both 32 (or n observations)

inner=None
delta =0.05
final_width = 0.6
inner=None

offset_violinplot_halves(ax, delta, final_width, inner, 'horizontal')


