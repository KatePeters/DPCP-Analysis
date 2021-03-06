#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 09:16:54 2018

@author: u1490431
"""
'''
   All imports and all functions needed for MMiN18 poster figures
   Run this script before anything else 
   
   Contains:
       
   loadmatfile, distractedOrNot, remcheck, distractionCalc2...
'''

# Import modules --------------------------------------------------------

import numpy as np
import scipy.io as sio

import matplotlib.pyplot as plt
import pandas as pd
import os
import matplotlib as mpl
import itertools
import matplotlib.mlab as mlab
import seaborn as sb
import statistics as stats
# Set plot parameters and styles

#sb.set_context("paper")
#sb.set_style("white")

# Plot settings, font / size / styles
#Calibri = {'fontname':'Calibri'}
#Size = {'fontsize': 20}
#label_size = 14
#plt.rcParams['xtick.labelsize'] = label_size 
#plt.rcParams['ytick.labelsize'] = label_size 

# Functions -------------------------------------------------------------

'''
    Loads a matlab converted TDT file, produces output session 
    dictionary of data from Synapse tankfiles. Photometry data
    and TTLs for licks, distractors etc.

'''

def loadmatfile(file):
    a = sio.loadmat(file, squeeze_me=True, struct_as_record=False)
    
    sessiondict = {}
    sessiondict['blue'] = a['output'].blue
    sessiondict['uv'] = a['output'].uv
    sessiondict['fs'] = a['output'].fs   
    sessiondict['licks'] = a['output'].licks.onset
    sessiondict['licks_off'] = a['output'].licks.offset

    sessiondict['distractors'] = distractionCalc2(sessiondict['licks'])

#   #write distracted or not to produce 2 lists of times, distracted and notdistracted
    #distracted, notdistracted= distractedOrNot(sessiondict['distractors'], sessiondict['licks'])
#    
    sessiondict['distracted'], sessiondict['notdistracted'] = distractedOrNot(sessiondict['distractors'], sessiondict['licks'])
   # sessiondict['notdistracted'] = notdistracted
   
 # ''' sessiondict['lickRuns'] = lickRunCalc(sessiondict['licks']) ''' 
    
    return sessiondict
# -----------------------------------------------------------------

def distractedOrNot(distractors, licks):
    distracted = []
    notdistracted = []
    lickList = []
    for l in licks:
        lickList.append(l)
    

    for index, distractor in enumerate(distractors):
        if distractor in licks:

            ind = lickList.index(distractor)
            try:
                if (licks[ind+1] - licks[ind]) > 1:
                    distracted.append(licks[ind])
                else:
                    if (licks[ind+1] - licks[ind]) < 1:
                        notdistracted.append(licks[ind])
            except IndexError:
                print('last lick was a distractor!!!')
                distracted.append(licks[ind])

    return(distracted, notdistracted)


def remcheck(val, range1, range2):
    # function checks whether value is within range of two decimels
    if (range1 < range2):
        if (val > range1) and (val < range2):
            return True
        else:
            return False
    else:
        if (val > range1) or (val < range2):
            return True
        else:
            return False


def distractionCalc2(licks, pre=1, post=1):
    licks = np.insert(licks, 0, 0)
    b = 0.001
    d = []
    idx = 3
    
    while idx < len(licks):
        if licks[idx]-licks[idx-2] < 1 and remcheck(b, licks[idx-2] % 1, licks[idx] % 1) == False:
                d.append(licks[idx])
                b = licks[idx] % 1
                idx += 1
                try:
                    while licks[idx]-licks[idx-1] < 1:
                        b = licks[idx] % 1
                        idx += 1
                except IndexError:
                    pass
        else:
            idx +=1
#    print(len(d))
    
#    print(d[-1])
    if len(d) > 1:
        if d[-1] > 3599:
            d = d[:-1]
        
#    print(len(d))
    
    return d


# LickCalc ============================================================
# Looking at function from Murphy et al (2017)

"""
This function will calculate data for bursts from a train of licks. The threshold
for bursts and clusters can be set. It returns all data as a dictionary.
"""
def lickCalc(licks, offset = [], burstThreshold = 0.25, runThreshold = 10, 
             binsize=60, histDensity = False):
    
    # makes dictionary of data relating to licks and bursts
    if type(licks) != np.ndarray or type(offset) != np.ndarray:
        try:
            licks = np.array(licks)
            offset = np.array(offset)
        except:
            print('Licks and offsets need to be arrays and unable to easily convert.')
            return

    lickData = {}

    if len(licks) == len(offset) + 1:
        licks = licks[0:-1]
    
    if len(offset) > 0:
        lickData['licklength'] = offset - licks
        lickData['longlicks'] = [x for x in lickData['licklength'] if x > 0.3]
    else:
        lickData['licklength'] = []
        lickData['longlicks'] = []

    lickData['licks'] = np.concatenate([[0], licks])
    lickData['ilis'] = np.diff(lickData['licks'])
    lickData['freq'] = 1/np.mean([x for x in lickData['ilis'] if x < burstThreshold])
    lickData['total'] = len(licks)
    
    # Calculates start, end, number of licks and time for each BURST 
    lickData['bStart'] = [val for i, val in enumerate(lickData['licks']) if (val - lickData['licks'][i-1] > burstThreshold)]  
    lickData['bInd'] = [i for i, val in enumerate(lickData['licks']) if (val - lickData['licks'][i-1] > burstThreshold)]
    lickData['bEnd'] = [lickData['licks'][i-1] for i in lickData['bInd'][1:]]
    lickData['bEnd'].append(lickData['licks'][-1])

    lickData['bLicks'] = np.diff(lickData['bInd'] + [len(lickData['licks'])])    
    lickData['bTime'] = np.subtract(lickData['bEnd'], lickData['bStart'])
    lickData['bNum'] = len(lickData['bStart'])
    if lickData['bNum'] > 0:
        lickData['bMean'] = np.nanmean(lickData['bLicks'])
        lickData['bMed'] = np.median(lickData['bLicks'])
    else:
        lickData['bMean'] = 0
        lickData['bMed'] = 0 
    
    lickData['bILIs'] = [x for x in lickData['ilis'] if x > burstThreshold]
    
    lickData['bILIs'] = [x for x in lickData['ilis'] if x > burstThreshold]

    # Calculates start, end, number of licks and time for each RUN
    lickData['rStart'] = [val for i, val in enumerate(lickData['licks']) if (val - lickData['licks'][i-1] > runThreshold)]  
    lickData['rInd'] = [i for i, val in enumerate(lickData['licks']) if (val - lickData['licks'][i-1] > runThreshold)]
    lickData['rEnd'] = [lickData['licks'][i-1] for i in lickData['rInd'][1:]]
    lickData['rEnd'].append(lickData['licks'][-1])

    lickData['rLicks'] = np.diff(lickData['rInd'] + [len(lickData['licks'])])    
    lickData['rTime'] = np.subtract(lickData['rEnd'], lickData['rStart'])
    lickData['rNum'] = len(lickData['rStart'])
    
    if lickData['rNum'] > 0:
        lickData['rMean'] = np.nanmean(lickData['rLicks'])
        lickData['rMed'] = np.median(lickData['rLicks'])
    else:
        lickData['rMean'] = 0
        lickData['rMed'] = 0 

    lickData['rILIs'] = [x for x in lickData['ilis'] if x > runThreshold]
    try:
        lickData['hist'] = np.histogram(lickData['licks'][1:], 
                                    range=(0, 3600), bins=int((3600/binsize)),
                                          density=histDensity)[0]
    except TypeError:
        print('Problem making histograms of lick data')
        
    return lickData  

def asnumeric(s):
    try:
        x = float(s)
        return x
    except ValueError:
        return float('nan')
    
def medfilereader(filename, varsToExtract = 'all',
                  sessionToExtract = 1,
                  verbose = False,
                  remove_var_header = False):
    if varsToExtract == 'all':
        numVarsToExtract = np.arange(0,26)
    else:
        numVarsToExtract = [ord(x)-97 for x in varsToExtract]
    
    f = open(filename, 'r')
    f.seek(0)
    filerows = f.readlines()[8:]
    datarows = [asnumeric(x) for x in filerows]
    matches = [i for i,x in enumerate(datarows) if x == 0.3]
    if sessionToExtract > len(matches):
        print('Session ' + str(sessionToExtract) + ' does not exist.')
    if verbose == True:
        print('There are ' + str(len(matches)) + ' sessions in ' + filename)
        print('Analyzing session ' + str(sessionToExtract))
    
    varstart = matches[sessionToExtract - 1]
    medvars = [[] for n in range(26)]
    
    k = int(varstart + 27)
    for i in range(26):
        medvarsN = int(datarows[varstart + i + 1])
        
        medvars[i] = datarows[k:k + int(medvarsN)]
        k = k + medvarsN
        
    if remove_var_header == True:
        varsToReturn = [medvars[i][1:] for i in numVarsToExtract]
    else:
        varsToReturn = [medvars[i] for i in numVarsToExtract]

    if np.shape(varsToReturn)[0] == 1:
        varsToReturn = varsToReturn[0]
    return varsToReturn


def MetaExtractor (metafile):
    f = open(metafile, 'r')
    f.seek(0)
    Metafilerows = f.readlines()[1:]
    tablerows = []

    for row in Metafilerows: 
        items = row.split(',')
        tablerows.append(items)

    MedFilenames, RatID, Date, Day, Session, Drug, TotLicks, Distractions, \
    NonDistractions, PercentDistracted = [], [], [], [], [], [], [], [], [], []

    for i, lst in enumerate(tablerows):
       MedFilenames = MedFilenames + [lst[0]]
       RatID = RatID + [lst[1]]
       Date = Date + [lst[2]]
       Day = Day + [lst[3]]
       Session = Session + [lst[4]]
       Drug = Drug + [lst[5]]
       TotLicks = TotLicks + [lst[6]]
       Distractions = Distractions + [lst[7]] 
       NonDistractions = NonDistractions + [lst[8]]
       PercentDistracted = PercentDistracted + [lst[9]]
 
    return ({'MedFilenames':MedFilenames, 'RatID':RatID, 'Date':Date, 'Day':Day, 'Session':Session, \
             'Drug':Drug, 'TotLicks':TotLicks, 'Distractions':Distractions, \
             'PercentDistracted':PercentDistracted})
    
def time2samples(self):
    tick = self.output.Tick.onset
    maxsamples = len(tick)*int(self.fs)
    if (len(self.data) - maxsamples) > 2*int(self.fs):
        print('Something may be wrong with conversion from time to samples')
        print(str(len(self.data) - maxsamples) + ' samples left over. This is more than double fs.')
    
    self.t2sMap = np.linspace(min(tick), max(tick), maxsamples)
    
def snipper(data, timelock, fs = 1, t2sMap = [], preTrial=10, trialLength=30,
                 adjustBaseline = True,
                 bins = 0):

    if len(timelock) == 0:
        print('No events to analyse! Quitting function.')
        raise Exception('no events')
    nSnips = len(timelock)
    pps = int(fs) # points per sample
    pre = int(preTrial*pps) 
#    preABS = preTrial
    length = int(trialLength*pps)
# converts events into sample numbers
    event=[]
    if len(t2sMap) > 1:
        for x in timelock:
            event.append(np.searchsorted(t2sMap, x, side="left"))
    else:
        event = [x*fs for x in timelock]

    avgBaseline = []
    snips = np.empty([nSnips,length])

    for i, x in enumerate(event):
        start = int(x) - pre
        avgBaseline.append(np.mean(data[start : start + pre]))
#        print(x)
        try:
            snips[i] = data[start : start+length]
        except: # Deals with recording arrays that do not have a full final trial
            snips = snips[:-1]
            avgBaseline = avgBaseline[:-1]
            nSnips = nSnips-1

    if adjustBaseline == True:
        snips = np.subtract(snips.transpose(), avgBaseline).transpose()
        snips = np.divide(snips.transpose(), avgBaseline).transpose()

    if bins > 0:
        if length % bins != 0:
            snips = snips[:,:-(length % bins)]
        totaltime = snips.shape[1] / int(fs)
        snips = np.mean(snips.reshape(nSnips,bins,-1), axis=2)
        pps = bins/totaltime
              
    return snips, pps

def trialsFig(ax, trials1, trials2, pps=1, preTrial=10, scale=5, noiseindex = [],
              plotnoise=True,
              eventText='event', 
              ylabel=''):

    if len(noiseindex) > 0:
        trialsNoise = np.array([i for (i,v) in zip(trials1, noiseindex) if v])
        trials1 = np.array([i for (i,v) in zip(trials1, noiseindex) if not v])
        if plotnoise == True:
            ax.plot(trialsNoise.transpose(), c='red', alpha=0.4)
        
    ax.plot(trials1.transpose(), c='lightblue', alpha=0.6)
    
    
    ax.plot(trials2.transpose(), c='thistle', alpha=0.6)
    ax.plot(np.mean(trials2, axis=0), c='purple', linewidth=2)
    ax.plot(np.mean(trials1,axis=0), c='blue', linewidth=2)
    ax.set(ylabel = ylabel)
    ax.xaxis.set_visible(False)
            
    scalebar = scale * pps

    yrange = ax.get_ylim()[1] - ax.get_ylim()[0]
    scalebary = (yrange / 10) + ax.get_ylim()[0]
    scalebarx = [ax.get_xlim()[1] - scalebar, ax.get_xlim()[1]]
    
    ax.plot(scalebarx, [scalebary, scalebary], c='k', linewidth=2)
    ax.text((scalebarx[0] + (scalebar/2)), scalebary-(yrange/50), str(scale) +' s', ha='center',va='top', **Calibri, **Size)
 
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    
    xevent = pps * preTrial  
    ax.plot([xevent, xevent],[ax.get_ylim()[0], ax.get_ylim()[1] - yrange/20],'--')
    ax.text(xevent, ax.get_ylim()[1], eventText, ha='center',va='bottom', **Calibri, **Size)
    
    return ax




def med_abs_dev(data, b=1.4826):
    median = np.median(data)
    devs = [abs(i-median) for i in data]
    mad = np.median(devs)*b
                   
    return mad

def findnoise(data, background, t2sMap = [], fs = 1, bins=0, method='sd'):
    
    bgSnips, _ = snipper(data, background, t2sMap=t2sMap, fs=fs, bins=bins)
    
    if method == 'sum':
        bgSum = [np.sum(abs(i)) for i in bgSnips]
        bgMAD = med_abs_dev(bgSum)
        bgMean = np.mean(bgSum)
    elif method == 'sd':
        bgSD = [np.std(i) for i in bgSnips]
        bgMAD = med_abs_dev(bgSD)
        bgMean = np.mean(bgSD)
   
    return bgMAD, bgMean


def makerandomevents(minTime, maxTime, spacing = 77, n=100):
    events = []
    total = maxTime-minTime
    start = 0
    for i in np.arange(0,n):
        if start > total:
            start = start - total
        events.append(start)
        start = start + spacing
    events = [i+minTime for i in events]
    return events


def makephotoTrials(self, bins, events, threshold=10):
    bgMAD = findnoise(self.data, self.randomevents,
                          t2sMap = self.t2sMap, fs = self.fs, bins=bins,
                          method='sum')          
    blueTrials, self.pps = snipper(self.data, events,
                                        t2sMap = self.t2sMap, fs = self.fs, bins=bins)        
    UVTrials, self.pps = snipper(self.dataUV, events,
                                        t2sMap = self.t2sMap, fs = self.fs, bins=bins)
    sigSum = [np.sum(abs(i)) for i in blueTrials]
    sigSD = [np.std(i) for i in blueTrials]
    noiseindex = [i > bgMAD*threshold for i in sigSum]

    return blueTrials, UVTrials, noiseindex


def removenoise(snipsIn, noiseindex):
    snipsOut = np.array([x for (x,v) in zip(snipsIn, noiseindex) if not v])   
    return snipsOut

def trialsMultShadedFig(ax, trials, pps = 1, scale = 5, preTrial = 10,
                      eventText = 'event', ylabel = '',
                      linecolor=['purple', 'blue'], errorcolor=['thistle', 'lightblue'],
                        title=''):
    
    for i in [0, 1]:
        yerror = [np.std(i)/np.sqrt(len(i)) for i in trials[i].T]
        y = np.mean(trials[i],axis=0)
        x = np.arange(0,len(y))
    
        ax.plot(x, y, c=linecolor[i], linewidth=2)

        errorpatch = ax.fill_between(x, y-yerror, y+yerror, color=errorcolor[i], alpha=0.8)
    
    ax.set(ylabel = ylabel)
    ax.xaxis.set_visible(False)
            
    scalebar = scale * pps

    yrange = ax.get_ylim()[1] - ax.get_ylim()[0]
    scalebary = (yrange / 10) + ax.get_ylim()[0]
    scalebarx = [ax.get_xlim()[1] - scalebar, ax.get_xlim()[1]]
    
    ax.plot(scalebarx, [scalebary, scalebary], c='k', linewidth=2) # below in '' = 5
    ax.text((scalebarx[0] + (scalebar/2)), scalebary-(yrange/50), '5 s', ha='center',va='top', **Calibri, **Size)
 
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    
    xevent = pps * preTrial
    ax.plot([xevent, xevent],[ax.get_ylim()[0], ax.get_ylim()[1] - yrange/20],'--')
    ax.text(xevent, ax.get_ylim()[1], eventText, ha='center',va='bottom', **Calibri, **Size)
    ax.set_title(title, fontsize=14)
    
    return ax, errorpatch

def nearestevents(timelock, events, preTrial=10, trialLength=30):
#    try:
#        nTrials = len(timelock)
#    except TypeError:
#        nTrials = 1
    data = []
    start = [x - preTrial for x in timelock]
    end = [x + trialLength - preTrial for x in start]
    for start, end in zip(start, end):
        data.append([x for x in events if (x > start) & (x < end)])
    for i, x in enumerate(data):
        data[i] = x - timelock[i]      
    
    return data

''' Barscatter '''

#colors = ['darkorange', 'orange']
#colors2 = ['k','k']
#colors3 = ['white', 'white']
 
def barscatter(data, transpose = False,
                groupwidth = .75,
                barwidth = .9,
                paired = False,
                barfacecoloroption = 'same', # other options 'between' or 'individual'
                barfacecolor = ['white'],
                baredgecoloroption = 'same',
                baredgecolor = ['black'],
                baralpha = 1,
                scatterfacecoloroption = 'same',
                scatterfacecolor = ['white'],
                scatteredgecoloroption = 'same',
                scatteredgecolor = ['grey'],
                scatterlinecolor = 'grey', # Don't put this value in a list
                scattersize = 80,
                scatteralpha = 1,
                linewidth=1,
                ylabel = 'none',
                xlabel = 'none',
                title = 'none',
                grouplabel = 'auto',
                itemlabel = 'none',
                yaxisparams = 'auto',
                show_legend = 'none',
                legendloc='upper right',
                ax=[]):
#
#    if type(data) == float
    # Check if transpose = True
    if transpose == True:
        data = np.transpose(data)
        
    # Initialize arrays and calculate number of groups, bars, items, and means
    
    barMeans = np.zeros((np.shape(data)))
    items = np.zeros((np.shape(data)))
    
    nGroups = np.shape(data)[0]
    groupx = np.arange(1,nGroups+1)

    if len(np.shape(data)) > 1:
        grouped = True
        barspergroup = np.shape(data)[1]
        barwidth = (barwidth * groupwidth) / barspergroup
        
        for i in range(np.shape(data)[0]):
            for j in range(np.shape(data)[1]):
                barMeans[i][j] = np.mean(data[i][j])
                items[i][j] = len(data[i][j])
        
    else:
        grouped = False
        paired = True
        barspergroup = 1
        
        for i in range(np.shape(data)[0]):
            barMeans[i] = np.mean(data[i])
            items[i] = len(data[i])
    
    # Calculate x values for bars and scatters    
    xvals = np.zeros((np.shape(data)))
    barallocation = groupwidth / barspergroup
    k = (groupwidth/2) - (barallocation/2)
    
    if grouped == True:
        
        for i in range(np.shape(data)[0]):
            xrange = np.linspace(i+1-k, i+1+k, barspergroup)
            for j in range(barspergroup):
                xvals[i][j] = xrange[j]
    else:
        xvals = groupx
    
    # Set colors for bars and scatters  
    #colors = ['#1abc9c', '#f1c40f', '#d35400', '#3498db', '#8e44ad']
    colors = ['dodgerblue', 'hotpink', 'dodgerblue', 'hotpink']
    colors2 = ['k','k','k', 'k', 'k']
    colors3 = ['white', 'white','white']
    
    barfacecolorArray = setcolors("individual", colors, 1, 2, data, paired_scatter = False)
    baredgecolorArray = setcolors("individual", colors, 1, 2, data, paired_scatter = False)
     
    scfacecolorArray = setcolors("individual", colors3, 1, 2, data, paired_scatter = False)
    scedgecolorArray = setcolors("individual", colors2, 1, 2, data, paired_scatter = False)
 #   scfacecolorArray = setcolors("between", colors3, nGroups=nGroups, barspergroup=barspergroup, data=dataX, paired_scatter = True)
    
# Initialize figure
    if ax == []:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.tick_params(axis='both', which='major', labelsize=14)
        fig.tight_layout()
    
    # Make bars
    barlist = []
    barx = []
    for x, y, bfc, bec in zip(xvals.flatten(), barMeans.flatten(),
                              barfacecolorArray, baredgecolorArray):
        barx.append(x)
        barlist.append(ax.bar(x, y, barwidth,
                         facecolor = bfc, edgecolor = bec,
                         zorder=-1))
    
    # Make scatters
    sclist = []
    if paired == False:
        for x, Yarray, scf, sce  in zip(xvals.flatten(), data.flatten(),
                                        scfacecolorArray, scedgecolorArray):
            for y in Yarray:
                sclist.append(ax.scatter(x, y, s = scattersize,
                         c = scf,
                         edgecolors = sce,
                         zorder=1))

    else:
        try:
            np.shape(data)[1]
            for x, Yarray, scf, sce in zip(xvals, data, scfacecolorArray, scedgecolorArray):
                for y in np.transpose(Yarray.tolist()):
                    sclist.append(ax.plot(x, y, '-o', markersize = scattersize/10,
                             color = scatterlinecolor,
                             linewidth=linewidth,
                             markerfacecolor = scf,
                             markeredgecolor = sce))

# Explicitly added color here, issue with assignment of scf and sce 
        except IndexError:                    
            print(len(data[0]))
            for n,_ in enumerate(data[0]):
                y = [y[n-1] for y in data]
                sclist.append(ax.plot(xvals, y, '-o', markersize = scattersize/10,
                             color = 'grey',
                             linewidth=linewidth,
                             markerfacecolor = 'white',
                             markeredgecolor = 'k'))
                
    # Label axes
    if ylabel != 'none':
        plt.ylabel(ylabel, fontsize=14)
    
    if xlabel != 'none':
        plt.xlabel(xlabel)
        
    if title != 'none':
        plt.title(title, fontsize=14)
    
    # Set range and tick values for Y axis
    if yaxisparams != 'auto':
        ax.set_ylim(yaxisparams[0])
        plt.yticks(yaxisparams[1])
       
    # X ticks
    plt.tick_params(
        axis='x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom='off',      # ticks along the bottom edge are off
        top='off') # labels along the bottom edge are off
    
    if grouplabel == 'auto':
        plt.tick_params(labelbottom='off')
    else:
        plt.xticks(range(1,nGroups+1), grouplabel)
        plt.tick_params(top='off')
    
    # Hide the right and top spines and set bottom to zero
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position('zero')
    
    
    if show_legend == 'within':
        if len(itemlabel) != barspergroup:
            print('Not enough item labels for legend!')
        else:
            legendbar = []
            legendtext = []
            for i in range(barspergroup):
                legendbar.append(barlist[i])
                legendtext.append(itemlabel[i])
            plt.legend(legendbar, legendtext, loc=legendloc)

    ax.set(ylabel='Mean pdp - notdistracted trials')
    #ax.set(ylabel='Percent distracted trials')
    ax.yaxis.label.set_size(14)      
#    fig.savefig('/Volumes/KPMSB352/Distraction photometry paper/BehaviourFigs/PDP_notdis_salvpcp_M.pdf', bbox_inches="tight") 

    return ax, barx, barlist, sclist
      
def setcolors(coloroption, colors, barspergroup, nGroups, data, paired_scatter = False):
            
    nColors = len(colors)
    
    if (paired_scatter == True) & (coloroption == 'within'):
        print('Not possible to make a Paired scatter plot with Within setting.')
        coloroption = 'same'
        
    if coloroption == 'within':
        if nColors < barspergroup:
            print('Not enough colors for this option! Reverting to one color.')
            coloroption = 'same'
        elif nColors > barspergroup:
            colors = colors[:barspergroup]
        coloroutput = [colors for i in data]
        coloroutput = list(chain(*coloroutput))
        
    if coloroption == 'between':
        if nColors < nGroups:
            print('Not enough colors for this option! Reverting to one color.')
            coloroption = 'same'
        elif nColors > nGroups:
            colors = colors[:nGroups]
        if paired_scatter == False:
            coloroutput = [[c]*barspergroup for c in colors]
            coloroutput = list(chain(*coloroutput))
        else:
            coloroutput = colors
            
    if coloroption == 'individual':
        if nColors < nGroups*barspergroup:
            print('Not enough colors for this color option')
            coloroption = 'same'
        elif nColors > nGroups*barspergroup:
            coloroutput = colors[:nGroups*barspergroup]
        else: 
            coloroutput = colors
    
    if coloroption == 'same':
        coloroutput = [colors[0] for x in range(len(data.flatten()))]

    return coloroutput

#### FUNCTIONS IN ORDER OF APPEARANCE IN DISTRACTION BEHAVIOUR ANALYSIS

'''
SUBSETTER KP
# Subsets data according to date, reads in dictionnary produced from metafile
# and subsets into variable based on date(s) and drug condition 
# if distraction day argument is given as True adds the distractor type 
# to the output lists for later processing 

'''

def subsetter(dictionary, dates, drug, dis=False, verbose=False):
    subset = []
    for ind, filename in enumerate(dictionary['MedFilenames']):
        path = medfolder + filename
        onsets, offsets, med_dis_times, dis_type = medfilereader(path, ['e', 'f', 'i', 'j'], remove_var_header = True)  # e onset, f offset

        if dis == True:
            if dictionary['Date'][ind] in dates and dictionary['Drug'][ind] == drug:
                subset.append([onsets, offsets, dis_type, dictionary['RatID'][ind]])
                
        elif dis==False:   
            if dictionary['Date'][ind] in dates and dictionary['Drug'][ind] == drug:
                subset.append([onsets, offsets, dictionary['RatID'][ind]])
            
        if verbose: #assumes true
            print('filename, or comment ...') 
    return subset
    
'''
LICKANALYSIS KP
# Takes lickdata from subset lists/dictionary
# produces 25 item dictionary for each rat / day 
# lick information on bursts, clusters(runs) etc. 

'''
def lickanalysis(lickdata, burstThreshold=0.25, runThreshold=10):
    analysis = []
    for lists in lickdata:
        lickon = lists[0]
        offset = lists[1]
        lick_analysis = lickCalc(lickon, offset, burstThreshold=burstThreshold, runThreshold=runThreshold)
        analysis.append(lick_analysis)
    return analysis


'''
GROUPED_LICKANALYSIS 

Takes list of dictionaries previously sorted by subsetter
Finds lick analysis information on bursts, clusters, intervals 
taken from individual lick analysis 
Runs need to be defined somewhere????
'''

def grouped_lickanalysis(groupdicts):

    all_n_bursts, all_n_runs, all_mean_IBI, all_mean_burst_length, \
        all_mean_IRI, all_mean_run_length = [], [], [], [], [], []
    for dictionary in groupdicts:     
      
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


''' Calculates distractors, distracted and modalities for dictionary of 
    rats by group for just distraction day only 
    
    Calculates a grouped percentage of each modality and how distracted 
    by that modality rats are on average (by group)
    
'''
    
def discalc_modalities(dictionary, modalitykey, ):
    percent_dis_whitenoise_group = []
    percent_dis_tone_group = []
    percent_dis_combined_group = []
    discalcgroup = []
    ## SAL MALES - DISTRACTION DAY ONLY - DISTRACTOR TYPE ANALYSIS INCLUDED
# Finds distracted or not (corrects for med slipping issue)
    for rat in dictionary:
        
        discalc = distractionCalc2(rat[0])
        distracted, notdistracted = distractedOrNot(discalc, rat[0])
      #  work out percentage and add this too 
        discalcgroup.append([distracted, notdistracted])
    
        dis_numeric = []
        ndis_numeric = []
    # Modality analysis - calculates which distractors contain different features (whitenoise, tone or combination)
    # Then works out on how many of these trials rats are distracted (individual) before creating a mean 
        for d in distracted:
            dis_numeric.append([rat[2][idx] for idx, val in enumerate(discalc) if val == d][0])
        for nd in notdistracted:
            ndis_numeric.append([rat[2][idx] for idx, val in enumerate(discalc) if val == nd][0])   
        # Makes the distracted trial types into integers 
        dis_numeric = [int(d) for d in dis_numeric]
        # Counts to work out percentages after finding how many are each modality 
        d_whitenoise_count = 0
        d_tone_count = 0
        d_combined_count = 0 
        
        dis_type_text = [] #labels the distypes with text labels and adds to the counts
        for d in dis_numeric:
            if d in modalitykey['whitenoise']:
                dis_type_text.append('whitenoise')
                d_whitenoise_count += 1
            elif d in modalitykey['tone']:
                dis_type_text.append('tone')
                d_tone_count += 1
            elif d in modalitykey['combined3']:
                dis_type_text.append('combined3')
                d_combined_count += 1 
        d_percent_white_noise = d_whitenoise_count / (len(dis_type_text))*100
        d_percent_tone = d_tone_count / (len(dis_type_text))*100
        d_percent_combined = d_combined_count / (len(dis_type_text))*100  
    
        # Non-distracted trials by modality 
        ndis_numeric = [int(d) for d in ndis_numeric]
        nd_whitenoise_count = 0
        nd_tone_count = 0
        nd_combined_count = 0 
        
        ndis_type_text = []
        for d in ndis_numeric:
            if d in modalitykey['whitenoise']:
                ndis_type_text.append('whitenoise')
                nd_whitenoise_count += 1
            elif d in modalitykey['tone']:
                ndis_type_text.append('tone')
                nd_tone_count += 1
            elif d in modalitykey['combined3']:
                ndis_type_text.append('combined3')
                nd_combined_count += 1 
                
    
        nd_percent_white_noise = nd_whitenoise_count / (len(ndis_type_text))*100
        nd_percent_tone = nd_tone_count / (len(ndis_type_text))*100
        nd_percent_combined =  nd_combined_count / (len(ndis_type_text))*100
        
        percent_distracted_whitenoise = d_whitenoise_count / (d_whitenoise_count + nd_whitenoise_count) *100
        percent_distracted_tone = d_tone_count / (d_tone_count + nd_tone_count) *100
        percent_distracted_combined = d_combined_count / (d_combined_count + nd_combined_count) *100  
        
        percent_dis_whitenoise_group.append(percent_distracted_whitenoise)
        percent_dis_tone_group.append(percent_distracted_tone)
        percent_dis_combined_group.append(percent_distracted_combined)
      
    mean_percent_WHITENOISE = np.mean(percent_dis_whitenoise_group) # the average percentage of JUST whitenoise trials that rats are distracted on 
    mean_percent_TONE = np.mean(percent_dis_tone_group)
    mean_percent_COMBINED = np.mean(percent_dis_combined_group)
    
    
    return discalcgroup, percent_dis_whitenoise_group, percent_dis_tone_group, \
            percent_dis_combined_group, mean_percent_WHITENOISE, mean_percent_TONE, \
            mean_percent_COMBINED


''' Prodcues times of distracted and not distracted as 2 lists
    takes a dictionary of grouped rat data 
'''

def disbygroup(dictionary):
    dis = []
    for rat in dictionary:
        
        discalc = distractionCalc2(rat[0])         
        distracted, notdistracted = distractedOrNot(discalc, rat[0])
        dis.append([distracted, notdistracted])
        
    return dis

def pdpbygroup(distractiondict, groupdict):
    ''' Distraction dict = discalc for the chosen group 
        groupdict is the whole disctionary on distraction 
        day from subsetter
    
    '''
    
    pdps_dis_group, med_pdps_dis_group, preDPs_dis_group, \
    pdps_notdis_group, med_pdps_notdis_group, preDPs_notdis_group = [],[],[],[],[],[]
    
    for index, rat in enumerate(distractiondict):
        pdps_dis = []
        preDPs_dis = []
        for distractorlick in rat[0]:
            
            if distractorlick in groupdict[index][0] and distractorlick != groupdict[index][0][-1]:
                lick_index = groupdict[index][0].index(distractorlick) 
                lick_index_plus1 = lick_index+1
                lick_index_minus3 = lick_index-3
                distracted_PDP = groupdict[index][0][lick_index_plus1] - groupdict[index][0][lick_index]
                distracted_preDP = groupdict[index][0][lick_index] - groupdict[index][0][lick_index_minus3]
            
            pdps_dis.append(distracted_PDP)
            preDPs_dis.append(distracted_preDP)
        pdps_dis_group.append(pdps_dis)
        med_pdps_dis_group.append(np.mean(pdps_dis))
        preDPs_dis_group.append(preDPs_dis)
    
    
    # Not distracted PDPs 
    
    for index, rat in enumerate(distractiondict):
        pdps_notdis = []
        preDPs_notdis = []
        for notdistractedlick in rat[1]:
            if notdistractedlick in groupdict[index][0] and notdistractedlick != groupdict[index][0][-1]:
                lick_index = groupdict[index][0].index(notdistractedlick) 
                lick_index_plus1 = lick_index+1
                lick_index_minus3 = lick_index-3
                notdistracted_PDP = groupdict[index][0][lick_index_plus1] - groupdict[index][0][lick_index]
                notdistracted_preDP = groupdict[index][0][lick_index] - groupdict[index][0][lick_index_minus3]
            
            pdps_notdis.append(notdistracted_PDP)
            preDPs_notdis.append(notdistracted_preDP)
        pdps_notdis_group.append(pdps_notdis)
        med_pdps_notdis_group.append(np.mean(pdps_notdis))
        preDPs_notdis_group.append(preDPs_notdis)
    
    return pdps_dis_group, med_pdps_dis_group, preDPs_dis_group, \
        pdps_notdis_group, med_pdps_notdis_group, preDPs_notdis_group
        

def percentdisgroup(distractiondict):
    ''' Discalc_sal_M == distractiondict '''
    
    percent_dis_group = []
    for rat in distractiondict: 
        percentage = len(rat[0]) / (len(rat[0])+len(rat[1])) * 100
        percent_dis_group.append(percentage)
    return percent_dis_group
        