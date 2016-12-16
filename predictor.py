import pandas as pd
import numpy as np

def didSurvive(sex, age):
    return np.logical_or(sex == "female", age >= 15).astype(int)


titanic_df = pd.read_csv("test.csv")

submission = pd.DataFrame({
    "PassengerId": titanic_df["PassengerId"],
    "Survived": didSurvive(titanic_df["Sex"], titanic_df["Age"])
})
submission.to_csv('titanic-predictions.csv', index=False)
