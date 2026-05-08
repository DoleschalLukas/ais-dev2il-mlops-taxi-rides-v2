import pandas as pd
import os
import time


print("Time metrics")
t = time.time()
for _ in range(365):
    pd.read_csv('example-data/2025-01-01.taxi-rides.csv')
csv_time = time.time() - t

t = time.time()
for _ in range(365):
    pd.read_parquet('example-data/2025-01-01.taxi-rides.parquet')
pq_time = time.time() - t

print(f'CSV:     {csv_time:.1f}s')
print(f'Parquet: {pq_time:.2f}s')
print(f'Parquet is {csv_time / pq_time:.0f}x faster')

print("Storage metrics")

csv_size = os.path.getsize('example-data/2025-01-01.taxi-rides.csv')
pq_size  = os.path.getsize('example-data/2025-01-01.taxi-rides.parquet')

print(f'CSV:     {csv_size / 1024 / 1024:.1f} MB')
print(f'Parquet: {pq_size  / 1024 / 1024:.1f} MB')
print(f'Parquet is {csv_size / pq_size:.1f}x smaller')

print("Datatype metrics")

df_csv = pd.read_csv('example-data/2025-01-01.taxi-rides.csv')
df_csv['tpep_pickup_datetime']  = pd.to_datetime(df_csv['tpep_pickup_datetime'])
df_csv['tpep_dropoff_datetime'] = pd.to_datetime(df_csv['tpep_dropoff_datetime'])
df_csv['ride_time'] = pd.to_numeric(df_csv['ride_time'])
print(df_csv.dtypes)

df_pq = pd.read_parquet('example-data/2025-01-01.taxi-rides.parquet')
print(df_pq.dtypes)

