import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\HP\OneDrive - Higher Education Commission\Desktop\python\global ai impact\ai_impact_jobs_2010_2025.csv", encoding="latin1")

# ── Data Cleaning ──────────────────────────────────────────────
df['Salary'] = df['salary_usd'].fillna(df['salary_usd'].mean())
df['Ai_adoption_stage'] = df['industry_ai_adoption_stage']
df = df.drop('industry_ai_adoption_stage', axis=1)
df = df.drop('salary_usd', axis=1)
df.columns = df.columns.str.capitalize()
df['Ai_keywords'] = df['Ai_keywords'].fillna("None")
df['Ai_skills'] = df['Ai_skills'].fillna("None")

colors = ['#e74c3c', '#2ecc71', '#3498db', '#f39c12', '#9b59b6', '#1abc9c', '#e67e22', '#34495e', '#e91e63']

SAVE_PATH = r"C:\Users\HP\OneDrive - Higher Education Commission\Desktop\python\global ai impact"

# ── CHART 1: Bar Chart — Reskilling Required by Industry (COMPARISON) ──
result = df.groupby('Industry')['Reskilling_required'].sum().sort_values(ascending=False).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='Industry', y='Reskilling_required', data=result, palette=colors)
plt.title('Reskilling Required by Industry')
plt.xlabel('Industry')
plt.ylabel('Number of Jobs Needing Reskilling')
plt.xticks(rotation=45)
plt.ylim(0, 300)
for i, v in enumerate(result['Reskilling_required']):
    plt.text(i, v + 2, str(v), ha='center', fontweight='bold', fontsize=12)
plt.tight_layout()
plt.savefig(f"{SAVE_PATH}\\chart1_reskilling.png", dpi=150, bbox_inches='tight')
plt.close()
print("Chart 1 saved: Bar - Reskilling by Industry")

# ── CHART 2: Pie Chart — AI Job Displacement Risk (PERCENTAGES) ──
result2 = df['Ai_job_displacement_risk'].value_counts()

plt.figure(figsize=(8, 8))
colors2 = ['#2ecc71', '#f39c12', '#e74c3c']
wedges, texts, autotexts = plt.pie(
    result2.values,
    labels=result2.index,
    autopct='%1.1f%%',
    colors=colors2,
    startangle=90,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)
for text in autotexts:
    text.set_fontsize(13)
    text.set_fontweight('bold')
plt.title("AI Job Displacement Risk (%)", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(f"{SAVE_PATH}\\chart2_ai_job_displacement_risk.png", dpi=150, bbox_inches='tight')
plt.close()
print("Chart 2 saved: Pie - AI Job Displacement Risk")

# ── CHART 3: Bar Chart — Automation Risk Score by Industry (COMPARISON) ──
result4 = df.groupby('Industry')['Automation_risk_score'].mean().sort_values(ascending=True).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='Automation_risk_score', y='Industry', data=result4, palette=colors)
plt.title('Average Automation Risk Score by Industry')
plt.xlabel('Risk Score')
plt.ylabel('Industry')
for i, v in enumerate(result4['Automation_risk_score']):
    plt.text(v + 0.002, i, f'{v:.3f}', va='center', fontweight='bold', fontsize=10)
plt.tight_layout()
plt.savefig(f"{SAVE_PATH}\\chart3_automation_risk_score.png", dpi=150, bbox_inches='tight')
plt.close()
print("Chart 3 saved: Bar - Automation Risk Score")

# ── CHART 4: Line Chart — Job Postings Over Years (GROWTH/TREND) ──
result5 = df['Posting_year'].value_counts().sort_index().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(x='Posting_year', y='count', data=result5, color='steelblue', marker='o', linewidth=2.5)
plt.title("AI Job Postings Growth Over Years", fontsize=14, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Number of Job Postings')
plt.tight_layout()
plt.savefig(f"{SAVE_PATH}\\chart4_job_postings_growth.png", dpi=150, bbox_inches='tight')
plt.close()
print("Chart 4 saved: Line - Job Postings Growth")

# ── CHART 5: Histogram — Automation Risk Score Distribution (DATA SPREAD) ──
plt.figure(figsize=(10, 6))
plt.hist(df['Automation_risk_score'].dropna(), bins=20, color='#3498db', edgecolor='white', linewidth=0.8)
plt.title("Distribution of Automation Risk Scores", fontsize=14, fontweight='bold')
plt.xlabel('Automation Risk Score')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig(f"{SAVE_PATH}\\chart5_automation_risk_histogram.png", dpi=150, bbox_inches='tight')
plt.close()
print("Chart 5 saved: Histogram - Automation Risk Score Distribution")

# ── Save Cleaned CSV ───────────────────────────────────────────
df['Reskilling_count'] = df['Reskilling_required'].astype(int)
df.to_csv(f"{SAVE_PATH}\\cleaned_ai_jobs.csv", index=False)
print("CSV saved!")
