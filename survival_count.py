import pandas as pd

titanic_df = pd.read_csv("train.csv")
print(titanic_df['Survived'].value_counts())
