# Food Recalls at the US Food and Drug Administration
==============================

# Introduction

This project examines food recalls in the United States between January 20, 2015 and January 19, 2019. The goal of the project is to test several hypotheses with the purpose of informing congressional oversight committees, the Consumer Financial Protection Bureau, and other interested parties. The analysis is designed to address the following questions:

1. Has the proportion of recalls classified as Class I declined since President Trump took office?
2. Has the proportion of recall initiated by the FDA declined since President Trump took office?
3. Did the proportion of voluntary recalls from won by President Trump in the 2016 Presidential Election decline after the election?
4. Did the proportion of Class I recalls from states won by President Trump in the 2016 Presidential Election decline after the election?

These questions address several concerns that may be of interest to oversight groups. Such concerns include: 

1. The possibility that firms have reduced reporting of Class I recalls to protect their image, under the assumption that the likelihood of being caught under the current administration is reduced due to the administration's pro-business/anti-regulation views.  
2. The possibility that, as part of broader deregulation and resizing efforts, the FDA initiating fewer recalls.
3. The possibility that under the Trump Administration, firms in "Red States" voluntarily report recalls less often. This situation could occur if these firms believed they are less likely to be caught by the FDA, or more likely to face minimal consequences, under the Trump Administration due to political favor bestowed by the administration on states that supported the president in the 2016 election. 
4. The possibility that under the Trump Administration, firms in "Red States" report Class I recalls less often. This situation could occur if these firms believed they are less likely to be caught by the FDA, or more likely to face minimal consequences, under the Trump Administration due to political favor bestowed by the administration on states that supported the president in the 2016 election. 

