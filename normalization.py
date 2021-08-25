# untuk normalisasi fitur mfcc
import numpy as np
a=0
b=1
def normalisasi(signal):
    normalized = []
    sig_min = min(signal)
    sig_max = max(signal)
    for i in range(len(signal)):
        normalized.append((((signal[i] - sig_min) / (sig_max - sig_min)) * (b - a)) + a)
    return np.array(normalized)