#!/usr/bin/python2

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import sys

# This is for nice graphics, using the same styling as the latex template
# and using a sane width-height ratio and so on.

fig_width_pt = 319.0                    # Get this from LaTeX using \showthe\columnwidth
inches_per_pt = 1.0/72.27               # Convert pt to inches
golden_mean = (sp.sqrt(5)-1.0)/2.0      # Aesthetic ratio
fig_width = fig_width_pt*inches_per_pt  # width in inches
fig_height =fig_width*golden_mean       # height in inches
fig_size = [fig_width,fig_height]
params = {'backend': 'pdf',
          'axes.labelsize': 10,
          'text.fontsize': 10,
          'legend.fontsize': 9,
          'xtick.labelsize': 9,
          'ytick.labelsize': 9,
          'text.usetex': True,
          'figure.figsize': fig_size}
mpl.rcParams.update(params)


# plot something
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.xlabel('Some y-axis things')

# plot the beautiful thing.
plt.savefig('../../content/figures/example.pdf', bbox_inches='tight')
