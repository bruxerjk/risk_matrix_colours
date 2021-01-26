"""
Create Matplotlib colour map gradient and export as a list of hex code colours

Developed for risk matrix color coding, a generalized plot example included

@author: Jacob Bruxer
"""
import numpy as np

import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import rgb2hex

'''
OPTIONS:

    The script will create a continuous colour gradient first, this can
    be modified by modifying the transition values and colours in CMAP_COLOURS

    Next, a list of length N_COLOURS is drawn from the continuous gradient.
'''

# these values, colours could be modified as desired
CMAP_COLOURS = [(0.0, '#0f0'),  # green (must start at 0)
                (0.10, '#0f0'), # green (10%)
                (0.3, '#ff0'), # yellow (25%)
                (0.50, '#ffa500'), # orange (50%)
                (.7, '#EA0003'), # red ()
                (0.9, '#65007a'), # purple (90%)
                (1.0, '#65007a')  # purple (must end at 1)
                ]

# output list will have this many colors
N_COLOURS = 100

'''END OF OPTIONS'''

def create_colormap(name, cmap_colours):

    '''Create a color map with name and customized value, color arrays'''

    cmap = mpl.colors.LinearSegmentedColormap.from_list(name, cmap_colours)

    return cmap


def create_risk_matrix(cmap, increments):

    '''Plots a 1-dimensional color map as a 2-dimensional risk matrix'''

    step = 100/(increments-1)
    x = np.arange(0, 100+step, step)
    y = np.arange(0, 100+step, step)
    X, Y = np.meshgrid(x, y)
    h=0
    k=0
    Z = ((X-h)**2 + (Y-k)**2)**0.5 / (2**0.5)  # circle equation, normalized

    fig, ax = plt.subplots(1, 1)

    im = ax.imshow(Z, interpolation='nearest', origin='lower', cmap=cmap,
                   extent = [0,100,0,100])
    ax.set_title(f'N_COLOURS = {N_COLOURS}')
    ax.set_xlabel('impact')
    ax.set_ylabel('probability')

    fig.colorbar(im, ax=ax)

    return fig, ax


# specify name and colour increments as (value, colour) pairs for colour map
name = 'Impact Zones'
cmap = create_colormap(name, CMAP_COLOURS)


# the number of increments determines how many colors to list
# and how the gradient is plotted
increments = N_COLOURS  # increase increments to make more course

step = 100/(increments-1)

# convert cmap of rgb colours to list of hex colours and print
colours = [rgb2hex(cmap(x/100)) for x in np.arange(0,100+step,step)]

print(f'Gradient with {len(colours)} colours:')
print(colours)

# plot the results and see how it looks
fig, ax = create_risk_matrix(cmap, increments)
plt.show()