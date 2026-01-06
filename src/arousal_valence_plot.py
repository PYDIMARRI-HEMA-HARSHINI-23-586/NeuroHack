import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
data = sio.loadmat("data/DREAMER.mat")
dreamer = data["DREAMER"][0, 0]
Data = dreamer["Data"]

valence_all = []
arousal_all = []

# Collect VAD scores
for subj in range(Data.shape[1]):
    subject = Data[0, subj][0, 0]
    valence_all.append(subject["ScoreValence"].flatten())
    arousal_all.append(subject["ScoreArousal"].flatten())

valence_all = np.concatenate(valence_all)
arousal_all = np.concatenate(arousal_all)

# Plot Arousal–Valence space
plt.figure(figsize=(6, 6))
plt.scatter(valence_all, arousal_all, alpha=0.6)

plt.xlabel("Valence")
plt.ylabel("Arousal")
plt.title("Arousal–Valence Emotional Space (DREAMER Dataset)")
plt.xticks(range(1, 6))
plt.yticks(range(1, 6))
plt.grid(True)

plt.savefig("outputs/arousal_valence_plot.png", dpi=300, bbox_inches="tight")
plt.show(block=True)

