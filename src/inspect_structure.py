import scipy.io as sio

data = sio.loadmat("data/DREAMER.mat")
dreamer = data["DREAMER"]

print("Type:", type(dreamer))
print("Shape:", dreamer.shape)

dreamer_struct = dreamer[0,0]

print("Fields inside DREAMER:")
print(dreamer_struct.dtype)
