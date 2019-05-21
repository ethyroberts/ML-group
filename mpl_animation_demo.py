#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 13:53:46 2019

@author: ethan
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

plt.ioff()

n = 100
x = np.linspace(0, 4*np.pi, n)

fig = plt.figure()
ax = fig.add_subplot(111)

artist_list = []
for i in range(n):
    artist = []
    artist0 = ax.plot(x[0:i], np.cos(x[0:i]), c='C0')[0]
    artist1 = ax.plot(x[0:i], np.sin(x[0:i]), c='C1')[0]
    artist.append(artist0)
    artist.append(artist1)
    artist_list.append(artist)

delay_end = 300
for i in range(delay_end):
    artist_list.append(artist)

FFwriter = animation.FFMpegWriter(fps=30)

my_ani = animation.ArtistAnimation(fig, artist_list)
my_ani.save('first.mp4', writer=FFwriter)