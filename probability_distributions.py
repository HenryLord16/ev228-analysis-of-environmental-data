''' probability_distributions
Demonstrate generating and visualizing probability distribution functions.
'''
import matplotlib.pyplot as plt
import numpy as np

#  Settings
binwidth = 0.5
n_samples_x = 1000
n_samples_y = 1000

x = np.random.normal(0, 1, size=(n_samples_x,))
y = np.random.normal(0, 1, size=(n_samples_y,))

x_bins = np.arange(-4.5, 4.5, binwidth)
val_counts_x, bin_edges_x = np.histogram(x, x_bins)
val_counts_y, bin_edges_y = np.histogram(y, x_bins)

fig, ax = plt.subplots()
plt.xlabel('value')
plt.ylabel('counts')
plot_x = val_counts_x.astype(float)
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
plt.savefig('/Users/danielhueholt/Documents/Figures/ev228_fig/distribution.pdf')