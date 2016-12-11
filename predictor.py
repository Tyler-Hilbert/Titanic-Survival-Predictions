import pandas as pd

def didSurvive(sex):
    return (sex == "female").astype(int)


titanic_df = pd.read_csv("test.csv")
submission = pd.DataFrame({
    "PassengerId": titanic_df["PassengerId"],
    "Survived": didSurvive(titanic_df["Sex"])
})
submission.to_csv('titanic-predictions.csv', index=False)
