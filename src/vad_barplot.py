import scipy.io as sio
import numpy as np
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

# Compute mean values
means = [
    np.mean(valence_all),
    np.mean(arousal_all),
    np.mean(dominance_all)
]

labels = ["Valence", "Arousal", "Dominance"]

# Plot bar chart
plt.figure(figsize=(6, 4))
plt.bar(labels, means)
plt.ylabel("Mean Rating")
plt.title("Mean Valence, Arousal, and Dominance Ratings (DREAMER Dataset)")
plt.ylim(0, 5)
plt.grid(axis="y")

plt.show()
