#See README.md for references > Credits and References >Program : plottask.py
# Weekly task week 8


import numpy as np
import matplotlib.pyplot as plt


mean = 5
standard_deviation = 2
number_of_values = 1000

np.random.seed(1) 

values = np.random.normal(mean, standard_deviation, number_of_values)




plt.hist((values), color='blue', edgecolor='black')
plt.title('Histogram of a normal distribution of a 1000 values ')
plt.xlabel('Values')
plt.ylabel('Frequency')

plt.show()
