#!/usr/bin/env python
# coding: utf-8

# Applications of Accelerators Lecture
# Python Exercise 3
# Tugce Sirkecioglu 3301159
# December 2021

# From the accelerator department, you received some data (see the attached data file: 2016-07-11_ipm_data.txt) from an ionisation beam profile monitor (IPM). Read the file and plot it in blue color on a black grid background. The mark the maximum with a red dot! Code and plot (PNG) as usual on GitHUB.

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('2016-07-11_ipm_data.txt', 'float')

plt.plot(data, color='blue', linestyle='solid', linewidth = 0.5)

plt.grid(axis='both', color='black', linestyle='-', linewidth=0.1)

ymax = max(data)
xpos = np.where(data == ymax)
xmax = xpos

plt.plot( xmax, ymax, 'ro', markersize=2.5)
 
plt.savefig("2016-07-11_ipm_data_plot.png", dpi=250)
