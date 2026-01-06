import numpy as np
import matplotlib.pyplot as plt

# Load saved features
data = np.load("data/eeg_features_valence.npz")

X = data["X"]   # shape: (samples, 42)
y = data["y"]   # shape: (samples,)

"""
Feature layout:
[Theta_ch1..14 | Alpha_ch1..14 | Beta_ch1..14]
"""

# Split bands
theta = X[:, 0:14]
alpha = X[:, 14:28]
beta  = X[:, 28:42]

# Mean band power per sample
theta_mean = theta.mean(axis=1)
alpha_mean = alpha.mean(axis=1)
beta_mean  = beta.mean(axis=1)

# Separate classes
low_valence = y == 0
high_valence = y == 1

band_means = {
    "Theta": [theta_mean[low_valence].mean(), theta_mean[high_valence].mean()],
    "Alpha": [alpha_mean[low_valence].mean(), alpha_mean[high_valence].mean()],
    "Beta":  [beta_mean[low_valence].mean(),  beta_mean[high_valence].mean()],
}

# Plot
labels = ["Low Valence", "High Valence"]
x = np.arange(len(labels))
width = 0.25

plt.figure(figsize=(8,5))
plt.bar(x - width, band_means["Theta"], width, label="Theta (4–8 Hz)")
plt.bar(x, band_means["Alpha"], width, label="Alpha (8–13 Hz)")
plt.bar(x + width, band_means["Beta"], width, label="Beta (13–30 Hz)")

plt.xticks(x, labels)
plt.ylabel("Mean Band Power")
plt.title("Band Power Trends Across Valence States")
plt.legend()
plt.tight_layout()
plt.show()
