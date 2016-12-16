import pandas as pd
import numpy as np

def didSurvive(sex, embarked, age):
    return np.logical_or(sex == "female", np.logical_and(age <= 10, embarked == 'C')).astype(int)


titanic_df = pd.read_csv("test.csv")

submission = pd.DataFrame({
    "PassengerId": titanic_df["PassengerId"],
    "Survived": didSurvive(titanic_df["Sex"], titanic_df["Embarked"], titanic_df["Age"])
})
submission.to_csv('titanic-predictions.csv', index=False)
