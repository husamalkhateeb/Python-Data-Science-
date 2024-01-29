import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# import xlrd
# import xlwt
import  seaborn as sns
#from ggplot import *
import openpyxl
from scipy.stats import norm
from statistics import *

filename =r'/home/hughsamm/Documents/study lmao/Year 3 fall/Sercurity/project/Players_WorldCup_Wins.csv'
filename1 =r'/home/hughsamm/Documents/study lmao/Year 3 fall/Sercurity/project/RecentProfessionalPlayers.csv'
filename2 = r'/home/hughsamm/Documents/study lmao/Year 3 fall/Sercurity/project/WorldCupMatches.csv'

worldCupWins = pd.read_csv(filename)
players = pd.read_csv(filename1)
matches = pd.read_csv(filename2)


worldCupWins = worldCupWins.rename(columns = {'Other appearances':'Other_appearances'})



LFP = players[(players.Club_Position == 'LW') | (players.Club_Position == 'LB') | (players.Club_Position == 'LM') | (players.Club_Position == 'LCB') | (players.Club_Position == 'LS')]

LP_RF = LFP[(LFP.Preffered_Foot == 'Right')]
LP_LF = LFP[(LFP.Preffered_Foot == 'Left')]

LP_RF_LMAO = LP_RF.Preffered_Foot.to_numpy()
LP_LF_LMAO = LP_LF.Preffered_Foot.to_numpy()

lengthOfL = LP_RF_LMAO.size
lengthOfR = LP_LF_LMAO.size
all_LP = lengthOfL+lengthOfR




RFP = players[(players.Club_Position == 'RW') | (players.Club_Position == 'RB') | (players.Club_Position == 'RM') | (players.Club_Position == 'RCB') | (players.Club_Position == 'RS')]

RP_RF = RFP[(RFP.Preffered_Foot == 'Right')]
RP_LF = RFP[(RFP.Preffered_Foot == 'Left')]

RP_RF_LMAO = RP_RF.Preffered_Foot.to_numpy()
RP_LF_LMAO = RP_LF.Preffered_Foot.to_numpy()

lengthOfL1 = RP_RF_LMAO.size
lengthOfR1 = RP_LF_LMAO.size
all_RP = lengthOfL+lengthOfR

allPos = all_LP+all_RP




perLPRF = (lengthOfL/allPos) * 100
perLPLF = (lengthOfR/allPos) * 100
perRPRF = (lengthOfL1/allPos) * 100
perRPLF = (lengthOfR1/allPos) * 100

width = 0.10       
labels = ['Left Footed Players', 'Right Footed Players']

fig, ax = plt.subplots()
names = []
ax.bar(labels[0], perLPLF, color='blue',edgecolor='white', label = 'Left Position, Left Foot')
ax.bar(labels[0], perLPRF, bottom=perLPLF, color='deepskyblue',edgecolor='white', label = 'Left Position, Right Foot')
ax.bar(labels[1], perRPRF, color='red',edgecolor='white', label = 'Right Position, Right Foot')
ax.bar(labels[1], perRPLF, bottom=perRPRF, color='indianred',edgecolor='white', label = 'Right Position, Left Foot')


ax.set_ylabel('Percentage %')
ax.set_title('Percentage by Preffered Foot')

ax.legend()
plt.show()






#####BRAZIL######

Brazil = worldCupWins[(worldCupWins.Team == 'Brazil')]
years = Brazil.Years.to_numpy()
ndYears = np.unique(years)
newYears = []
for i in ndYears:
    newYears.append(i.replace(","," ").lower().split())
newnewYears = np.concatenate(newYears)
newnewYears = np.unique(newnewYears)
########URUGUAY##############
Uruguay = worldCupWins[(worldCupWins.Team == 'Uruguay')]
yearsU = Uruguay.Years.to_numpy()
ndYearsU = np.unique(yearsU)
newYearsU = []
for i in ndYearsU:
    newYearsU.append(i.replace(","," ").lower().split())
newnewYearsU = np.concatenate(newYearsU)
newnewYearsU = np.unique(newnewYearsU)
######ARGENTINA###############
Argentina = worldCupWins[(worldCupWins.Team == 'Argentina')]
yearsA = Argentina.Years.to_numpy()
ndYearsA = np.unique(yearsA)
newYearsA = []
for i in ndYearsA:
    newYearsA.append(i.replace(","," ").lower().split())
