
class Team:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.points = 0
        self.matches = 0

    def __str__(self):
        scores = self.name + (31 - len(self.name)) * ' '
        return scores + '|  {0} |  {1} |  {2} |  {3} |  {4}'.format(
            self.matches, self.wins, self.draws, self.losses, self.points)

    def __lt__(self, other):
        if self.points == other.points:
            return self.name < other.name
        return self.points > other.points

    def win(self):
        self.wins += 1
        self.matches += 1
        self.points += 3

    def draw(self):
        self.draws += 1
        self.matches += 1
        self.points += 1

    def lose(self):
        self.losses += 1
        self.matches += 1


def tally(rows):
    teams = []
    for game_result in rows:
        _register_game(teams, game_result)
    teams.sort()
    return _create_scorecard(teams)


def _create_scorecard(teams):
    table = ['Team                           | MP |  W |  D |  L |  P']

    [table.append(str(team)) for team in teams]

    return table


def _find_or_create_team(teams, team_name):
    found_team = next((x for x in teams if x.name == team_name), None)
    if found_team:
        return found_team
    found_team = Team(team_name)
    teams.append(found_team)
    return found_team


def _register_game(teams, game_result):
    team_one, team_two, outcome = game_result.split(';')
    if outcome == 'draw':
        _find_or_create_team(teams, team_one).draw()
        _find_or_create_team(teams, team_two).draw()
    elif outcome == 'loss':
        _find_or_create_team(teams, team_one).lose()
        _find_or_create_team(teams, team_two).win()
    elif outcome == 'win':
        _find_or_create_team(teams, team_one).win()
        _find_or_create_team(teams, team_two).lose()
