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
  </blockquote>
</details>
