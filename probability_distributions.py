''' probability_distributions
Demonstrate generating and visualizing probability distribution functions.
'''

import matplotlib.pyplot as plt # Import matplotlib.pylot package as plt
import numpy as np # Import numpy package as np
from icecream import ic

#  Settings
binwidth = 0.5 # width of each data point collection group
n_samples_x = 1000 # number of samples on x-axis
n_samples_y = 1000 # number of samples on y-axis

x = np.random.normal(0, 1, size=(n_samples_x,)) # x is a variable that equals a random point on x-axis
y = np.random.normal(0, 1, size=(n_samples_y,)) # y is a variable that equals a random point on y-axis

x_bins = np.arange(-4.5, 4.5, binwidth) # x_bins is a variable that has a range of -4.5, 4.5 and bin width of 0.5
val_counts_x, bin_edges_x = np.histogram(x, x_bins) # All points inside of the x_bins edges create histogram bar with x_bins width
val_counts_y, bin_edges_y = np.histogram(y, x_bins) # All 

fig, ax = plt.subplots() # creating the figure from matplot
plt.xlabel('value') # labeling x axis
plt.ylabel('counts') # labeling y axis
plot_x = val_counts_x.astype(float) #
plot_y = val_counts_y.astype(float)
plt.bar(
    bin_edges_x[:-1], plot_x, edgecolor='#b24342', color=[], width=.3, 
    label='x', linewidth=2, alpha=0.5)
plt.bar(
    bin_edges_y[:-1], plot_y, edgecolor='#6e7aaa', color=[], width=.3, 
    label='y', linewidth=2, alpha=0.5)
plt.plot(bin_edges_x[:-1], plot_x, color='#b24342')
plt.plot(bin_edges_y[:-1], plot_y, color='#6e7aaa')
plt.legend()
plt.savefig('/Users/henrylord/Documents/EV228_Figures//distribution.pdf') 