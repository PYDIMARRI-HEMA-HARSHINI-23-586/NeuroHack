import scipy.io as sio

data = sio.loadmat("data/DREAMER.mat")
dreamer = data["DREAMER"][0,0]
Data = dreamer["Data"]

subject0 = Data[0,0][0,0]
EEG_struct = subject0["EEG"][0,0]

baseline = EEG_struct["baseline"]

print("baseline type:", type(baseline))
print("baseline shape:", baseline.shape)

b00 = baseline[0,0]
print("\nbaseline[0,0] type:", type(b00))

# If it's a struct, print fields
if hasattr(b00, "dtype"):
    print("baseline[0,0] dtype:", b00.dtype)

# Try ONE more unwrap safely
try:
    b000 = b00[0,0]
    print("\nbaseline[0,0][0,0] type:", type(b000))
    if hasattr(b000, "shape"):
        print("baseline[0,0][0,0] shape:", b000.shape)
except Exception as e:
    print("Error while unwrapping:", e)
