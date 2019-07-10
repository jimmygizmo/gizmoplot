#! /usr/bin/env python3

from matplotlib import pyplot as plt
# pyplot is a collection of command style functions which make matplotlib work
# like MATLAB. If you want more flexibility, use the OO interface.

agex = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

devy = [38496, 42000, 46752, 49320, 53200, 56000,
        62316, 64928, 67317, 68748, 73752]

pydevy = [45372, 48876, 53850, 57287, 63016, 65998,
          70003, 70000, 71496, 75370, 83640]

jsdevy = [37810, 43515, 46823, 49293, 53437, 56373,
          62375, 66674, 68745, 68746, 74583]

# Using Matplot format string (less desireable.) Single character
# component format codes can be in any position it seems.
# Format strings documented (halfway down page) here:
# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html
fmt_dev = '.k--'  # Point marker, Black, dashed line
fmt_pydev = '.b-'  # Point marker, Blue, solid line
# Using the format strings:
# plt.plot(agex, devy, fmt_dev, label='All Devs')
# plt.plot(agex, pydevy, fmt_pydev, label='Python Devs')

plt.plot(agex, devy, color='#444444', linestyle='--',
         label='All Devs')

plt.plot(agex, pydevy, color='#5a7d9a',
         label='Python')

plt.plot(agex, jsdevy, color='#adad3b',
         label='JavaScript')

plt.xlabel('Age (years)')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')

# Put color-matched legend in upper-left corner. Order of plot calls must
# match order of legend list.
# plt.legend(['All Devs', 'Python'])
# Or:
plt.legend()  # No args when you have label attrs in the above plot()s

# When using legend attrs in each plot() you just call legend() with no args
# and the legend appears the same as the legend(['a', 'b']) technique.

plt.show()

