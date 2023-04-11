import pandas as pd

data = pd.read_csv("all_seasons.csv")

df = pd.DataFrame(data)

result = df.columns

result = df.head(10) #1
result = len(df.index) #2
result = df["age"].mean() #3
result = df["player_height"].max() #4
result = df[df["player_height"]==df["player_height"].max()]["player_name"].iloc[0] #5
result = df[(df["age"] >= 20) & (df["age"] < 25)][["team_abbreviation","player_name","age"]].sort_values("age",ascending=False)
#result = df.groupby("player_name").get_group("John Holland")["team_abbreviation"] #7
result = df[df["player_name"] == "John Holland"]["team_abbreviation"].iloc[0]
# result = df.groupby("team_abbreviation")["player_height"].mean() #8
# result = len(df["team_abbreviation"].unique()) #9
result = df.groupby("team_abbreviation")["player_name"].count() #10
result2 = df["team_abbreviation"].value_counts() #10
# result = len(df[df["player_name"].str.contains("and")]) #10
# print(pd.concat([result,result2], axis=1)) #10
result = df[df["player_name"].str.contains("and")] #11
df.dropna(inplace=True)
# def str_find(player_name):
#     if "and" in player_name.lower():
#         return True
#     return False
# result = df[df["player_name"].apply(str_find)]  ###11

print(result)