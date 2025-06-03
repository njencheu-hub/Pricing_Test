# 12\_18: **Pricing Test**

##  **Goal**

Pricing optimization, predictably, stands out as an area where data science can deliver substantial value.

The objective is to assess the effectiveness of a pricing experiment currently underway on the website. The approach centers on segmenting users based on their behavior and uncovering insights into segments that exhibit distinct responses, alongside any other notable findings.

---

**Challenge Description**

Company XYZ currently sells its software at a price of $39, and the VP of Product has initiated a pricing experiment to test whether increasing the price to $59 could boost revenue. The experiment randomly assigned 66% of users to see the original price and 33% to see the higher price.

To determine the optimal price point, several key questions need addressing:

1. **Which price should the company adopt ($39 or $59)?**  
   * The data analysis will focus on comparing revenue and conversion metrics between the two price points to assess which price yields better results.  
2. **What actionable insights can be derived to potentially increase conversion rate?**  
   * Insights will be derived from user behavior patterns and conversion rates at both price points. This will help identify factors influencing user decisions and suggest strategies to optimize conversion rates.

3. **\[Bonus\] Is the test duration appropriate, and when should the test be concluded?**  
   * Assessing the statistical significance and stability of results over time will determine the appropriate duration of the pricing test. Recommendations will be made based on when conclusive results are likely to be obtained.

## **Data**

We have two tables downloadable by clicking [**here**](https://drive.google.com/uc?export=download&id=1w4Z92zzDQcP2IXBlQI0Jw1pkqvNoX1vR).

The dataset includes two tables relevant to evaluating a pricing test conducted by Company XYZ:

**test\_results Table:**

* **user\_id**: Unique identifier for each user, can be linked to the user\_id in the user\_table.  
* **timestamp**: Date and time when the user first visited the Company XYZ webpage, recorded in the user's local time.  
* **source**: Marketing channel through which the user accessed the site, categorized into ads (e.g., Google, Facebook), SEO (e.g., Google, Bing), friend referrals, or direct traffic.  
* **device**: Type of device used by the user, categorized as mobile or web.  
* **operative\_system**: Operating system of the user's device, classified as Windows, Linux, Mac (for web), or Android, iOS (for mobile); labeled as "Other" if none of these.  
* **test**: Indicates whether the user was in the test group (1 for higher price) or the control group (0 for the old/lower price).  
* **price**: The price of the software that the user saw, matching the test group they were assigned to.  
* **converted**: Binary indicator showing whether the user completed a purchase (1) or not (0).

**user\_table:**

* **user\_id**: Unique identifier for each user, linking to the user\_id in the test\_results table.  
* **city**: City where the user is located, derived from the user's IP address.  
* **country**: Country where the city is located.  
* **lat**: Latitude of the city.  
* **long**: Longitude of the city.

This data will be used to evaluate the effectiveness of a pricing test where 66% of users viewed the original price ($39) and 33% viewed the increased price ($59). Insights will focus on user behavior across different segments, such as marketing channels, devices, and geographic locations, to understand the impact of pricing on conversion rates and revenue.