newnewYearsA = np.concatenate(newYearsA)
newnewYearsA = np.unique(newnewYearsA)

###########France####################

France = worldCupWins[(worldCupWins.Team == 'France')]
yearsF = France.Years.to_numpy()
ndYearsF = np.unique(yearsF)
newYearsF = []
for i in ndYearsF:
    newYearsF.append(i.replace(","," ").lower().split())
newnewYearsF = np.concatenate(newYearsF)
newnewYearsF = np.unique(newnewYearsF)

##############ITALY####################
Italy = worldCupWins[(worldCupWins.Team == 'Italy')]
yearsI = Italy.Years.to_numpy()
ndYearsI = np.unique(yearsI)
newYearsI = []
for i in ndYearsI:
    newYearsI.append(i.replace(","," ").lower().split())
newnewYearsI = np.concatenate(newYearsI)
newnewYearsI = np.unique(newnewYearsI)

##############SPAIN####################
Spain = worldCupWins[(worldCupWins.Team == 'Spain')]
yearsS = Spain.Years.to_numpy()
ndYearsS = np.unique(yearsS)
newYearsS = []
for i in ndYearsS:
    newYearsS.append(i.replace(","," ").lower().split())
newnewYearsS = np.concatenate(newYearsS)
newnewYearsS = np.unique(newnewYearsS)
#############GERMANY####################
newWorldCupWins = worldCupWins.replace(to_replace=r'West Germany', value='Germany', regex=True)
Germany = newWorldCupWins[(newWorldCupWins.Team == 'Germany')]
worldCupWins = newWorldCupWins.rename(columns = {'Other appearances':'Other_appearances'})

yearsG = Germany.Years.to_numpy()
ndYearsG = np.unique(yearsG)
newYearsG = []
for i in ndYearsG:
    newYearsG.append(i.replace(","," ").lower().split())
newnewYearsG = np.concatenate(newYearsG)
newnewYearsG = np.unique(newnewYearsG)
#############England#####################
England = worldCupWins[(worldCupWins.Team == 'England')]
yearsE = England.Years.to_numpy()
ndYearsE = np.unique(yearsE)
newYearsE = []
for i in ndYearsE:
    newYearsE.append(i.replace(","," ").lower().split())
newnewYearsE = np.concatenate(newYearsE)
newnewYearsE = np.unique(newnewYearsE)


bnum = newnewYears
unum = newnewYearsU
anum = newnewYearsA
fnum = newnewYearsF
inum = newnewYearsI
snum = newnewYearsS
gnum = newnewYearsG
enum = newnewYearsE
numOfAll=[]
numOfAll = np.concatenate((bnum, unum, anum, fnum, inum, snum, gnum, enum))
allWorldCups = numOfAll.size
bavg = newnewYears.size/allWorldCups
uavg = newnewYearsU.size/allWorldCups
aavg = newnewYearsA.size/allWorldCups
favg = newnewYearsF.size/allWorldCups
iavg = newnewYearsI.size/allWorldCups
savg = newnewYearsS.size/allWorldCups
gavg = newnewYearsG.size/allWorldCups
eavg = newnewYearsE.size/allWorldCups


labels = ['South America', 'Europe']
brazil = bavg * 100
uruguay = uavg * 100
argentina = aavg* 100
italy = iavg* 100
germany = gavg* 100
france = favg* 100
spain = savg* 100
england = eavg* 100

width = 0.10

fig, ax = plt.subplots()
names = []
ax.bar(labels[0], brazil, color='gold',edgecolor='white', label = 'Brazil')
ax.bar(labels[0], uruguay, bottom=brazil, color='cornsilk',edgecolor='white', label = 'Uruguay')
ax.bar(labels[0], argentina, bottom=brazil+uruguay, color='lightskyblue',edgecolor='white', label = 'Argentina')
ax.bar(labels[1], italy, color='slateblue',edgecolor='white', label = 'Italy')
ax.bar(labels[1], germany, bottom=italy, color='palevioletred',edgecolor='white', label = 'Germany')
ax.bar(labels[1], france, bottom=germany+italy, color='b',edgecolor='white', label = 'France')
ax.bar(labels[1], spain, bottom=germany+italy+france, color='yellow',edgecolor='white', label = 'Spain')
ax.bar(labels[1], england, bottom=germany+italy+france+spain, color='grey',edgecolor='white', label = 'England')

