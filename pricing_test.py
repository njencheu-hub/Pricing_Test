# 1. Import Libraries and Load Data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from scipy.stats import ttest_ind
import statsmodels.stats.api as sms
from matplotlib import rcParams

rcParams.update({'figure.autolayout': True})
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 350)
  
#read the files
test = pd.read_csv("test_results.csv")
print(test.head())

#    user_id            timestamp          source  device operative_system  test  price  converted
# 0   604839  2015-05-08 03:38:34    ads_facebook  mobile              iOS     0     39          0
# 1   624057  2015-05-10 21:08:46      seo-google  mobile          android     0     39          0
# 2   317970  2015-04-04 15:01:23        ads-bing  mobile          android     0     39          0
# 3   685636  2015-05-07 07:26:01  direct_traffic  mobile              iOS     1     59          0
# 4   820854  2015-05-24 11:04:40    ads_facebook     web              mac     0     39          0

user = pd.read_csv("user_table.csv")
print(user.head())

#   user_id         city country    lat    long
# 0   510335      Peabody     USA  42.53  -70.97
# 1    89568         Reno     USA  39.54 -119.82
# 2   434134       Rialto     USA  34.11 -117.39
# 3   289769  Carson City     USA  39.15 -119.74
# 4   939586      Chicago     USA  41.84  -87.68

# Check for missing values:

print(test.isnull().sum())

# user_id             0
# timestamp           0
# source              0
# device              0
# operative_system    0
# test                0
# price               0
# converted           0
# dtype: int64

print(user.isnull().sum())

# user_id    0
# city       0
# country    0
# lat        0
# long       0
# dtype: int64

#merge the two datasets on user_id
data=pd.merge(left=test, right=user, how='left', on='user_id')

print(data.head())

#    user_id            timestamp          source  device operative_system  ...  converted          city  country    lat   long
# 0   604839  2015-05-08 03:38:34    ads_facebook  mobile              iOS  ...          0       Buffalo      USA  42.89 -78.86
# 1   624057  2015-05-10 21:08:46      seo-google  mobile          android  ...          0     Lakeville      USA  44.68 -93.24
# 2   317970  2015-04-04 15:01:23        ads-bing  mobile          android  ...          0         Parma      USA  41.38 -81.73
# 3   685636  2015-05-07 07:26:01  direct_traffic  mobile              iOS  ...          0  Fayetteville      USA  35.07 -78.90
# 4   820854  2015-05-24 11:04:40    ads_facebook     web              mac  ...          0       Fishers      USA  39.95 -86.02

#Check for missing values.
#Since there were no missing values before the join, 
#this would mean some users are in the test table, but not in the user table

print(data.isnull().sum())

# [5 rows x 12 columns]
# user_id                 0
# timestamp               0
# source                  0
# device                  0
# operative_system        0
# test                    0
# price                   0
# converted               0
# city                41184
# country             41184
# lat                 41184
# long                41184
# dtype: int64

#let's check if, in fact, those missing values are exactly the number of rows 
#in the test table - user table

print(max(data.isnull().sum())==(test.shape[0]-user.shape[0]))

# True

# 2. Basic EDA (Exploratory Data Analysis)

# Whenever two columns are supposed to always agree/be consistent (like test and price here), 
# one of the first things you want to do is to check if they in fact always agree. 
# Especially in a take-home challenge, why would they have two columns when just one would be needed?

# So, let’s check if people in test always get the 59$ and people in control 39$.

print(data[['user_id','test','price']].groupby(['test','price']).count())

#             user_id
# test price
# 0    39      202517
#      59         210
# 1    39         155
#      59      113918

# There are instances where a few users seem to have been assigned the incorrect price 
# based on their test or control group assignment. Given the relatively low number of affected users, 
# the approach will be to exclude them from the analysis and proceed with the assessment. 
# However, it is essential to conduct further investigation to ensure there are no larger 
# systemic issues that could 
# potentially impact other aspects of the data or conclusions drawn from the analysis.

