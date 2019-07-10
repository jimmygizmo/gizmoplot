#! /usr/bin/env python3

from matplotlib import pyplot as plt
# pyplot is a collection of command style functions which make matplotlib work
# like MATLAB. If you want more flexibility, use the OO interface.

devx = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

devy = [38496, 42000, 46752, 49320, 53200, 56000,
        62316, 64928, 67317, 68748, 73752]

pydevy = [45372, 48876, 53850, 57287, 63016, 65998,
          70003, 70000, 71496, 75370, 83640]

plt.plot(devx, devy, label='All Devs')
plt.plot(devx, pydevy, label='Python Devs')

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

