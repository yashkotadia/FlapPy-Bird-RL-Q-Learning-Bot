import pickle
import random
from matplotlib import pyplot as plt
import pandas as pd

with open('scores.pkl', 'rb') as f:
	Q = pickle.load(f)

df  = pd.DataFrame(Q)
rm = df.rolling(window=1000).mean()
rs = df.rolling(window=1000).std()
upper_band = rm + 2*rs
lower_band = rm - 2*rs
plt.figure(figsize=(15,10))
plt.plot(df,'g.',rm,'b',upper_band,'r')
plt.title('Scores')
plt.show()