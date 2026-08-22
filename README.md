🤖 AI Impact on Jobs — Analytics Dashboard (2010–2025)

A data analytics project exploring how Artificial Intelligence is reshaping the global job market — analyzing automation risk, reskilling demand, and job displacement trends across 10 major industries from 2010 to 2025.

Show Image Show Image

📌 Overview

This project analyzes a 5,000-row dataset to uncover how AI adoption is affecting the global workforce — which industries are most exposed to automation, where reskilling demand is highest, and how job postings have shifted over a 15-year window. The workflow covers data cleaning and exploratory analysis in Python, followed by an interactive Power BI dashboard for stakeholder-facing exploration.

🛠️ Tools & Technologies
Category	Tools
Data Cleaning & EDA	Python — pandas, matplotlib, seaborn
Dashboard	Power BI
Version Control	Git & GitHub
📂 Dataset
Source: Kaggle — AI Impact on Jobs (2010–2025)
Size: 5,000 rows
Key columns: Industry, Salary, Automation Risk Score, AI Adoption Stage, Reskilling Required, Displacement Risk, Posting Year
🔍 Key Findings
Healthcare and Energy show the highest automation risk (above 0.60) — most vulnerable to AI-driven displacement
Finance and Tech show the lowest risk — AI appears to be augmenting these roles rather than replacing them
Job postings peaked around 2020–2022, reflecting a post-pandemic surge in demand for AI-skilled professionals
Displacement risk is nearly evenly split — 34% High, 34% Medium, 32% Low — indicating AI's impact is broad rather than concentrated
Reskilling demand is highest in Manufacturing, Healthcare, and Retail
📊 Visualizations
Chart	Type	Insight
Reskilling Required by Industry	Bar chart	Cross-industry comparison
Job Postings Growth (2010–2025)	Line chart	Trend over time
Automation Risk Score Distribution	Histogram	Spread of risk across dataset
AI Job Displacement Risk	Pie chart	Proportional breakdown
Automation Risk Score by Industry	Bar chart	Industry-level comparison
📁 Repository Structure
├── AI_Jobs_Dashboard.pbix        # Interactive Power BI dashboard
├── global_impact.py               # Data cleaning & analysis script
├── chart1_reskilling.png
├── chart2_ai_job_displacement_risk.png
├── chart3_automation_risk_score.png
├── chart4_job_postings_growth.png
├── chart5_automation_risk_histogram.png
└── README.md
🚀 How to Run
Clone the repo
Run global_impact.py to reproduce the cleaning and EDA steps
Open AI_Jobs_Dashboard.pbix in Power BI Desktop to explore the interactive dashboard

Built as part of independent data analytics practice — see my portfolio for more.
