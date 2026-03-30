# Tobacco Tax Policy Analysis: Virginia vs. Maryland (FY2021–FY2025)

**Author:** Muhammad Salman Pasha | Data Analyst  
**Published:** March 2026  
**SSRN:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6491418  
**Interactive Dashboard:** https://public.tableau.com/app/profile/muhammad.salman.pasha/viz/VA-MDTobaccoTaxPolicyAnalysis2021-2025Pasha/Dashboard1

---

## Overview

This repository contains the complete data, code, and visualizations for original research examining how divergent tobacco tax policies in Virginia and Maryland affected state tax revenues and small retail businesses between FY2021 and FY2025.

The full paper is published on SSRN. All data is sourced directly from official government reports.

---

## Key Findings

- Virginia's cigarette tax revenue declined **33.5%** over the study period despite no tax increases
- Maryland's revenue surged **+29.7%** in FY2022 after raising its tax to $3.75/pack — then fell **-12.0%** in FY2024
- OTP revenue grew in **both states** — Maryland +38.3%, Virginia +4.9% — confirming product substitution
- A **$4.40/pack tax gap** creates $44/carton savings buying in Virginia vs Maryland

---

## Repository Contents

| File | Description |
|------|-------------|
| `01_annual_summary.csv` | Annual revenue data — both states FY2021–FY2025 |
| `02_tax_rate_differential.csv` | Tax rate comparison by year |
| `03_md_monthly_cigarettes.csv` | Maryland monthly cigarette stamp revenue (60 data points) |
| `04_md_monthly_otp.csv` | Maryland monthly OTP revenue (60 data points) |
| `05_policy_events.csv` | Key policy events timeline |
| `tobacco_visualizations_guide.py` | Python code to reproduce all 7 charts |
| `fig1_cigarette_revenue_comparison.png` | VA vs MD cigarette revenue trend |
| `fig2_otp_revenue_comparison.png` | OTP revenue growth comparison |
| `fig3_grouped_bar_cigarette_otp.png` | Cigarette vs OTP grouped bar chart |
| `fig4_tax_rate_differential.png` | Tax rate gap visualization |
| `fig5_yoy_change.png` | Year-over-year % change comparison |
| `fig6_md_monthly_heatmap.png` | Maryland monthly revenue heatmap |
| `fig7_stacked_area_total_revenue.png` | Total revenue composition |

---

## Data Sources

All data confirmed from official government sources:

- **Virginia:** Virginia Department of Taxation Annual Report FY2025, Table 5.2
  https://www.tax.virginia.gov/annual-reports

- **Maryland:** Maryland Alcohol, Tobacco, and Cannabis Commission Annual Reports FY2021–FY2025
  https://atcc.maryland.gov/resources/publications/reports/

- **US Census Bureau:** Annual Survey of State Government Tax Collections (STC)
  https://www.census.gov/programs-surveys/stc/data/datasets.html

---

## How to Reproduce the Visualizations
```bash
pip install matplotlib numpy
python tobacco_visualizations_guide.py
```

All 7 figures will be saved as PNG files in your working directory.

---

## Policy Context

| Fiscal Year | Virginia Rate | Maryland Rate | Gap |
|-------------|--------------|---------------|-----|
| FY2021 | $0.60/pack | $3.75/pack | $3.15 |
| FY2022 | $0.60/pack | $3.75/pack | $3.15 |
| FY2023 | $0.60/pack | $3.75/pack | $3.15 |
| FY2024 | $0.60/pack | $5.00/pack | $4.40 |
| FY2025 | $0.60/pack | $5.00/pack | $4.40 |

---

## Citation

If you use this data or code in your research please cite:

> Pasha, M. S. (2026). *Divergent Tobacco Tax Policies and Their Impact on State Tax Revenues and Small Retail Businesses: A Comparative Analysis of Virginia and Maryland, 2021–2025.* SSRN. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6491418

---

## License

MIT License — free to use with attribution.
