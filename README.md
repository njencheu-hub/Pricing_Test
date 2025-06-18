# A/B Test Analysis: Optimal Pricing Strategy

**Duration:** June 1-5 2025
 
**Tools Used:** Python, Pandas, Seaborn, Matplotlib, SciPy, Statsmodels  

## Overview

This project evaluated whether increasing software pricing from $39 to $59 would improve overall revenue, using A/B test data. By merging user information and test outcomes, we conducted detailed statistical analysis and segmentation to inform data-driven pricing decisions.

---

## Key Steps

### 1. Data Integration & Cleaning
- Merged test group data with user demographics on `user_id`.
- Identified and excluded mismatched test/price assignments and missing location data.

### 2. Metric Engineering
- Created key variable: **`revenue = converted * price`**.
- Calculated average revenue per user (ARPU) by test group.

### 3. Statistical Evaluation
- Confirmed price increase reduced conversion by ~25%, but **ARPU increased** from **$0.78 → $0.93**.
- **T-test (p < 0.000000001)** showed results were statistically significant.

### 4. Segmentation Insights
- **By Source**: Most channels (ads, SEO) showed higher revenue with the $59 price.
- **By Device**: Mobile users were **less price sensitive**, a positive long-term signal.
- **By OS**: Identified Linux-specific bug affecting conversions; removed for accuracy.
- **By City**: Large variance observed—suggests potential for localized pricing strategies.

### 5. Sample Size & Test Duration Planning
- Calculated needed **sample size ≈ 5,548 users per group**.
- Average weekly user traffic: ~24,356.
- Conclusion: **Minimum 2-week test** with **~11% of traffic** in the test group ensures statistical power.

---

## Visual Outputs

- `revenue_by_source.png`  
- `revenue_by_device.png`  
- `revenue_by_os.png`  
- `revenue_by_top10city.png`

---

## Conclusion

Raising the price to $59 improves revenue per user significantly, despite lower conversion. Data supports implementing the price increase, especially among mobile users and ad-driven sources. Test planning calculations confirm feasibility for future rollouts.