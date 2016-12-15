import pandas as pd

titanic_df = pd.read_csv("train.csv")
print(titanic_df['Survived'].value_counts())

#TODO - how can I divide these values by eachother to get the ratio?
print(titanic_df['Pclass'].value_counts())
print(titanic_df.loc[titanic_df['Survived'] == 1]['Pclass'].value_counts())
