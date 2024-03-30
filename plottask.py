#See README.md for references > Credits and References >Program : plottask.py
# Weekly task week 8

#1: Impot libraries.
import numpy as np
import matplotlib.pyplot as plt


#2: Get the data to plot the histogram.
# Set the mean, standard deviation and the number of values.
mean = 5
standard_deviation = 2
number_of_values = 1000
#3: (Optional) > Set the seed to 1 so the random values stay the same each time the program is run.
#np.random.seed(1) 
#4: Generate the random 1000 values. Set as variable 'values' to be used in the histogram.
values = np.random.normal(mean, standard_deviation, number_of_values)

#5: Get the values for the function h(x)= x^3.
# Get 'x' .
# Use np.arange to get the values in the range 0 to 10.
# In this case I used .5 as the step. I did some playing around with the step and realized the smaller the step the smoother the curve.
xpoints = np.arange(0, 11,.5)
#6: get 'y' the output of the function h(x)= x^3.
#Use 'x' (xpoints) and cube it.
ypoints = xpoints ** 3

#7: Plot the histogram and the function h(x)=x^3.
#Use plt.his to plot the histogram of variable 'values'.
#Use colour, labels and title to customise the histogram.
plt.hist((values), color='blue', edgecolor='black')
plt.title('Histogram of a normal distribution of a 1000 values ')
plt.xlabel('Values')
plt.ylabel('Frequency')
#8: Use plt.plot to plot the function h(x)=x^3. Using the x and y point defined in steps 5 and 6.
plt.plot(xpoints, ypoints, color='red')
#9: Use plt.legend to add a legend to the plot.
plt.legend(['h(x)=x3 in the range 0 to 10']) 
#10: Display the plot.
plt.show()

