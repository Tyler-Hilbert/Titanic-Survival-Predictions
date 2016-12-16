import pandas as pd

# Print how many people lived with a field
def printFieldSurvival(df, field):
    print(field)
    #TODO - how can I divide these values by eachother to get the ratio?
    print("Number of people:")
    print(df[field].value_counts())
    print("Number of people survived:")
    print(df.loc[df['Survived'] == 1][field].value_counts())
    print()

titanic_df = pd.read_csv("train.csv")

# Print amount survived
print("Amount survived")
print(titanic_df['Survived'].value_counts())
print();

# Print fields
printFieldSurvival(titanic_df, 'Pclass')
printFieldSurvival(titanic_df, 'SibSp')
printFieldSurvival(titanic_df, 'Embarked')
printFieldSurvival(titanic_df, 'Parch')


# Create graph
print (titanic_df['Age'].hist(bins=15))