ax.set_ylabel('Percentage %')
ax.set_title('Percentage by Continent')

ax.legend()
plt.show()


################################################################################################

matches = matches.rename(columns = {'Home Team Goals':'Home_Team_Goals'})
matches = matches.rename(columns = {'Away Team Goals':'Away_Team_Goals'})
matches = matches.rename(columns = {'Half-time Home Goals':'Half_time_Home_Goals'})
matches = matches.rename(columns = {'Half-time Away Goals':'Half_time_Away_Goals'})






halfTimeScore = (matches["Half_time_Home_Goals"][0:852] - matches["Half_time_Away_Goals"][0:852]).to_numpy()

fullTimeScore = (matches["Home_Team_Goals"][0:852] - matches["Away_Team_Goals"][0:852]).to_numpy()
n = np.subtract(fullTimeScore, halfTimeScore) 
draw = 0
comeBackWin = 0
win = 0
lose = 0
hTLose = 0
for i in range(0, fullTimeScore.size):

    if (halfTimeScore[i] < 0 and fullTimeScore[i] > 0):
        comeBackWin += 1
        hTLose += 1
    elif fullTimeScore[i] == 0:
        draw += 1
    elif (fullTimeScore[i] > 0 and halfTimeScore[i] > 0):
        win += 1
    elif (fullTimeScore[i] < 0):
        lose += 1


totalGamesWon = win + comeBackWin
winPer = (win / totalGamesWon) * 100
cbWinPer = (comeBackWin / totalGamesWon) * 100
losePer = (lose / hTLose) * 100
cbWinPer1 = (cbWinPer/hTLose) * 100
values = [winPer, cbWinPer]
Ans= ['Games Won The Whole Game','Games Won With a Comeback']
plt.pie(values,labels = Ans,autopct = '%1.1f%%',startangle=90,explode =(0,.1))
plt.legend()
plt.title('Percentage of Games Won with a Comeback Relative to All the Games Won')
plt.show()

values1 = [losePer, cbWinPer1]
Ans1= ['Percentage of Games Lost Relative to Games Lost After Half Time','Percentage of Games Won With a Comeback Relative to Games Lost After Half Time']
plt.pie(values1,labels = Ans1,autopct = '%1.1f%%',startangle=90,explode =(0,.1))
plt.legend()
plt.title('Percentage of Games Won After a Comeback Relative To Games Lost')
plt.show()
#########################################################################################################3

topPlayers = players[(players.Rating >= 86)]

avgOfAll = topPlayers.groupby((['Club'])).mean()



avgOfAll = avgOfAll.reset_index()

avg = avgOfAll.drop(columns=['Contract_Expiry'])

avg['Club'].str.split()

avg['Club'] = avg['Club'].str.split().str[0]
plt.scatter('Club', 'Stamina', c='Strength', data=avg, cmap='viridis')
plt.xlabel('Clubs')
plt.ylabel('Stamina')
plt.colorbar(label = 'Strength Color Bar');
plt.show()


#########################################################################################################3




sorted_attendance = matches.sort_values(by=['Attendance'], ascending=False)
top_attendances = sorted_attendance.head(10)
top_home = top_attendances.loc[:,"Home Team Initials"]
#(type(top_home))
top_away = top_attendances.loc[:,"Away Team Initials"]

top_all =    pd.concat([top_away,top_home])
#(top_all.value_counts())

x = top_all.value_counts()
sns.barplot(x= x.index,y = x.values)
plt.show()
#########################################################################################################3

height = pd.DataFrame(players["Height"])
height.dropna()
# (height)
height['Height'].str.split()

height['Height'] = height['Height'].str.split().str[0]
height["Height"] = height["Height"].astype(str).astype(int)
#(height)
#(height.count(),'\n',height.sum())
#(height.describe())
mean = height.describe().mean()
std = height.describe().std()
x_values = np.arange(160, 200, 1)
y_values = norm(mean, std)




height['Height'].plot(kind='hist')
plt.show()

