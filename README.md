# ECommerce-Customer-Segmentation
# End-to-End E-Commerce Customer Segmentation & Analytics

An end-to-end data analytics project combining data science (Python) and business intelligence (Power BI) to analyze over 500,000 transaction rows, uncover behavioral purchasing patterns, and build an executive-ready risk tracking dashboard.

## 📊 Dashboard Preview
![Dashboard Screenshot](./Images/dashboard_screenshot.png) 
*(Note: Replace this path with the actual path to your saved dashboard screenshot image)*

## 🛠️ Project Workflow & Technical Breakdown

### 1. Data Engineering & Analytics (Python)
- Cleaned and prepared raw retail transactional datasets using **Pandas**.
- Engineered custom transaction metrics to isolate user behavioral trends.

### 2. Business Intelligence & Matrix Modeling (Power BI & DAX)
- Imported processed datasets into Power BI Desktop to build a centralized data model.
- Wrote custom **DAX** expressions to calculate real-time behavioral metrics dynamically:
  - **Recency:** `DATEDIFF(data[InvoiceDate], MAX(data[InvoiceDate]), DAY)` to measure customer inactivity periods.
  - **Frequency:** Automated unique `InvoiceNo` calculations partitioned by `CustomerID`.
- Developed custom classification frameworks (`SWITCH`/`TRUE` logic) to bin customer interaction scores into actionable **Recency** and **Frequency** risk buckets.
- Configured a dynamic **Matrix Heatmap** early-warning system using gradient conditional formatting to spotlight high-value churn risks.

## 📈 Executive Insights & Impact
- **Retention Tracking:** The behavioral risk matrix isolates high-frequency customers stalling in the $91\text{+ days}$ inactive zone, signaling critical win-back opportunities.
- **Geographic Concentrations:** Mapped global spending distribution via relative bubble sizes, allowing marketing teams to immediately optimize territorial ad spends.
- **Operational Optimization:** Provides a data-driven blueprint to replace generic marketing blasts with precise, segment-targeted campaigns.

---
*Developed as a comprehensive personal data analytics case study.*
