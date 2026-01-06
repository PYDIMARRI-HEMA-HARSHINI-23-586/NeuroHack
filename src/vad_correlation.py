import scipy.io as sio
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = sio.loadmat("data/DREAMER.mat")
dreamer = data["DREAMER"][0, 0]
Data = dreamer["Data"]

valence_all = []
arousal_all = []
dominance_all = []

# Collect VAD scores
for subj in range(Data.shape[1]):
    subject = Data[0, subj][0, 0]
    valence_all.append(subject["ScoreValence"].flatten())
    arousal_all.append(subject["ScoreArousal"].flatten())
    dominance_all.append(subject["ScoreDominance"].flatten())

valence_all = np.concatenate(valence_all)
arousal_all = np.concatenate(arousal_all)
dominance_all = np.concatenate(dominance_all)

# Create DataFrame
vad_df = pd.DataFrame({
    "Valence": valence_all,
    "Arousal": arousal_all,
    "Dominance": dominance_all
})

# Correlation matrix
corr = vad_df.corr(method="pearson")
print("Correlation Matrix:\n", corr)

# Plot heatmap
plt.figure(figsize=(5, 4))
sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Between Valence, Arousal, and Dominance")
plt.show()
