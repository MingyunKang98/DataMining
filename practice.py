import pandas as pd
import numpy as np

a  = np.arange(0, 200 ,3)
print(a)

a = pd.DataFrame(a)
print(a)

print(a.iloc[3:8])
print("==================")
print(a.loc[3:8])
print("==================")
print(a[3:8])