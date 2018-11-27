from deap import creator, base, tools, algorithms
from __future__ import absolute_import
import random
import numpy as np
from deap import tools
import pandas as pd
from sklearn.model_selection import cross_val_score
import warnings
warnings.filterwarnings('ignore')
from FeatureGA import FeatureSelectionGA

main_data=pd.read_csv(r"agg_data.csv",sep=',',encoding="utf-8",error_bad_lines=False,low_memory = False)
print(main_data.shape)

features=['ECG_Peaks','ECG_Average_Amplitude', 'ECG_Differ_Mean', 'ECG_Resting','EMG_peaks', 'EMG_Average_Amplitude',
          'EMG_Differ_Mean', 'RESP_peak', 'RESP_Average_Amplitude','RESP_Differ_Mean','TEMP',
          'BVP_peak', 'BVP_Average_Amplitude','BVP_Differ_Mean','Mean_ACC_X', 'Mean_ACC_Y', 'Mean_ACC_Z', 'SD_ACC_X', 'SD_ACC_Y',
           'SD_ACC_Z', 'MAX_ACC_X', 'MAX_ACC_Y', 'MAX_ACC_Z', 'MIN_ACC_X', 'MIN_ACC_Y', 'MIN_ACC_Z', 'X_Y_CORR', 'Y_Z_CORR',
          'X_Z_CORR', 'KURT_X','KURT_Y', 'KURT_Z', 'SKEW_X', 'SKEW_Y', 'SKEW_Z', 'FFT_X', 'FFT_Y','FFT_Z', 'CREST_FACTOR_X',
          'CREST_FACTOR_Y', 'CREST_FACTOR_Z']
labels=['Label']

feat=agg_data[features]
labe=agg_data[labels]
