# plot_stratum_counts.py
import os
import pandas as pd
import matplotlib.pyplot as plt

HERE = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
DATA_DIR = os.path.join(ROOT, 'data')
OUTPUT_DIR = os.path.join(ROOT, 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

pop = pd.read_csv(os.path.join(DATA_DIR, 'retail_population.csv'))
pop['stratum'] = pop['format'] + '_' + pop['region']
counts = pop['stratum'].value_counts().head(10)

fig, ax = plt.subplots(figsize=(8,6))
counts.plot(kind='bar', ax=ax)
ax.set_title('Top 10 Strata by Population (example)')
ax.set_ylabel('Count')
ax.set_xlabel('Stratum')
plt.tight_layout()
out = os.path.join(OUTPUT_DIR, 'stratum_counts.png')
fig.savefig(out)
plt.close(fig)
print('Wrote', out)
