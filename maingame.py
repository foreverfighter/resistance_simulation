# get input for number of players, from 5 to 10
# set number of spies and resistance for each number of players
# set number of players on each mission and successes needed each mission

# game start

# assign spy status to players

# set random player as leader
# choose x random players for mission
# players randomly vote yes or no
# if majority, go_mission(players)

# go mission, check if < 1 players on mission are spies

# check if 3 successes or 3 failures

# set next player as leader, start next mission

from classes import *
df = pd.read_excel('results.xlsx', 'Sheet1', index_col=None, na_values=['NA'])

no_of_players = 0
no_of_games = 0

while no_of_players not in range(5, 11):
    no_of_players = int(input("""\
-----------------------
Welcome to
THE RESISTANCE
-----------------------
How many players? (5-10) """))

players = [Player('AI') for i in range(no_of_players)]

while no_of_games < 1:
    no_of_games = int(input('How many games would you like to simulate, my good sir? '))

for i in range(no_of_games):
    game = Game(players)
    df.loc[len(df)] = game.play()

df.to_excel('results.xlsx', sheet_name='Sheet1')

# import random
# import time

# no_of_players = 0
# player = ''
# players = []
# leader = ''
# nominated_team = []
# current_mission = 0
# spies = []
# resistance = []
# votes = 0
# vote_fail_count = 0
# mission_outcome = ''

# no_of_spies = {5: 2, 6: 2, 7: 3, 8: 3, 9: 3, 10: 4}

# mission_players = {5: (2, 3, 2, 3, 3), 6: (2, 3, 4, 3, 4), 7: (2, 3, 3, 4, 4), 8: (3, 4, 4, 5, 5), 9: (3, 4, 4, 5, 5), 10: (3, 4, 4, 5, 5)}

# print("You've set the number of players to " + str(no_of_players))

# for i in range(no_of_players):
#     player = 'Player ' + str(i + 1)
#     players.append(player)

# spies = random.sample(players, no_of_spies[no_of_players])
# resistance = [x for x in players if x not in spies]

# time.sleep(1)
# print('The spies are ' + ' and '.join(spies))
# # game start setup

# time.sleep(1)
# leader = random.choice(players)
# print(leader + ' has been randomly chosen as the first leader')

# # first mission
# current_mission = 1

# time.sleep(1)
# nominated_team = random.sample(players, mission_players[no_of_players][current_mission - 1])
# print(leader + ' has nominated ' + ' and '.join(nominated_team) + ' for the first mission')

# time.sleep(1)
# votes = 0
# for i in range(no_of_players):
#     if random.random() > 0.5:
#         votes += 1
# if votes > no_of_players // 2:
#     # successful vote
#     mission_outcome = 'Success'
#     for player in nominated_team:
#         if player in spies:
#             mission_outcome = 'Failure'
#     if mission_outcome == 'Success':
#         print('The mission was successful.')
#     else:
#         print('The mission was a failure.')
# else:
#     # unsuccessful vote
#     if players.index(leader) == no_of_players - 1:
#         leader = players[0]
#     else:
#         leader = players[players.index(leader) + 1]
#     print('The vote has failed.\nThe next leader is ' + leader)
