#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 07:52:50 2018

@author: u1490431
"""

# Bar scatter plots 


#distraction_modality = np.empty((3,), dtype=np.object)
#distraction_modality[0] = np.array(percent_dis_tone_sal_M)
#distraction_modality[1] = np.array(percent_dis_whitenoise_sal_M)
#distraction_modality[2] = np.array(percent_dis_combined_sal_M)
#
#barscatter(distraction_modality, grouplabel=['tone', 'whitenoise', 'combined'])
'''
# ANOVA - is there an effect of distrator modality? 
distraction_percents = np.empty((5,), dtype=np.object)
distraction_percents[0] = np.array(percent_dis_modelled_sal_M)
distraction_percents[1] = np.array(percent_dis_dis_sal_M)
distraction_percents[2] = np.array(percent_dis_hab1_sal_M)
distraction_percents[3] = np.array(percent_dis_hab2_sal_M)
distraction_percents[4] = np.array(percent_dis_amph_sal_M)


barscatter(distraction_percents, grouplabel=['mod', 'distraction', 'hab1', 'hab2', 'amph'])
'''

'''
#### 
distraction_sasVpcp = np.empty((2,), dtype=np.object)
distraction_sasVpcp[0] = np.array(percent_dis_dis_sal_M)
distraction_sasVpcp[1] = np.array(percent_dis_dis_pcp_M)


barscatter(distraction_sasVpcp, grouplabel=['saline', 'pcp']) #grouplabel=['mod', 'distraction', 'hab1', 'hab2', 'amph'])


### females (n = 11, 5-6 per group)
distraction_salVpcp_F = np.empty((2,), dtype=np.object)
#distraction_salVpcp_F[0] = np.array(percent_dis_dis_sal_F)
#distraction_salVpcp_F[1] = np.array(percent_dis_hab1_sal_F)
distraction_salVpcp_F[0] = np.array(percent_dis_dis_pcp_F)
distraction_salVpcp_F[1] = np.array(percent_dis_hab1_pcp_F)

barscatter(distraction_salVpcp_F, grouplabel=['pcp dis', 'pcp hab'])

'''
## Use mean PDPs  - median gives same result for males and females too 

# females 

dis_pdps_median = np.empty((2,), dtype=np.object)
dis_pdps_median[0] = np.array(med_pdps_dis_sal_M)
dis_pdps_median[1] = np.array(med_pdps_dis_pcp_M)

#dis_pdps_median[2] = np.array(med_pdps_dis_sal_F)
#dis_pdps_median[3] = np.array(med_pdps_dis_pcp_F)


notdis_pdps_median = np.empty((2,), dtype=np.object)
notdis_pdps_median[0] = np.array(med_pdps_notdis_sal_M)
notdis_pdps_median[1] = np.array(med_pdps_notdis_pcp_M)

#notdis_pdps_median[2] = np.array(med_pdps_notdis_sal_F)
#notdis_pdps_median[3] = np.array(med_pdps_notdis_pcp_F)

barscatter(notdis_pdps_median, grouplabel=['sal', 'pcp'])

#barscatter(notdis_pdps_median)

















