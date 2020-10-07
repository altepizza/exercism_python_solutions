

def create_rows(teams):
    table = ['Team                           | MP |  W |  D |  L |  P']
    for team in teams:
        name = list(team.keys())[0]
        scores = team[name]
        row = ''
        row = name + (31 - len(name)) * ' '
        row += '|  {0} |  {1} |  {2} |  {3} |  {4}'.format(
            scores['MP'], scores['W'], scores['D'], scores['L'], scores['P'])
        table.append(row)
    return table


def create_team(teams, team):
    if team not in teams:
        teams[team] = {'MP': 1}
        teams[team]['W'] = 0
        teams[team]['D'] = 0
        teams[team]['L'] = 0
        teams[team]['P'] = 0
        teams[team]['name'] = team
    else:
        teams[team]['MP'] += 1


def count(teams, team_one, team_two, outcome):
    if outcome == 'draw':
        for team in [team_one, team_two]:
            teams[team]['D'] += 1
            teams[team]['P'] += 1
        return None
    elif outcome == 'loss':
        teams[team_one]['L'] += 1
        teams[team_two]['P'] += 3
        teams[team_two]['W'] += 1
    else:
        teams[team_one]['W'] += 1
        teams[team_one]['P'] += 3
        teams[team_two]['L'] += 1


def tally(rows):
    teams = {}
    for row in rows:
        split = row.split(';')

        create_team(teams, split[0])
        create_team(teams, split[1])

        count(teams, split[0], split[1], split[2])
    sorted_teams = sorted(teams, key=lambda x: (
        teams[x]['P']), reverse=True)
    teams = [{key: teams[key]} for key in sorted_teams]
    return create_rows(teams)
