import matplotlib.pyplot as plt
import fetch_player_statistics as fp


def plot_NBA_player_statistics(teams, best_scores):
    """Plot NBA player statistics. In this case, just PPG"""
    count_so_far = 0
    all_names = []

    # iterate through each team and the
    for team, players in teams.items():
        # pick the color for the team, from the table above
        color = color_table[team]
        # collect the ppg and name of each player on the team
        # you'll want to repeat with other stats as well
        ppg = []
        names = []
        for player in players:
            names.append(player["name"])
            ppg.append(player["ppg"])
        # record all the names, for use later in x label
        all_names.extend(names)

        # the position of bars is shifted by the number of players so far
        x = range(count_so_far, count_so_far + len(players))
        count_so_far += len(players)
        # make bars for this team's players ppg,
        # with the team name as the label
        bars = plt.bar(x, ppg, color=color, label=team)
        # add the value as text on the bars
        plt.bar_label(bars)

    # use the names, rotated 90 degrees as the labels for the bars
    plt.xticks(range(len(all_names)), all_names, rotation=90)
    # add the legend with the colors  for each team
    plt.legend(loc=0)
    # turn off gridlines
    plt.grid(False)
    # set the title
    plt.title("points per game")
    # save the figure to a file
    plt.savefig("ppg.png")


def main():
    """
    Create plots
    """

    teams = []

    team_names, team_urls = fp.extract_teams()

    team_players = []
    for team in team_urls:
        team_players.append(fp.extract_players(team))

    for i in range(len(team_names)):
        players = team_players[i]
        player_scores = []
        for player_url in players[1]:
            scores = fp.extract_player_statistics(player_url)
            if scores=='':
                player_scores.append(0.0)
            else:
                player_scores.append(scores[0])

        # Get best scores
        best_scores = sorted(zip(players[0], player_scores), reverse=True)[:3]

        teams.append(best_scores)
    
    #plot_NBA_player_statistics(team_names, best_scores)


if __name__ == '__main__':
    main()
