import pandas as pd

# feature = pd.read_csv("feature_wo_pca_6 Channel.csv", header = None)
threshold = 4

data = pd.read_csv('participant_ratings_wo_12.csv')
data_class = []
for i in range(len(data['Valence'])):
    if data['Valence'][i]<threshold and data['Arousal'][i]<threshold:
        data_class.append('Gloom')
    elif data['Valence'][i]<threshold and data['Arousal'][i]>=threshold:
        data_class.append('Angry')
    elif data['Valence'][i]>=threshold and data['Arousal'][i]<threshold:
        data_class.append('Relax')
    elif data['Valence'][i]>=threshold and data['Arousal'][i]>=threshold:
        data_class.append('Hype')