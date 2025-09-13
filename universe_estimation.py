# universe_estimation.py
import os
import numpy as np
import pandas as pd

HERE = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
DATA_DIR = os.path.join(ROOT, 'data')
OUTPUT_DIR = os.path.join(ROOT, 'output')
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 1) Create synthetic population of retail outlets
np.random.seed(42)
n_pop = 20000
formats = ['Kirana','Modern Trade','Convenience','Wholesale']
regions = ['North','South','East','West']
pop = pd.DataFrame({
    'store_id': np.arange(1, n_pop+1),
    'format': np.random.choice(formats, size=n_pop, p=[0.6,0.2,0.15,0.05]),
    'region': np.random.choice(regions, size=n_pop),
    'monthly_sales': np.round(np.random.gamma(shape=2.0, scale=20000, size=n_pop)).astype(int)
})
pop.to_csv(os.path.join(DATA_DIR, 'retail_population.csv'), index=False)

# 2) Define strata by format x region
pop['stratum'] = pop['format'] + '_' + pop['region']
strata = pop.groupby('stratum').agg(pop_size=('store_id','count'), avg_sales=('monthly_sales','mean')).reset_index()

# 3) Stratified sampling: allocate sample proportional to stratum size (with minimum)
total_sample = 1000
strata['alloc'] = (strata['pop_size']/strata['pop_size'].sum()*total_sample).round().astype(int)
strata.loc[strata['alloc']<5,'alloc']=5

# Draw sample
samples = []
for _, row in strata.iterrows():
    s = pop[pop['stratum']==row['stratum']].sample(n=row['alloc'], random_state=42)
    s = s.copy()
    s['stratum_pop'] = row['pop_size']
    s['stratum_sample_size'] = row['alloc']
    samples.append(s)
sample_df = pd.concat(samples, ignore_index=True)
sample_df.to_csv(os.path.join(OUTPUT_DIR, 'stratified_sample.csv'), index=False)

# 4) Compute weights and estimate total sales (expansion estimator)
sample_df['weight'] = sample_df['stratum_pop'] / sample_df['stratum_sample_size']
estimate_total = (sample_df['monthly_sales'] * sample_df['weight']).sum()
estimate_mean = (sample_df['monthly_sales'] * sample_df['weight']).sum() / sample_df['stratum_pop'].sum()

results = pd.DataFrame({
    'metric': ['estimated_total_monthly_sales', 'estimated_mean_monthly_sales'],
    'value': [int(estimate_total), float(estimate_mean)]
})
results.to_csv(os.path.join(OUTPUT_DIR, 'estimation_results.csv'), index=False)

print('Universe estimation: generated population and stratified sample.')
