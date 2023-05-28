# Excerise
# Mean and median
# In this chapter, you'll be working with the 2018 Food Carbon Footprint Index from nu3. The food_consumption dataset contains information about the kilograms of food consumed per person per year in each country in each food category (consumption) as well as information about the carbon footprint of that food category (co2_emissions) measured in kilograms of carbon dioxide, or CO2, per person per year in each country.

# In this exercise, you'll compute measures of center to compare food consumption in the US and Belgium using your pandas and numpy skills.

# pandas is imported as pd for you and food_consumption is pre-loaded.
# instruction
# Import numpy with the alias np.
# Create two DataFrames: one that holds the rows of food_consumption for 'Belgium' and another that holds rows for 'USA'. Call these be_consumption and usa_consumption.
# Calculate the mean and median of kilograms of food consumed per person per year for both countries.

# Import numpy with alias np
import numpy as np

# Filter for Belgium
be_consumption = food_consumption[food_consumption['country']=="Belgium"]

# Filter for USA
usa_consumption = food_consumption[food_consumption["country"]=="USA"]

# Calculate mean and median consumption in Belgium
print(np.mean(be_consumption['consumption']))
print(np.median(be_consumption['consumption']))

# Calculate mean and median consumption in USA
print(np.mean(usa_consumption['consumption']))
print(np.median(usa_consumption['consumption']))

# Subset food_consumption for rows with data about Belgium and the USA.
# Group the subsetted data by country and select only the consumption column.
# Calculate the mean and median of the kilograms of food consumed per person per year in each country using .agg().
import numpy as np

# Subset for Belgium and USA only
be_and_usa = food_consumption[(food_consumption['country']=='Belgium') | (food_consumption['country']=='USA')]

# Group by country, select consumption column, and compute mean and median
print(be_and_usa.groupby('country')['consumption'].agg([np.mean,np.median]))
# # Excerise 2
# In the video, you learned that the mean is the sum of all the data points divided by the total number of data points, and the median is the middle value of the dataset where 50% of the data is less than the median, and 50% of the data is greater than the median. In this exercise, you'll compare these two measures of center.

# pandas is loaded as pd, numpy is loaded as np, and food_consumption is available.

#instructions 
# Import matplotlib.pyplot with the alias plt.
# Subset food_consumption to get the rows where food_category is 'rice'.
# Create a histogram of co2_emission for rice and show the plot.

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category']=='rice']

# Histogram of co2_emission for rice and show plot
plt.hist(rice_consumption['co2_emission'])
plt.show()


# Question
# Take a look at the histogram you just created of different countries' CO2 emissions for rice. Which of the following terms best describes the shape of the data?

#  Answer is right skew


# Use .agg() to calculate the mean and median of co2_emission for rice.

# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

# Calculate mean and median of co2_emission with .agg()
print(rice_consumption['co2_emission'].agg([np.mean,np.median]))


# Question
# Given the skew of this data, what measure of central tendency best summarizes the kilograms of CO2 emissions per person per year for rice?

# Possible answers

# MEdian as it is representing the answer near the majority of the numbers are graphed