Data for the project comes from the United States Food and Drug Administration (FDA) [Food Recall Enforcement Reports](https://open.fda.gov/downloads/) which includes information about the classification of the recall and the type of recall(i.e., voluntary or mandatory). Food recalls are classified into one of three classes. The FDA defines these classes as follows:

1. Class I recall: a situation in which there is a reasonable probability that the use of or exposure to a violative product will cause serious adverse health consequences or death.
2. Class II recall: a situation in which use of or exposure to a violative product may cause temporary or medically reversible adverse health consequences or where the probability of serious adverse health consequences is remote.
3. Class III recall: a situation in which use of or exposure to a violative product is not likely to cause adverse health consequences. 
(Source: [FDA](https://www.fda.gov/safety/industry-guidance-recalls/recalls-background-and-definitions))

Recalls in the data set fall into three categories:
  1. Voluntary: Firm Initiated- These recalls are voluntarily initiated by the recalling firm. Voluntary recalls make up  approximately 97% of all recalls in the United States. 
  2. FDA requested- These recalls are initiated by a request from the FDA. Requested recalls are the rarest type of recall.
  3. FDA Mandated- These recalls are mandated by the FDA. Mandated requests make up approximately 3% of recalls in the United States. 


# Process
The following steps were conducted as part of this project:

1. The data was retrieved from the FDA's website and subsequently imported into a Jupyter Notebook using the Python coding language.
2. Data for years prior to 2012 was removed from the data set due to its apparent incompleteness. Also, a single year of data was removed due to an error in the data.
3. New features were created indicating which recalls were Class I, which recalls were initiated by the FDA (this included both FDA requested and FDA mandated recalls), and which recalls were from states won by President Trump in the 2016 Presidential election. A datetime feature, initiation date, was created from the recall initiation date (which is stored as a string in the data set). 
4. The data was filtered to include only recalls from firms in the United States and features not used in the analysis were dropped. Filtering and dataframe creation (see next step) were conducted using Pandas SQL. 
5. In order to conduct the hypothesis tests, separate data frames were created for each of the samples being compared in the hypothesis tests. Each sample included data for either the two years prior to President Trump's inauguration or the two following the inauguration. For example, to test whether the proportion of recalls classified as Class I changed after the election, a dataframe including information about recalls occuring between January 20, 2015 and January 19, 2017 (inclusive) was created as was a dataframe containing information about recalls occuring between January 20, 2017 and January 19, 2019 (inclusive). 
6. To test the hypotheses, the data is assumed to be a sample of food products that should have been recalled taken from a population of all food products that should have been recalled for the time period included in the sample. This assumption implies that not all food products that should have recalled were recalled. The assumption is necessary for the hypothesis test to have meaning. Without the assumption, the data set would represent the population of all recalls during the time period under examination and, as a result, a statistical hypothesis test would not be necessary. 
7. The hypotheses were tested using z-tests for the difference in two proportions. 
8. The results of the hypothesis tests and trends in results over the years 2012 to 2019 were examined to gain a deeper understanding of the data and to develop a more complete interpretation of the test results. 
9. Recommendations were developed in response to the analysis. 


# Methodology

Z-tests for the differences between two proportions are used to test a set of hypotheses. The hypothesis tests are one-tailed (upper-tail) tests designed to evaluate whether the proportion being tested declines after President Trump's inauguration. Sample sizes for each hypothesis are provided in the table below.  In addition to z-tests, trends from 2012 to 2019 are analyzed. The trend analyses evaluate whether the z-test results reflect a true change relative to the beginning of the Trump Administration or the continuation of a trend beginning prior to President Trump's inauguration. 

| Hypothesis    | Sample Size Prior to the Inauguration | Sample Size Following to the Inauguration |
| ------------- |:-------------------------------------:| :-----------------------------------:|
| Hypothesis 1  | 5605                                  |                                 4470 |
| Hypothesis 2  | 5605                                  |                                 4470 |
| Hypothesis 3  | 5325                                  |                                 4441 |
| Hypothesis 4  | 2595                                  |                                 1386 |  

# Findings

* Has the proportion of recalls classified as Class I declined since President Trump took office?

The hypothesis test was statistically significant (z-statistic: 15.6, p-value: 0.000) with a medium effect size (Cohen's h: 0.32). This result suggests that there is a true difference in Class I recalls between the two years prior and two years following President Trump's inauguration. Analysis of the yearly trend in the proportion of Class I recalls, however, shows that the difference can be explained by a declining trend in the proportion of Class I recalls between 2012 and 2019 and a spike in Class I recalls in 2016. Together, these results provide evidence that any change in the proportion of Class I recalls is not related to actions by the Trump Administration.


* Has the proportion of recalls initiated by the FDA declined since President Trump took office?

The hypothesis test was statistically significant (z-statistic: 12.57, p-value: 0.000) with a medium effect size (Cohen's h: 0.29). This result suggests that there is a true difference in FDA initiated recalls between the two years prior and two years following President Trump's inauguration. Analysis of the yearly trend in the proportion of FDA mandated recalls, however, shows that the difference can be explained by a a spike in FDA initiated recalls in 2015. This spike is driven primarily by two recall events involving two producers of dietary supplements. Together, these results provide evidence that any change in the proportion of FDA initiated recalls is not related to actions by the Trump Administration.


* Did the proportion of voluntary recalls from won by President Trump in the 2016 Presidential Election decline after the election?

The hypothesis test was statistically significant (z-statistic: 12.27, p-value: 0.000) with a medium effect size (Cohen's h: 0.25). This result suggests that there is a true difference in proportion of voluntary recalls initiated by firms in "Red States" between the two years prior and two years following President Trump's inauguration. Analysis of the yearly trend in the proportion voluntary recalls, supports the hypothesis test results. Together, these results provide evidence that since President Trump's inauguration, "Red States" are voluntarily initiating recalls at a lower rate than they did prior to President Trump taking office. 


* Did the proportion of Class I recalls from states won by President Trump in the 2016 Presidential Election decline after the election?

The hypothesis test was not statistically significant (z-statistic: -0.4, p-value: 0.655) with a very small effect size (Cohen's h: -0.01). This result suggests that there is not a true difference in the proportion of Class I recalls initiated by firms in "Red States" between the two years prior and two years following President Trump's inauguration. Analysis of the yearly trend in the proportion of voluntary recalls in "Red States", however, shows an interesting pattern. Between 2012 and 2016, the proportion of Class I recalls in "Red States" oscillates between roughly 0.35 and 0.65. From 2016 through June of 2019, the annual proportion of Class I recalls in "Red States" has increased each year from a low of approximately 0.40 to 0.60 in June of 2019. An explanation for this change in pattern is unknown and requires further investigation. 

# Recommendations
Based on the foregoing analysis, the following recommendations are proffered:
* Oversight committees and organizations should watch the trend in voluntary recalls in "Red States" over the next two years. If the proportion of voluntary recalls continues to indicate a consistent pattern of "Red States" representing a smaller proportion of recalls than "Blue States", then further investigation into the cause of this pattern should be initiated. 
* Oversight committees and organizations should watch the trend in Class I recalls in "Red States" over the next two years. If the proportion of Class I recalls continues to indicate a consistent pattern of "Red States" representing a larger proportion of recalls than "Blue States", then further investigation into the cause of this pattern should be initiated.  

# Limitations and Further Study
The analysis outlined above utilized z-tests for the difference in two proportions. The z-test requires that the samples being tested are randomly selected from the population under study. The population for this project is not fully defined and, therefore, the randomness of the samples cannot be confirmed. If the samples deviate significantly from the population, then the results of the z-tests are misleading. 

This project used individual recalls as the unit of analysis. Multiple recalls often make up a single recall event. For example, firm A issues a recall (an event) for multiple products(individual recalls). Further analysis should examine these hypotheses with the event as the unit of analysis. 
