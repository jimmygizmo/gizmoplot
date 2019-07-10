#! /usr/bin/env python3

from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

agex = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
devy = [38496, 42000, 46752, 49320, 53200, 56000,
        62316, 64928, 67317, 68748, 73752]
# pydevy = [45372, 48876, 53850, 57287, 63016, 65998,
#           70003, 70000, 71496, 75370, 83640]
# jsdevy = [37810, 43515, 46823, 49293, 53437, 56373,
#           62375, 66674, 68745, 68746, 74583]

# plt.plot(agex, pydevy, color='#5a7d9a', linewidth=3,
#          label='Python')

# plt.plot(agex, jsdevy, color='#adad3b', linewidth=3,
#          label='JavaScript')

plt.plot(agex, devy, color='#444444', linestyle='--',
         label='All Devs')

plt.xlabel('Age (years)')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')

plt.legend()
plt.tight_layout()
#plt.savefig('plot.png')

plt.show()

