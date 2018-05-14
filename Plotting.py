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

c = ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1',]
df = pd.DataFrame()
df['nRuns'] = a
df['Group'] = b
df['all'] = c


# Should make PANDAS dataframe here so you can access labels with col names 

fig, ax = plt.subplots(1,1)
ax = sb.violinplot(hue=df['Group'], y=df['nRuns'], x=df['all'], palette="muted", split=True, scale="width", scale_hue=False, inner=None)
ax = sb.swarmplot(y=df['nRuns'], x=df['all'], color="grey", edgecolor="grey", split=True)


inner=None


# offset stuff
delta = 0.5
for ii, item in enumerate(ax.collections):
    # axis contains PolyCollections and PathCollections
    if isinstance(item, matplotlib.collections.PolyCollection):
        # get path
        path= item.get_paths()
        vertices = path.vertices

        # shift x-coordinates of path
        if not inner:
            if ii % 2: # -> to right
                vertices[:,0] += delta
            else: # -> to left
                vertices[:,0] -= delta



