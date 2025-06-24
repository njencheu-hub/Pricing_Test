# A/B Test Analysis: Optimal Pricing Strategy
 
**Tools Used:** Python, Pandas, Seaborn, Matplotlib, SciPy, Statsmodels  

> This project evaluates whether raising software prices from $39 to $59 improves overall revenue, using user-level A/B test data and detailed segment analysis to support pricing strategy decisions.

---

## Table of Contents

- [Overview](#overview)
- [Real-World Use Cases](#real-world-use-cases)
- [Features](#features)
- [Key Steps](#key-steps)
- [Visual Outputs](#visual-outputs)
- [Installation](#installation)
- [Usage](#usage)
- [Conclusion](#conclusion)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The analysis combined A/B test data with user demographics to examine the impact of a price increase on conversion and revenue. Key metrics were engineered, statistical tests were run, and segment-specific patterns were explored to inform pricing rollout.

---

## 🌍 Real-World Use Cases

- **Product Managers**: Use conversion and revenue trade-offs to guide pricing strategy.
- **Growth Teams**: Identify segments (e.g., device or acquisition source) that tolerate higher prices.
- **Executives**: Justify pricing decisions with data-backed ARPU improvements.
- **Analysts**: Apply segmentation and power analysis frameworks to future experiments.

---

## Features

- User-level data cleaning and test integrity validation
- Revenue metric engineering and ARPU analysis
- Statistical testing with Welch’s t-test
- Granular segmentation by device, source, city, and OS
- Sample size and test duration calculator
- Chart exports for stakeholder presentation

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

## Installation

To install the required Python packages:

pip install -r requirements.txt

## Usage

To run the analysis:

python pricing_test.py

## Conclusion

Raising the price to $59 improves revenue per user significantly, despite lower conversion. Data supports implementing the price increase, especially among mobile users and ad-driven sources. Test planning calculations confirm feasibility for future rollouts.

## Contributing

We welcome community contributions!

1. Fork the repository

2. Create a new branch:

git checkout -b feature/your-feature

3. Make your changes

4. Push to your branch:

git push origin feature/your-feature

5. Submit a Pull Request

## License
This project is licensed under the MIT License.
