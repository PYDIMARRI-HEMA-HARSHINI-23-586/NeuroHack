import scipy.io as sio

data = sio.loadmat("data/DREAMER.mat")
dreamer = data["DREAMER"][0,0]
Data = dreamer["Data"]

subject0 = Data[0,0][0,0]
EEG_cell = subject0["EEG"]
EEG_struct = EEG_cell[0,0]

print("EEG struct type:", type(EEG_struct))
print("EEG struct dtype:")
print(EEG_struct.dtype)
