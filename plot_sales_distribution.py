# plot_sales_distribution.py
import os, pandas as pd, matplotlib.pyplot as plt
HERE = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
DATA_DIR = os.path.join(ROOT, 'data')
OUTPUT_DIR = os.path.join(ROOT, 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

pop = pd.read_csv(os.path.join(DATA_DIR, 'retail_population.csv'))
sample = pd.read_csv(os.path.join(ROOT, 'output', 'stratified_sample.csv')) if os.path.exists(os.path.join(ROOT, 'output', 'stratified_sample.csv')) else None

# Population distribution
fig, ax = plt.subplots(figsize=(8,6))
pop['monthly_sales'].hist(bins=50, ax=ax)
ax.set_title('Population Monthly Sales Distribution')
ax.set_xlabel('Monthly Sales')
ax.set_ylabel('Count')
plt.tight_layout()
out1 = os.path.join(OUTPUT_DIR, 'pop_sales_hist.png')
fig.savefig(out1)
plt.close(fig)

if sample is not None:
    fig, ax = plt.subplots(figsize=(8,6))
    sample['monthly_sales'].hist(bins=50, ax=ax)
    ax.set_title('Sample Monthly Sales Distribution')
    ax.set_xlabel('Monthly Sales')
    ax.set_ylabel('Count')
    plt.tight_layout()
    out2 = os.path.join(OUTPUT_DIR, 'sample_sales_hist.png')
    fig.savefig(out2)
    plt.close(fig)
    print('Wrote', out1, out2)
else:
    print('Wrote', out1)
