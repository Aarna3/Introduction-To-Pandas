import pandas as pd

print("PART 1: Panda Series")
scores = [98500, 87200, 76400, 65100, 54800]
players = pd.Series(scores, index=["NightWolf", "StarBlaze", "PixelKing", "CyberFox", "IronStorm"])
print(players)

print()
print("PART 2: Pandas DataFrame")
data = {
    "Player": ["NightWolf", "StarBlaze", "PixelKing", "CyberFox", "IronStorm"],
    "Level": [42, 38, 35, 30, 27],
    "Score": [98500, 87200, 76400, 65100, 54800],
    "Wins": [210, 185, 162, 140, 118]

}
df = pd.DataFrame(data)
print(df)

print("Row 0(top player):")
print(df.loc[0])
print()
print("Rows 2 and 3")
print(df.loc[2:3])

full_df = pd.read_csv("leaderboard.csv")
print(full_df.head())
print()
print("Last 3 rows(tail):")
print(full_df.tail(3))
print()
print("Dataset info:")
print(full_df.info())

print("Rows with missing values removed (dropna):")
clean_df = full_df.dropna()
print(clean_df.to_string())
print()
print("Missinhg values filled with 0 (fillna)")
filled_df = full_df.fillna(0)
print(filled_df.to_string())