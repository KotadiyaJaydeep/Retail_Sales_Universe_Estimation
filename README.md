# Retail_Sales_Universe_Estimation

This repository contains three end-to-end projects that simulate **real-world Product Design & Enhancement (PDE) workflows** .  
The projects demonstrate **sampling design, sample optimization, and retail index construction** using synthetic FMCG retail data.  

All datasets are **synthetic** and generated in Python for demonstration purposes.

---

## 📌 Projects Included

### 1. Retail Sales Universe Estimation
- **Objective**: Estimate the FMCG retail sales universe across store formats and regions.  
- **Methods**: Stratified sampling, weight computation, expansion estimator.  
- **Outputs**:
  - Synthetic retail population (`retail_population.csv`)
  - Stratified sample with weights (`stratified_sample.csv`)
  - Weighted sales estimates (`estimation_results.csv`)
  - Validation plots (sample vs population sales distribution)
- **Dashboard**: Power BI to validate sample composition, weight distributions, and estimation accuracy.

---

### 2. Store Sample Design Optimization
- **Objective**: Optimize sample selection of retail outlets to improve representativeness.  
- **Methods**: K-Means clustering, proportional allocation, stratification by region.  
- **Outputs**:
  - Selected representative sample (`selected_sample.csv`)
  - Cluster-level selection summary (`selection_summary.csv`)
  - Visualizations: cluster counts, population vs sample sales distribution
- **Dashboard**: Power BI to compare population vs selected sample across clusters and formats.

---

### 3. Retail Index Construction & Monitoring
- **Objective**: Build and monitor a retail price index from sampled retail data.  
- **Methods**: Laspeyres-like index, rolling averages for smoothing, anomaly detection.  
- **Outputs**:
  - Synthetic SKU × Store × Month price dataset (`price_samples.csv`)
  - Retail price index time series (`index_timeseries.csv`)
  - Visualizations: index trend line, pct change bars, anomaly flags
- **Dashboard**: Power BI to track index trends, detect anomalies, and drill down to SKU/store level.

---

## 📂 Repository Structure
NIQ_Projects/
│
├── Retail_Sales_Universe_Estimation/
│ ├── data/ # synthetic population data
│ ├── notebooks/ # main Python scripts
│ ├── output/ # sampled datasets & results
│ └── plots/ # visualization scripts
│
├── Store_Sample_Design_Optimization/
│ ├── data/
│ ├── notebooks/
│ ├── output/
│ └── plots/
│
├── Retail_Index_Construction_and_Monitoring/
│ ├── data/
│ ├── notebooks/
│ ├── output/
│ └── plots/
│
└── figures/ # Power BI dashboard mockups

yaml
Copy code

---

## 🚀 How to Run

1. Clone this repo:
```bash
git clone https://github.com/yourusername/NIQ-Projects.git
cd NIQ-Projects
Create environment and install dependencies:

bash
Copy code
python -m venv niq_env
source niq_env/bin/activate      # Windows: niq_env\Scripts\activate
pip install pandas numpy scikit-learn matplotlib pillow
Run project scripts to generate synthetic data and outputs:

bash
Copy code
# Universe Estimation
python Retail_Sales_Universe_Estimation/notebooks/universe_estimation.py

# Sample Design Optimization
python Store_Sample_Design_Optimization/notebooks/sample_design_optimization.py

# Retail Index
python Retail_Index_Construction_and_Monitoring/notebooks/retail_index.py
Generate plots for visualization:

bash
Copy code
python Retail_Sales_Universe_Estimation/plots/plot_stratum_counts.py
python Retail_Sales_Universe_Estimation/plots/plot_sales_distribution.py
python Store_Sample_Design_Optimization/plots/plot_cluster_counts.py
python Store_Sample_Design_Optimization/plots/plot_selected_vs_pop_sales.py
python Retail_Index_Construction_and_Monitoring/plots/plot_index_timeseries.py
python Retail_Index_Construction_and_Monitoring/plots/plot_index_pct_change.py
📊 Power BI Dashboards
Import CSV outputs into Power BI.

Suggested visuals:

Universe Estimation → sample composition bar chart, population vs sample sales distribution, KPI cards for estimates.

Sample Optimization → cluster allocation bar chart, selection summary table, population vs sample comparison.

Index Monitoring → time-series line chart of index, pct change bars, anomaly flag markers.

Example mockups are available in the figures/ folder:

universe_dashboard_mockup_v2.png

sample_design_dashboard_mockup_v2.png

index_dashboard_mockup_v2.png

🛠️ Tools & Libraries
Python: pandas, numpy, scikit-learn, matplotlib, pillow

Power BI: dashboards for validation and monitoring

Methodologies: stratified sampling, clustering, weighting, index construction, anomaly detection

🔑 Key Learnings
Designed representative retail sampling methodologies.

Optimized sample design using clustering and proportional allocation.

Built and monitored a Retail Price Index with smoothing and anomaly detection.

Produced Power BI dashboards to validate and present insights.

📌 Notes
