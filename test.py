import pandas, random

data = pandas.read_csv("data/french_words.csv")

dict = data.to_dict(orient="records")

print(dict)
