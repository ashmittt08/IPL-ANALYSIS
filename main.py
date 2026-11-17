import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("IPL.csv")
# print(df.head)

#check baic info 


# print(df.info())
# print(df.shape)

# print(f"total rows are {df.shape[0]} and columnns are {df.shape[1]}")

#CHECKING NULL VALUES
# print(df.isnull().sum())




# WHICH TEAM WON THE MOSTT MATCHES?
# match_wins = df["match_winner"].value_counts()    #ssaved as a series
# sns.barplot(y= match_wins.index,x=match_wins.values , palette='viridis')
# plt.title("Matches Won by Teams")


#TOSS DECISION TRENDS
# sns.countplot(x=df["toss_decision"], palette="rainbow")
# plt.title("Toss Decision Trends")


# TOSS WINNER VS MATCH WINNER -> compare if the tosss winner team == match winning team 
# count = df[df["toss_winner"] == df["match_winner"]]["match_id"].count()  # 36 out of 74
# percentage =(count * 100/df.shape[0])
# percentage.round(2)

#HOW DO TEAMS WON??   (BY WICKET  OR RUNS)
# sns.countplot(x=df["won_by"])
# plt.title("WON BY")



#KEY PLAYER PERFORMANCES 

# MOST "Player of the match " Awards
count = df["player_of_the_match"].value_counts().head(10)    #takes top 10 values
sns.barplot(x=count.values , y=count.index , palette="mako")
plt.title("TOP 10 PLAYERS")

