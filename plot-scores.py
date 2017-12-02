import pickle
import random
from matplotlib import pyplot as plt
import pandas as pd

# Open the scores file and load scores
with open('scores.pkl', 'rb') as f:
	Q = pickle.load(f)

df  = pd.DataFrame(Q) # Create a dataframe of scores
rm = df.rolling(window=500).mean() # Calculate rolling mean
rs = df.rolling(window=500).std() # Calculate rolling standard deviation
upper_band = rm + rs # The upper band in the graph to show how much scores deviate from mean

# Plotting the graph using pyplot
plt.semilogy(df,'g.',label='Scores')
plt.semilogy(rm,'b',label='Mean')
plt.semilogy(upper_band,'r',label='Standard Deviation')
plt.legend()
plt.grid(True, which='both')
plt.title('Training Curve')
plt.show()
