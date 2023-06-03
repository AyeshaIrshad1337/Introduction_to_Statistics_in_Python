# Introduction_to_Statistics_in_Python
+  [Summary Statistics](#Summary-Statistics)
+ chapter 2
+ chapter 3
# Summary Statistics  
<details>
  <summary>What is an Statistics:</summary> 
  <blockquote>
<details>
  <summary>What is an Statistics</summary>
 
  + **The field of statistics** - The practice and study of collecting and analyzing
  + **A Summary Statistics** - a fact about or summary of some data
</details>
<details>
  <summary>What Statistics Can do</summary>
 
  + How likely someone to purchase a product? are peopele more likely to purchase it, if they can use a different payment system?
  + How many occupants will your hotel have ? How can you optimize occupancy?
  + How many sizes of jeans need to be manufactured so they can fit 95% of the population? Should the same number of each size be prepared?
  + A/B test: Which ad is more effecive in getting people to purchase a product? 
</details>
<details>
  <summary>What Statistics Cannot do?</summary> 
  
  + While statistics can answer a lot of questions, it's important to note that statistics can't answer every question
</details>

<details>
  <summary>Types of statistics</summary>
  
  ### Descriptive
  + Decribe and summarize data
  ### Inferential Statistics
  + Use a sample of data to make inferences about a larger population like what percent of people drive to work?
#### Example  
  ![image](https://github.com/AyeshaIrshad1337/Introduction_to_Statistics_in_Python/assets/104616632/d54c9998-052a-4e7f-a31d-89c626f475ba)

</details>
<details>
  <summary>Types Of Data</summary>
  
 ### Numeric (Quantitaive)
  + **Continuous (Measured)**: 
  + Airplane speed
  + Time spent waiting in line
  + **Discete (Counted)**: 
  + Number of pets
  + Number of Packages shipped
 ### Categorical (Qualitative)
  + **Nomial (Unordered)**: 
  + Married/Unmarried
  + Country of residence
  + **Ordinal (Ordered)**: 
  + Strongly agreee / Somewhat disagree / Strongly disagree etc
  ### Example:
  ![image](https://github.com/AyeshaIrshad1337/Introduction_to_Statistics_in_Python/assets/104616632/f569cbaa-171c-459b-aed9-20881afc681b)

</details>
  </blockquote>
</details>
<details>
  <summary>Measure Of Center</summary>
  <blockquote>
<details>
      <summary>Historgram</summary>
      
![image](https://github.com/AyeshaIrshad1337/Introduction_to_Statistics_in_Python/assets/104616632/c7fc9606-35bf-441d-9d4d-b773dd0569e0)

A histogram takes a bunch of data points and separates them into bins, or ranges of values. Here, there's a bin for 0 to 2 hours, 2 to 4 hours, and so on. The heights of the bars represent the number of data points that fall into that bin, so there's one mammal in the dataset that sleeps between 0 to 2 hours, and nine mammals that sleep two to four hours. Histograms are a great way to visually summarize the data, but we can use numerical summary statistics to summarize even further.
   
</details>
<details>
      <summary>Measure Of Center : Mean</summary>
 
  ![image](https://github.com/AyeshaIrshad1337/Introduction_to_Statistics_in_Python/assets/104616632/67c261ad-2b99-477a-9137-0bed265ebaa8)

The mean, often called the average, is one of the most common ways of summarizing data. To calculate mean, we add up all the numbers of interest and divide by the total number of data points, which is 83 here. This gives us 10-point-43 hours of sleep. In Python, we can use numpy's mean function, passing it the variable of interest.

</details>
<details>
      <summary>Measure Of Center : Median</summary>
 
![image](https://github.com/AyeshaIrshad1337/Introduction_to_Statistics_in_Python/assets/104616632/9af45e5e-2691-4fc2-8da5-d92355351bef)
  
The median is the value where 50% of the data is lower than it, and 50% of the data is higher. We can calculate this by sorting all the data points and taking the middle one, which would be index 41 in this case. This gives us a median of 10-point-1 hours of sleep. In Python, we can use np-dot-median to do the calculations for us.
  
</details>
<details>
      <summary>Measure Of Center : Mode</summary>
 
![image](https://github.com/AyeshaIrshad1337/Introduction_to_Statistics_in_Python/assets/104616632/c86448da-f099-4195-9aac-ab5cb42c07e8)
 
The mode is the most frequent value in the data. If we count how many occurrences there are of each sleep_total and sort in descending order, there are 4 mammals that sleep for 12.5 hours, so this is the mode. The mode of the vore variable, which indicates the animal's diet, is herbivore. We can also find the mode using the mode function from the statistics module. Mode is often used for categorical variables, since categorical variables can be unordered and often don't have an inherent numerical representation.
  
</details>

<details>
      <summary>Adding Outlier</summary>
 
 We get a mean sleep time of 16-point-5 hours and a median sleep time of 18-point-9 hours.  
  
![image](https://github.com/AyeshaIrshad1337/Introduction_to_Statistics_in_Python/assets/104616632/760b285f-4ea2-4f34-8c01-907d47aaf2f1)

Now let's say we've discovered a new mystery insectivore that never sleeps. i.e row 89 has sleep 0.0

![image](https://github.com/AyeshaIrshad1337/Introduction_to_Statistics_in_Python/assets/104616632/a5706b58-6151-4727-ae91-753a93aef10a)

If we take the mean and median again, we get different results. The mean went down by more than 3 hours, while the median changed by less than an hour. This is because the mean is much more sensitive to extreme values than the median.  
  
![image](https://github.com/AyeshaIrshad1337/Introduction_to_Statistics_in_Python/assets/104616632/7313073f-c922-4060-bf21-21f953a4ddcd)
  
  
</details>

<details>
      <summary>Which Measure to Use ? </summary>
  
 ![image](https://github.com/AyeshaIrshad1337/Introduction_to_Statistics_in_Python/assets/104616632/c1e27433-9270-4eb9-b3b9-e86f752fb60e)

  
 Since the mean is more sensitive to extreme values, it works better for symmetrical data like this. Notice that the mean, in black, and median, in red, are quite close.
  
</details>
<details>
      <summary>Skew </summary>
  
 ![image](https://github.com/AyeshaIrshad1337/Introduction_to_Statistics_in_Python/assets/104616632/2b8a6d62-75b2-4b7b-b9a8-6035260f4de3)
  
However, if the data is skewed, meaning it's not symmetrical, like this, median is usually better to use. In this histogram, the data is piled up on the right, with a tail on the left. Data that looks like this is called left-skewed data. When data is piled up on the left with a tail on the right, it's right-skewed.
 ## Which measure to use?
  
  When data is skewed, the mean and median are different. The mean is pulled in the direction of the skew, so it's lower than the median on the left-skewed data, and higher than the median on the right-skewed data. Because the mean is pulled around by the extreme values, it's better to use the median since it's less affected by outliers.
    
</details>
  </blockquote>
</details>
<details>
  <summary>Measure Of Spread: </summary>
  <blockquote>
  
<details>
  <summary>What is Spread?</summary>
  
  ![image](https://github.com/AyeshaIrshad1337/Introduction_to_Statistics_in_Python/assets/104616632/0f4ceacb-8736-45b7-99f6-cb289c2015dd)

  Spread is just what it sounds like - it describes how spread apart or close together the data points are. Just like measures of center, there are a few different measures of spread.
</details>

<details>
  <summary>Variance</summary>
  
  ![image](https://github.com/AyeshaIrshad1337/Introduction_to_Statistics_in_Python/assets/104616632/e84744db-2b1c-420e-9c22-9d05234156fe)

  Average Distance from each data point to the data's mean  
  ## Calculate the Variance  
  
![image](https://github.com/AyeshaIrshad1337/Introduction_to_Statistics_in_Python/assets/104616632/2a3d0d9b-5fda-4981-b077-3d87e18973f6)  
    
![image](https://github.com/AyeshaIrshad1337/Introduction_to_Statistics_in_Python/assets/104616632/eadc36dc-141c-4c9b-ab4a-fa06f1fb6fb0)

  To calculate the variance, we start by calculating the distance between each point and the mean, so we get one number for every data point. We then square each distance and then add them all together. Finally, we divide the sum of squared distances by the number of data points minus 1, giving us the variance. The higher the variance, the more spread out the data is. It's important to note that the units of variance are squared, so in this case, it's 19-point-8 hours squared.   
  
  ![image](https://github.com/AyeshaIrshad1337/Introduction_to_Statistics_in_Python/assets/104616632/ee033693-f1bd-4f3f-8d99-a72080ab5ce2)

  
   We can calculate the variance in one step using np-dot-var, setting the ddof argument to 1. If we don't specify ddof equals 1, a slightly different formula is used to calculate variance that should only be used on a full population, not a sample.
</details>
<details>
  <summary>Standard Deviation</summary>
  
![image](https://github.com/AyeshaIrshad1337/Introduction_to_Statistics_in_Python/assets/104616632/92e8807e-b6d4-4b19-a2c8-397b06a9c3ab)

The standard deviation is another measure of spread, calculated by taking the square root of the variance. It can be calculated using np-dot-std. Just like np-dot-var, we need to set ddof to 1. The nice thing about standard deviation is that the units are usually easier to understand since they're not squared. It's easier to wrap your head around 4 and a half hours than 19-point-8 hours squared.
</details>
<details>
  <summary>Mean Absolute Deviation : MAD</summary>
    
![image](https://github.com/AyeshaIrshad1337/Introduction_to_Statistics_in_Python/assets/104616632/65f82a41-7d8b-4c1c-9d5f-4dd14033bb14)
    
Mean absolute deviation takes the absolute value of the distances to the mean, and then takes the mean of those differences. While this is similar to standard deviation, it's not exactly the same. Standard deviation squares distances, so longer distances are penalized more than shorter ones, while mean absolute deviation penalizes each distance equally. One isn't better than the other, but SD is more common than MAD.  
    
![image](https://github.com/AyeshaIrshad1337/Introduction_to_Statistics_in_Python/assets/104616632/2f7ae86a-a3c9-4332-89c7-91a24fad2960)
  
  
</details>
<details>
  <summary>Quantile</summary>
    
![image](https://github.com/AyeshaIrshad1337/Introduction_to_Statistics_in_Python/assets/104616632/be5ecc9f-3f25-4d99-b0c6-15d36da3a2a6)

 Quantiles, also called percentiles, split up the data into some number of equal parts. Here, we call np-dot-quantile, passing in the column of interest, followed by point-5. This gives us 10-point-1 hours, so 50% of mammals in the dataset sleep less than 10-point-1 hours a day, and the other 50% sleep more than 10-point-1 hours, so this is exactly the same as the median. We can also pass in a list of numbers to get multiple quantiles at once. Here, we split the data into 4 equal parts. These are also called quartiles. This means that 25% of the data is between 1-point-9 and 7-point-85, another 25% is between 7-point-85 and 10-point-10, and so on.
</details>
<details>
  <summary>BoxPlot</summary>
    
![image](https://github.com/AyeshaIrshad1337/Introduction_to_Statistics_in_Python/assets/104616632/c9ff3496-3656-49c1-bf29-9b3b95f6e508)

 The boxes in box plots represent quartiles. The bottom of the box is the first quartile, and the top of the box is the third quartile. The middle line is the second quartile, or the median
</details>
<details>
  <summary>Quantile using np.linespace</summary>
    
![image](https://github.com/AyeshaIrshad1337/Introduction_to_Statistics_in_Python/assets/104616632/b0599ca9-8065-44f0-9115-10089ba8d3d8)

we split the data in five equal pieces, but we can also use np-dot-linspace as a shortcut, which takes in the starting number, the stopping number, and the number intervals. We can compute the same quantiles using np-dot-linspace starting at zero, stopping at one, splitting into 5 different intervals
</details>
<details>
  <summary>IQR: Inter Quartile Range</summary>
    
![image](https://github.com/AyeshaIrshad1337/Introduction_to_Statistics_in_Python/assets/104616632/2884d7a2-a7b2-4a27-9b76-6bc250cd13f7)


The interquartile range, or IQR, is another measure of spread. It's the distance between the 25th and 75th percentile, which is also the height of the box in a boxplot. We can calculate it using the quantile function, or using the iqr function from scipy-dot-stats to get 5-point-9 hours.  
   
</details>
<details>
  <summary>Outliers</summary>
      
Outliers are data points that are substantially different from the others. But how do we know what a substantial difference is? A rule that's often used is that any data point less than the first quartile minus 1-point-5 times the IQR is an outlier, as well as any point greater than the third quartile plus 1-point-5 times the IQR.  
![image](https://github.com/AyeshaIrshad1337/Introduction_to_Statistics_in_Python/assets/104616632/85bf1b0e-7807-4d5a-b050-908f9d308927)
    
  ## Finding Outliers  
  ![image](https://github.com/AyeshaIrshad1337/Introduction_to_Statistics_in_Python/assets/104616632/c377de1e-efd6-4498-940f-8fa516943001)

</details>

  </blockquote>
</details>
