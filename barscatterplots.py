#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 07:52:50 2018

@author: u1490431
"""

# Bar scatter plots 


distraction_modality = np.empty((3,), dtype=np.object)
distraction_modality[0] = np.array(percent_dis_tone_sal_M)
distraction_modality[1] = np.array(percent_dis_whitenoise_sal_M)
distraction_modality[2] = np.array(percent_dis_combined_sal_M)

barscatter(distraction_modality, grouplabel=['tone', 'whitenoise', 'combined'])

# ANOVA - is there an effect of distrator modality? 
