import random
import time
import pandas as pd


class Player():
    NAMELIST = list(pd.read_excel('names.xlsx', 'Sheet1', index_col=None, na_values=['NA'])['NAMES'])

    def __init__(self, control):
        if control == 'AI':
            self.name = random.choice(Player.NAMELIST)
            Player.NAMELIST.remove(self.name)
            # print('created an AI player: ' + self.name)
        elif control == 'Human':
            pass

    def vote(self, mission):
        if random.random() < 0.5:
            mission.current_vote += 1

    def __repr__(self):
        return self.name


class Mission():
    MISSION_PLAYERS = {5: (2, 3, 2, 3, 3), 6: (2, 3, 4, 3, 4), 7: (2, 3, 3, 4, 4), 8: (3, 4, 4, 5, 5), 9: (3, 4, 4, 5, 5), 10: (3, 4, 4, 5, 5)}

    def __init__(self, mission, game):
        self.mission_no = mission
        self.fail_cards = 0
        self.current_vote = 0
        self.vote_fail_count = 0
        self.game = game
        self.nominated = []
        self.players_needed = self.MISSION_PLAYERS[len(self.game.players)][self.mission_no - 1]

    def play(self):
        def nominate():
            self.nominated = random.sample(self.game.players, self.players_needed)
            print('{} has nominated {} to go on the mission'.format(self.game.leader, ', '.join([x.name for x in self.nominated])))

        def start_vote():
            def execute_mission():
                print('')
                mission_outcome = 'Success'
                for player in self.nominated:
                    if player.team == 'Spy':
                        # Spy behavior here is always fail
                        print('Fail', end=' ')
                        mission_outcome = 'Failure'
                    else:
                        print('Success', end=' ')
                print()
                if mission_outcome == 'Success':
                    print('The mission was a success')
                    self.game.mission_successes += 1
                else:
                    print('The mission was a failure')
                    self.game.mission_failures += 1

            self.current_vote = 0
            for player in self.game.players:
                player.vote(self)
            if self.current_vote > len(self.game.players) // 2:
                print('The vote passed {} to {}'.format(self.current_vote, len(self.game.players) - self.current_vote))
                execute_mission()
            else:
                self.vote_fail_count += 1
                print('The vote failed {} to {}'.format(len(self.game.players) - self.current_vote, self.current_vote))
                if self.vote_fail_count == 5:
                    print('There were 5 consecutive vote failures. Mission {} ends in failure.'.format(str(self.mission_no)))
                    self.game.mission_failures += 1
                    return
                nominate()
                start_vote()

        def next_leader():
            if self.game.players.index(self.game.leader) == len(self.game.players) - 1:
                self.game.leader = self.game.players[0]
            else:
                self.game.leader = self.game.players[self.game.players.index(self.game.leader) + 1]
            print('{} is the new leader'.format(self.game.leader.name))

        print()
        print('MISSION {} - {} AGENTS NEEDED'.format(str(self.mission_no), self.players_needed))
        if self.mission_no != 1:
            next_leader()
        nominate()
        start_vote()


class Game():
    PLAYERS_SPIES = {5: 2, 6: 2, 7: 3, 8: 3, 9: 3, 10: 4}

    def __init__(self, players):
        self.missions = []
        self.players = players
        self.mission_successes = 0
        self.mission_failures = 0

        for player in players:
            player.team = 'Resistance'
        for spy in random.sample(players, self.PLAYERS_SPIES[len(players)]):
            spy.team = 'Spy'

        # self.spies = random.sample(players, PLAYERS_SPIES[len(players)])

        print('\nA new game for ' + str(len(self.players)) + ' players has been created')

    def play(self):
        def randomize_leader():
            self.leader = random.choice(self.players)
            print('{} has been randomly chosen as the leader for the first mission'.format(self.leader))

        def print_players():
            for player in self.players:
                print('Name: {:10} Team: {:10}'.format(player.name, player.team))
            print()
            # print('Name:',player,', Team:', player.team)

        def check_game_over():
            if self.mission_successes == 3 or self.mission_failures == 3:
                return True
            else:
                return False

        def show_result():
            if self.mission_successes == 3:
                print()
                print('The game is over and the resistance have won.')
                return 'Resistance'
            if self.mission_failures == 3:
                print()
                print('The game is over and the spies have won.')
                return 'Spies'

        print_players()
        randomize_leader()
        missions = [Mission(x, self) for x in range(1, 6)]
        for mission in missions:
            mission.play()
            print('SCORE: Resistance({}) Spies({})'.format(self.mission_successes, self.mission_failures))
            if check_game_over():
                return show_result()

                # if check_win_loss() == 'Resistance' or 'Spies':

                # nominate
                # vote
                #     success, continue
                #     fail, vote
                # mission
                # check win loss
                # advance mission