data=data[((data['test']==0) & (data['price']==39)) | ((data['test']==1) & (data['price']==59))]

print(data[['user_id','test','price']].groupby(['test','price']).count())

#             user_id
# test price
# 0    39      202517
# 1    59      113918

#Let's now create the revenue variable, which is the main target of this challenge

data['revenue']=data['converted']*data['price']

print(data['revenue'].describe())

# count    316435.000000
# mean          0.827083
# std           6.179009
# min           0.000000
# 25%           0.000000
# 50%           0.000000
# 75%           0.000000
# max          59.000000

# -----------
# Q: Should the company sell its software for 39 or 59?
# -----------

#Firstly let's compare conversion rate. 
#We obviously do expect convesion rate to drop, let's check by how much

print(data[['converted','test']].groupby('test').mean())

#       converted
# test
# 0      0.019900
# 1      0.015555

# Conversion rate did go down by roughly 25%. But are we still making more money per user?

#Check avg revenue per user

print(data[['revenue','test']].groupby('test').mean())

# test
# 0     0.776083
# 1     0.917748

# Yes, it looks like revenue per user is up. 
# Let’s now check if this is statistically significant:

#Check avg revenue per user

print(ttest_ind(data[data['test']==1]['revenue'], data[data['test']==0]['revenue'], equal_var=False))

# TtestResult(statistic=5.715224666463108, pvalue=1.0972577312420781e-08, df=186141.738219264)

# Good. It looks like revenue per user is up and highly statistically significant.

# Let’s now check how different segments are reacting to the test. 
# This can give us extremely useful information about user price sensitivity by segment, 
# which is really just a fancy way to say: how much different users are valuing our product?

# # Let’s start by source:

# sns.barplot(x='source', y='revenue', hue='test', data=data)
# plt.xticks(rotation=45)
# plt.title("Revenue by Source and Test Group")
# plt.tight_layout()  # Optional: improves layout if labels are crowded

# # Save the plot as a PNG file
# plt.savefig("revenue_by_source.png", dpi=300)

# # plt.show()

# # Most segments agree with the overall finding of an increase in revenue as we increase price. 
# # Unfortunately, the three segments with the higher avg revenue with the new price happen 
# # to be the most expensive ones, i.e. friend referral, and google/FB ads.

# # Let’s now check device:

# sns.barplot(x='device', y='revenue', hue='test', data=data)
# plt.xticks(rotation=45)
# plt.title("Revenue by Device and Test Group")
# plt.tight_layout()  # Optional: improves layout if labels are crowded

# # Save the plot as a PNG file
# plt.savefig("revenue_by_device.png", dpi=300)

# # plt.show()

# It appears that mobile users are less price sensitive. 
# This is typically very good as mobile is in most cases the channel that’s proportionally 
# growing more between the two. So, in the long run, the revenue gain from the price change 
# could be even larger.

# Let’s now check operative system:

# sns.barplot(x='operative_system', y='revenue', hue='test', data=data)
# plt.xticks(rotation=45)
# plt.title("Revenue by Operative_System and Test Group")
# plt.tight_layout()  # Optional: improves layout if labels are crowded

# # Save the plot as a PNG file
# plt.savefig("revenue_by_os.png", dpi=300)

# plt.show()

# A notable anomaly is the 0% conversion rate observed for Linux users in the test group. 
# This discrepancy strongly suggests a potential bug in the data. 
# It is not uncommon to encounter such issues with specific segments, which can introduce 
# bias into the results. To mitigate this issue, we will exclude the Linux segment from 
# the dataset and proceed to reanalyze the statistical test.

#Firstly, how many users are we talking about?

print(data.query('operative_system == \'linux\'').shape[0]/data.shape[0])


#Check avg revenue per user after removing Linux
data = data.query('operative_system != \'linux\'')

print(data[['revenue','test']].groupby('test').mean())

# test
# 0     0.778002
# 1     0.933531

