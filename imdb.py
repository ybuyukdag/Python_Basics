import pandas as pd

data = pd.read_csv("IMDB_Bottom250.csv")

df = pd.DataFrame(data)

result = df.head()
#result = df.columns
#result = df.info
result = df.head(10)
result = df.tail(10)
result = df["Title"].head()
result = df[["Title","Ratings.Value"]].head()
#result = df.columns
result = df[["Title","Ratings.Value"]].tail(7)
# result = df[5:10][["Title","Ratings.Value"]].head()
result = df[df["imdbRating"] >= 2.0][["Title","imdbRating"]].head()
# #result = df[["Title","Ratings.Value"]].head()
# # result = type(df)

print(result)