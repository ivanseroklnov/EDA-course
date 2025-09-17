import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    "https://raw.githubusercontent.com/aiedu-courses/eda_and_dev_tools/main/datasets/online_shoppers_intention.csv")
df.drop_duplicates(inplace=True)
median_inf_dur = df['Informational_Duration'].median()
median_prod_dur = df['ProductRelated_Duration'].median()

df['Informational_Duration'].fillna(median_inf_dur, inplace=True)
df['ProductRelated_Duration'].fillna(median_prod_dur, inplace=True)
df.dropna(subset=['ExitRates'], inplace=True)
df['Month'] = df['Month'].replace('aug', 'Aug')
df.to_csv('preprocessed.csv')