print(ttest_ind(data.query('test==1')['revenue'], data.query('test==0')['revenue'], equal_var=False))

# TtestResult(statistic=6.184240028400434, pvalue=6.253458285742887e-10, df=181667.22654265029)

# Since the bug was in test, as expected the overall numbers improve slightly. 
# We could quickly recheck the plots of OS and source with the new dataset after removing linux, 
# however it is highly unlikely insights will be different, given the small proportion of linux users.

# Let’s now check city. We will just check the top 10 cities in terms of user base:

top_cities = data['city'].value_counts().reset_index()
top_cities.columns = ['city', 'count']  # Rename for clarity
top_cities = top_cities.sort_values('count', ascending=False).head(10)
print(top_cities)

#            city  count
# 0      New York  25401
# 1       Chicago   7071
# 2       Houston   6608
# 3   San Antonio   4554
# 4   Los Angeles   4089
# 5      San Jose   3312
# 6  Indianapolis   3177
# 7  Jacksonville   2865
# 8  Philadelphia   2488
# 9     Las Vegas   2375

# #plot avg revenue for top 10 cities
# sns.barplot(x='city', y='revenue', hue='test', data=data[data['city'].isin(top_cities['city'])])
# plt.xticks(rotation=45)
# plt.title("Revenue by Top 10 City and Test Group")
# plt.tight_layout()  # Optional: improves layout if labels are crowded

# # Save the plot as a PNG file
# plt.savefig("revenue_by_top10city.png", dpi=300)

# plt.show()

# The outcomes vary significantly across different cities, although drawing concrete conclusions 
# is challenging. The city variable encompasses numerous levels, meaning that by sheer chance, 
# diverse results are expected. Nonetheless, integrating this data with domain expertise and 
# product knowledge could facilitate the formulation of hypotheses. These hypotheses could subsequently 
# be tested through more rigorously designed A/B tests to ensure statistical validity.

# --------
# [Bonus] After how many days you would have stopped the test?
# --------

# To determine the appropriate duration for running a test, it's crucial to establish the minimum 
# sample size required per group. This calculation hinges on defining the detectable effect size 
# we aim to observe. Normally, in practical scenarios, this figure would be specified by a product manager. 
# However, we can illustrate the sample size calculation under specific assumptions.

# Assuming a standard significance level of 0.05 and a power of 0.8, let's consider detecting 
# a difference in conversion rates of approximately 33%, equivalent to a change from 
# a 39% to a 59% conversion rate (1 - $39/$59). This means we aim to detect if the new 
# conversion rate is about 66% of the old rate.

conversion_rate_control = test.query('test==0').converted.mean()
p1_and_p2 = sms.proportion_effectsize(conversion_rate_control, conversion_rate_control*39/59)
sample_size = round(sms.NormalIndPower().solve_power(p1_and_p2, power=0.8, alpha=0.05))
print("The required sample size per group is ~", sample_size)

# The required sample size per group is ~ 5548

# Let’s now check how many users we have per week to figure out how long it will take to get enough users:

#create a column that's week of the year
test['week_year'] = pd.to_datetime(test.timestamp.str.split(' ').str[0]).dt.strftime('%W')
#take avg count of users per week. We remove first and last week, just in case they don't include all 7 days
users_week = test['week_year'].value_counts().sort_index()
users_week = users_week.drop(users_week.index[[0,(users_week.shape[0]-1)]]).mean()
  
print("Avg number of users per week is:", round(users_week))

# Avg number of users per week is: 24356

# If we conducted the test on 50% of the users, we could complete it in less than a week. 
# However, it's advisable to run the test for at least two weeks to capture weekly patterns effectively. 
# In terms of the percentage split between test and control groups, we need to determine the minimum 
# percentage of users in the test group required to achieve the necessary sample size within two weeks.

# That is:

print("The percentage of traffic that needs to be in test is", round(sample_size/(users_week*2)*100))

# The percentage of traffic that needs to be in test is 11