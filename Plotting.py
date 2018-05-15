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
# PUT ALL OF THE BURST LENGTHS IN HERE, THEN SEE AND ADD IN MEAN MEAN BURST LENGTH
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



#### nRuns
a = []
a.extend(nruns[0])
a.extend(nruns[1])
b = ['sal','sal','sal','sal','sal','sal','sal','sal','sal','sal','sal','sal','sal',\
     'sal','sal','sal','pcp','pcp','pcp','pcp','pcp','pcp','pcp','pcp','pcp','pcp',\
     'pcp','pcp','pcp','pcp','pcp','pcp']
# Arbitrary value (not numeric is horizontal) with n values for data points
c = ['a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a']
# c = ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']

df = pd.DataFrame()
df['nRuns'] = a
df['Group'] = b
df['Drug treatment'] = c

median_nRuns_sal_M = np.median(nruns[0])
median_nRuns_pcp_M = np.median(nruns[1])

sb.set_style("white")
fig, ax = plt.subplots(1,1)

plt.yticks()
ax = sb.violinplot(hue=df['Group'], x=df['nRuns'], y=df['Drug treatment'], bw = 0.4, palette=['dodgerblue', 'hotpink'], split=True, saturation=1, scale="width", inner=None)
ax.legend().set_visible(False)

ax = sb.swarmplot(x=df["nRuns"], y=df["Drug treatment"], hue=df["Group"], palette=['dodgerblue', 'hotpink'])
ax.bar(median_nRuns_pcp_M,0.3, color='white') # USE THIS TO ADD IN MEAN/MEDIAN  - MAKE BARS NARROW AND CLEANER
ax.bar(median_nRuns_sal_M,-0.3, color='white')
sb.despine(offset=10, trim=True)
ax.set_ylabel("")
ax.set(yticks=[]) 
# Choose the legend you want from the 4 options plotted
handles, labels = ax.get_legend_handles_labels()
l = plt.legend(handles[2:4], labels[2:4])
# Make a gap between the distributions for easier comparison, offset determined by delta
inner=None
delta =0.05
final_width = 0.6
inner=None
offset_violinplot_halves(ax, delta, final_width, inner, 'horizontal') ## Add this function to all funcs. be careful with import names sns vs sb

#### nBursts
a = []
a.extend(nbursts[0])
a.extend(nbursts[1])
b = ['sal','sal','sal','sal','sal','sal','sal','sal','sal','sal','sal','sal','sal',\
     'sal','sal','sal','pcp','pcp','pcp','pcp','pcp','pcp','pcp','pcp','pcp','pcp',\
     'pcp','pcp','pcp','pcp','pcp','pcp']
# Arbitrary value (not numeric is horizontal) with n values for data points
c = ['a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a',]

df = pd.DataFrame()
df['nBursts'] = a
df['Group'] = b
df['Drug treatment'] = c

median_nBursts_sal_M = np.median(nbursts[0])
median_nBursts_pcp_M = np.median(nbursts[1])

sb.set_style("white")
fig, ax2 = plt.subplots(1,1)

plt.yticks()
ax2 = sb.violinplot(hue=df['Group'], x=df['nBursts'], y=df['Drug treatment'], bw = 0.4, palette=['dodgerblue', 'hotpink'], split=True, saturation=1, scale="width", inner=None)
ax2.legend().set_visible(False)

ax2 = sb.swarmplot(x=df["nBursts"], y=df["Drug treatment"], hue=df["Group"], palette=['dodgerblue', 'hotpink'])
ax2.bar(median_nBursts_pcp_M,0.3, color='white') # USE THIS TO ADD IN MEAN/MEDIAN  - MAKE BARS NARROW AND CLEANER
ax2.bar(median_nBursts_sal_M,-0.3, color='white') 

sb.despine(offset=10, trim=True)
ax2.set_ylabel("")
ax2.set(yticks=[]) 
# Choose the legend you want from the 4 options plotted
handles, labels = ax.get_legend_handles_labels()
l = plt.legend(handles[2:4], labels[2:4])
# Make a gap between the distributions for easier comparison, offset determined by delta
inner=None
delta =0.05
final_width = 0.6
inner=None
offset_violinplot_halves(ax2, delta, final_width, inner, 'horizontal') ## Add this function to all funcs. be careful with import names sns vs sb



## Mean burst length 
a = []
a.extend(meanburstlength[0])
a.extend(meanburstlength[1])
b = ['sal','sal','sal','sal','sal','sal','sal','sal','sal','sal','sal','sal','sal',\
     'sal','sal','sal','pcp','pcp','pcp','pcp','pcp','pcp','pcp','pcp','pcp','pcp',\
     'pcp','pcp','pcp','pcp','pcp','pcp']
# Arbitrary value (not numeric is horizontal) with n values for data points
c = ['a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a']
# c = ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']

df = pd.DataFrame()
df['meanBurstlen'] = a
df['Group'] = b
df['Drug treatment'] = c

median_meanBurstlen_sal_M = np.median(meanburstlength[0])
median_meanBurstlen_pcp_M = np.median(meanburstlength[1])

sb.set_style("white")
fig, ax3 = plt.subplots(1,1)

plt.yticks()
ax3 = sb.violinplot(hue=df['Group'], x=df['meanBurstlen'], y=df['Drug treatment'], bw = 0.4, palette=['dodgerblue', 'hotpink'], split=True, saturation=1, scale="width", inner=None)
ax3.legend().set_visible(False)

