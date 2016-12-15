import pandas as pd
import numpy as np

def didSurvive(sex, pclass):
    return np.logical_and(sex == "female", pclass == 1).astype(int)


titanic_df = pd.read_csv("test.csv")

submission = pd.DataFrame({
    "PassengerId": titanic_df["PassengerId"],
    "Survived": didSurvive(titanic_df["Sex"], titanic_df["Pclass"])
})
submission.to_csv('titanic-predictions.csv', index=False)
