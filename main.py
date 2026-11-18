import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("IPL.csv")
# print(df.head)

#checking baic info 
# print(df.info())
# print(df.shape)

# print(f"total rows are {df.shape[0]} and columnns are {df.shape[1]}")

#CHECKING NULL VALUES
# print(df.isnull().sum())




# WHICH TEAM WON THE MOSTT MATCHES?
match_wins = df["match_winner"].value_counts()    #ssaved as a series
sns.barplot(y= match_wins.index,x=match_wins.values , palette='viridis')
plt.title("Matches Won by Teams")


#TOSS DECISION TRENDS
sns.countplot(x=df["toss_decision"], palette="rainbow")
plt.title("Toss Decision Trends")


# TOSS WINNER VS MATCH WINNER -> compare if the tosss winner team == match winning team 
count = df[df["toss_winner"] == df["match_winner"]]["match_id"].count()  # 36 out of 74
percentage =(count * 100/df.shape[0])
percentage.round(2)

#HOW DO TEAMS WON??   (BY WICKET  OR RUNS)
sns.countplot(x=df["won_by"])
plt.title("WON BY")



#KEY PLAYER PERFORMANCES 

# MOST "Player of the match " Awards
count = df["player_of_the_match"].value_counts().head(10)    #takes top 10 values
sns.barplot(x=count.values , y=count.index , palette="mako")
plt.title("TOP 10 PLAYERS")

#2 TOP SCORERS
high = df.groupby("top_scorer")["highscore"].sum().sort_values(ascending=False).head(2)      #gives top 2 high scorers
high.plot(kind= 'bar')
plt.title("TOP 2 SCORERS")



#VENUE ANALYSIS

#MOST MATCHES PLAYED BY VENUE

venue_count = df['venue'].value_counts()
sns.barplot(y=venue_count.index , x=venue_count.values , palette='rainbow')
plt.title("VENUE")


#CUSTOM
## WHO WON THE HIGHEST MARGIN BY RUNS?
df[df['won_by'] =='Runs'].sort_values(by = 'margin' , ascending=False).head(1)[['match_winner' , 'margin']]

#WHICH PLAYER HAS THE HIGHESST INDIVIDUAL SCORE
df[df['highscore']==df['highscore'].max()][[['top_scorer','highscore']]]


