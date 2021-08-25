import pandas as pd
import matplotlib.pyplot as plt
import scipy.io.wavfile
import numpy as np
from python_speech_features import mfcc as mfcc_extract
from sklearn.decomposition import PCA
import sys

#import data

class mfcc:
    def __init__(self,directory):
        self.directory = directory
        self.feature = []
    
    def normalisasi(self,signal):
        a=-1
        b=1
        normalized = []
        sig_min = min(signal)
        sig_max = max(signal)
        for i in range(len(signal)):
            normalized.append((((signal[i] - sig_min) / (sig_max - sig_min)) * (b - a)) + a)
        return np.array(normalized)

    def get_feature(self, signal):
        mfcc_feature = mfcc_extract(signal, samplerate=128, winlen=1, winstep=0.5,
                            nfft=128, lowfreq=0, highfreq=64, preemph=0, winfunc=np.hamming)

        if len(mfcc_feature) == 0:
            sys.stder, "ERROR: ",len(signal)
        return mfcc_feature
    
    def feature_extract(self, signal):
        normalized = self.normalisasi(signal)
        mfcc_feature = self.get_feature(normalized)
        feature_mean = np.mean(mfcc_feature, axis = 0)
        return feature_mean
    
    def extract(self):
        print("Extracting Feature")
        import time
        x = []
        # x[subjek][data][trial][channel]
        print("Importing Data")
        for i in range(1,33):
            if i < 10:
                x.append(pd.read_pickle(self.directory+'/s0'+str(i)+'.dat'))
            else:
                if i == 12:
                    continue
                x.append(pd.read_pickle(self.directory+'/s'+str(i)+'.dat'))
        import matplotlib.pyplot as plt
        start = time.time()
        for i in range(len(x)):
            for j in range(len(x[i]['data'])):
                temp = []
                temp.append(self.feature_extract(x[i]['data'][j][20]))
                temp.append(self.feature_extract(x[i]['data'][j][25]))
                temp.append(self.feature_extract(x[i]['data'][j][7]))
                temp.append(self.feature_extract(x[i]['data'][j][1]))
                self.feature.append(np.concatenate((temp[0],temp[1],temp[2],temp[3])))
        end = time.time()
        return self.feature, (end - start)

    
