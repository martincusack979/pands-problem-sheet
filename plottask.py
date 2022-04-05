# Week 8 task

# Author: Martin Cusack

# Write program called plottask.py displaying plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on one set of axes.

from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
xPoints = np.array(range(0,4))
fPoints = xPoints                                   # f(x)=x : each entry equal to x
gPoints = xPoints * xPoints                         # g(x)=x2 : square each entry
hPoints = xPoints * xPoints * xPoints               # h(x)=x3 : cube each entry
plt.scatter(fPoints, gPoints, hPoints, color = "r")  # create scatter plot
plt.title("Week 8 Task")                            # add title
plt.xlabel("X axis")                                # add label to X Axis
plt.show()
plt.savefig('fig1.png')