import scipy.io as sio

data = sio.loadmat("data/DREAMER.mat")
dreamer = data["DREAMER"][0,0]
Data = dreamer["Data"]

subject0 = Data[0,0][0,0]

EEG_cell = subject0["EEG"]

# Unwrap MATLAB cell
EEG_unwrapped = EEG_cell[0,0]

print("Unwrapped EEG type:", type(EEG_unwrapped))
print("Unwrapped EEG shape:", EEG_unwrapped.shape)
