import numpy as np
import matplotlib.pyplot as plt

# Load features
data = np.load("data/eeg_features_valence.npz")
X = data["X"]   # (samples, 42)
y = data["y"]   # 0 = Low Valence, 1 = High Valence

n_channels = 14

# Reshape to (samples, channels, bands)
X_reshaped = X.reshape(-1, n_channels, 3)

# Average across channels → band-level features
band_power = X_reshaped.mean(axis=1)
# shape: (samples, 3)

theta = band_power[:, 0]
alpha = band_power[:, 1]
beta  = band_power[:, 2]

# Split by class
low_valence = band_power[y == 0]
high_valence = band_power[y == 1]

# Plot
plt.figure(figsize=(10, 4))

plt.boxplot(
    [low_valence[:, 0], high_valence[:, 0],
     low_valence[:, 1], high_valence[:, 1],
     low_valence[:, 2], high_valence[:, 2]],
    labels=[
        "Theta (Low)", "Theta (High)",
        "Alpha (Low)", "Alpha (High)",
        "Beta (Low)",  "Beta (High)"
    ],
    patch_artist=True
)

plt.title("EEG Band Power Comparison: Low vs High Valence")
plt.ylabel("Band Power")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
