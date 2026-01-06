import scipy.io as sio

data = sio.loadmat("data/DREAMER.mat")

print("Keys in .mat file:")
for k in data.keys():
    print(k)
