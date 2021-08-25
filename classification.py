from collections import ChainMap
from functools import reduce
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
import pandas as pd
from data import data_class
from feature_reduction import pca
from normalization import normalisasi
import numpy as np


class svm_classsifier:
    def __init__(self, feature):

        self.feature = np.array(feature)
        transposed_feature = self.feature.transpose()
        normalized = []
        for pemotongan in range(len(transposed_feature)):
            normalized.append(normalisasi(transposed_feature[pemotongan]))
        normalized = np.array(normalized).transpose()
        self.feature = normalized
        self.full_feature = self.feature

    def trim_data(self, pemotongan):
        for i in range(pemotongan):
            current_len = self.feature.shape[1]
            for j in range(4, 0, -1):
                self.feature = np.delete(self.feature, int(current_len * j / 4) - 1, 1)

    def train_and_test(self, pemotongan, gamma, C):
        import time
        start = time.time()
        self.trim_data(pemotongan)
        clf = svm.SVC(kernel='rbf', gamma=gamma, C=C, decision_function_shape='ovo')  # RBF Kernel
        kf = KFold(n_splits=4)
        accuracy = []
        pred_array = []
        for train, test in kf.split(self.feature):
            clf.fit(np.array(self.feature)[train], np.array(data_class)[train])
            y_pred = clf.predict(np.array(self.feature)[test])
            pred_array.append(y_pred)
            accuracy.append(metrics.accuracy_score(np.array(data_class)[test], y_pred))
        end = time.time()
        index = np.argmax(accuracy)
        import collections
        count = collections.Counter(pred_array[index])
        import pandas as pd
        fold_id = [i for i in range(1, 5)]
        hype = []
        angry = []
        relax = []
        gloom = []
        for i in range(4):
            fold_counter = collections.Counter(pred_array[i])
            hype.append(count["Hype"])
            angry.append(count["Angry"])
            relax.append(count["Relax"])
            gloom.append(count["Gloom"])
        dict = {'Fold': fold_id, 'Accuracy': accuracy, 'Hype': hype, "Relax": relax, "Angry": angry, "Gloom": gloom}
        df = pd.DataFrame(dict)
        df.to_csv('K-Fold_Result.csv')
        self.feature = self.full_feature
        return accuracy[index], (end - start), count["Hype"], count["Angry"], count["Relax"], count["Gloom"], index+1