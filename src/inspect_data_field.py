import scipy.io as sio

data = sio.loadmat("data/DREAMER.mat")
dreamer = data["DREAMER"][0,0]

data_field = dreamer["Data"]

print("Type of Data field:", type(data_field))
print("Shape of Data field:", data_field.shape)