ax3 = sb.swarmplot(x=df["meanBurstlen"], y=df["Drug treatment"], hue=df["Group"], palette=['dodgerblue', 'hotpink'])
ax3.bar(median_meanBurstlen_pcp_M,0.3, color='white') # USE THIS TO ADD IN MEAN/MEDIAN  - MAKE BARS NARROW AND CLEANER
ax3.bar(median_meanBurstlen_sal_M,-0.3, color='white')
sb.despine(offset=10, trim=True)
ax3.set_ylabel("")
ax3.set(yticks=[]) 
# Choose the legend you want from the 4 options plotted
handles, labels = ax.get_legend_handles_labels()
l = plt.legend(handles[2:4], labels[2:4])
# Make a gap between the distributions for easier comparison, offset determined by delta
inner=None
delta =0.05
final_width = 0.6
inner=None
offset_violinplot_halves(ax3, delta, final_width, inner, 'horizontal') ## Add this function to all funcs. be careful with import names sns vs sb

# Mean run length
a = []
a.extend(meanrunlength[0])
a.extend(meanrunlength[1])
b = ['sal','sal','sal','sal','sal','sal','sal','sal','sal','sal','sal','sal','sal',\
     'sal','sal','sal','pcp','pcp','pcp','pcp','pcp','pcp','pcp','pcp','pcp','pcp',\
     'pcp','pcp','pcp','pcp','pcp','pcp']
# Arbitrary value (not numeric is horizontal) with n values for data points
c = ['a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a']
# c = ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']

df = pd.DataFrame()
df['meanRunlen'] = a
df['Group'] = b
df['Drug treatment'] = c

median_meanRunlen_sal_M = np.median(meanrunlength[0])
median_meanRunlen_pcp_M = np.median(meanrunlength[1])

sb.set_style("white")
fig, ax4 = plt.subplots(1,1)

plt.yticks()
ax4 = sb.violinplot(hue=df['Group'], x=df['meanRunlen'], y=df['Drug treatment'], bw = 0.4, palette=['dodgerblue', 'hotpink'], split=True, saturation=1, scale="width", inner=None)
ax4.legend().set_visible(False)

ax4 = sb.swarmplot(x=df["meanRunlen"], y=df["Drug treatment"], hue=df["Group"], palette=['dodgerblue', 'hotpink'])
ax4.bar(median_meanRunlen_pcp_M,0.3, color='white') # USE THIS TO ADD IN MEAN/MEDIAN  - MAKE BARS NARROW AND CLEANER
ax4.bar(median_meanRunlen_sal_M,-0.3, color='white')
sb.despine(offset=10, trim=True)
ax4.set_ylabel("")
ax4.set(yticks=[]) 
# Choose the legend you want from the 4 options plotted
handles, labels = ax.get_legend_handles_labels()
l = plt.legend(handles[2:4], labels[2:4])
# Make a gap between the distributions for easier comparison, offset determined by delta
inner=None
delta =0.05
final_width = 0.6
inner=None
offset_violinplot_halves(ax4, delta, final_width, inner, 'horizontal') ## Add this function to all funcs. be careful with import names sns vs sb


# Mean IBI 
a = []
a.extend(meanIBI[0])
a.extend(meanIBI[1])
b = ['sal','sal','sal','sal','sal','sal','sal','sal','sal','sal','sal','sal','sal',\
     'sal','sal','sal','pcp','pcp','pcp','pcp','pcp','pcp','pcp','pcp','pcp','pcp',\
     'pcp','pcp','pcp','pcp','pcp','pcp']
# Arbitrary value (not numeric is horizontal) with n values for data points
c = ['a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a']
# c = ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']

df = pd.DataFrame()
df['meanIBI'] = a
df['Group'] = b
df['Drug treatment'] = c

median_IBI_sal_M = np.median(meanIBI[0])
median_IBI_pcp_M = np.median(meanIBI[1])

sb.set_style("white")
fig, ax45= plt.subplots(1,1)

plt.yticks()
ax5 = sb.violinplot(hue=df['Group'], x=df['meanIBI'], y=df['Drug treatment'], bw = 0.4, palette=['dodgerblue', 'hotpink'], split=True, saturation=1, scale="width", inner=None)
ax5.legend().set_visible(False)

ax5 = sb.swarmplot(x=df["meanIBI"], y=df["Drug treatment"], hue=df["Group"], palette=['dodgerblue', 'hotpink'])
ax5.bar(median_IBI_pcp_M,0.3, color='white') # USE THIS TO ADD IN MEAN/MEDIAN  - MAKE BARS NARROW AND CLEANER
ax5.bar(median_IBI_sal_M,-0.3, color='white')
sb.despine(offset=10, trim=True)
ax5.set_ylabel("")
ax5.set(yticks=[]) 
# Choose the legend you want from the 4 options plotted
handles, labels = ax5.get_legend_handles_labels()
l = plt.legend(handles[2:4], labels[2:4])
# Make a gap between the distributions for easier comparison, offset determined by delta
inner=None
delta =0.05
final_width = 0.6
inner=None
offset_violinplot_halves(ax5, delta, final_width, inner, 'horizontal') ## Add this function to all funcs. be careful with import names sns vs sb


# Mean IRI 
