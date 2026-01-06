import scipy.io as sio

data = sio.loadmat("data/DREAMER.mat")
dreamer = data["DREAMER"][0,0]
Data = dreamer["Data"]

# Pick FIRST subject
subject0 = Data[0, 0]

print("Type of subject entry:", type(subject0))
print("Shape of subject entry:", subject0.shape)
print("Fields inside subject:")
print(subject0.dtype)
