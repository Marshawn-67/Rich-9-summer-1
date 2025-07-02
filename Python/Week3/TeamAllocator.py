import random

players = ["Max",
           "Kauri","Isaiah","Braylen",
           "Taymur","Xavier","Avery",
           "Taqari","Kenlon","Nahum",
           "Kamari","Kristopher","Joseph",
           "Darren","Carl","Walter",
           "Jeffrey","Nishad","JaDen",
           "Joaquin","Jarmauri",
           "Eustace","Semaj","Marshawn"]
def PickTeams (players):
    random.shuffle(players)
team1 = players[:len(players) // 2]
teamCaptain1 = team1[random.randrange(0, 12)]
print ("TEAM 1:")
print("Team 1 Captain " + teamCaptain1)
for player in team1: 
 print(player)
PickTeams(players)

team2 = players[:len(players) // 2]
teamCaptain2 = team2[random.randrange(0, 12)]
print ("TEAM 2:")
print("Team 2 Captain " + teamCaptain2)
for player in team2: 
 print(player)
PickTeams(players)
