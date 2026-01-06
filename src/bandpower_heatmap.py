import numpy as np
import matplotlib.pyplot as plt

# Load extracted features
data = np.load("data/eeg_features_valence.npz")
X = data["X"]   # shape: (samples, features)
y = data["y"]   # labels (not used here)

# Feature layout:
# 14 channels × 3 bands = 42 features
# Order assumed: [Ch1_theta, Ch1_alpha, Ch1_beta, ..., Ch14_beta]

n_channels = 14
bands = ["Theta (4–8 Hz)", "Alpha (8–13 Hz)", "Beta (13–30 Hz)"]

# Reshape: (samples, channels, bands)
X_reshaped = X.reshape(-1, n_channels, 3)

# Average across all samples
mean_band_power = X_reshaped.mean(axis=0).T
# Shape now: (bands, channels)

# Plot heatmap
plt.figure(figsize=(12, 4))
im = plt.imshow(mean_band_power, aspect="auto", cmap="viridis")

plt.colorbar(im, label="Average Band Power")
plt.xticks(range(n_channels), [f"EEG{i+1}" for i in range(n_channels)], rotation=45)
plt.yticks(range(3), bands)

plt.title("Channel-wise Average EEG Band Power")
plt.xlabel("EEG Channels")
plt.ylabel("Frequency Bands")

plt.tight_layout()
plt.show()
