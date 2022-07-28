from bs4 import BeautifulSoup
import re
from requesting_urls import get_html
from filter_urls import find_urls


def extract_teams():
    """Extract team names and urls from the NBA Playoff 'Bracket' section table.

    Returns:
        team_names (list): A list of team names that made it to the conference
            semifinals.
        team_urls (list): A list of absolute Wikipedia urls corresponding to team_names.

    """

    # get html using for example get_html from requesting_urls
    url = 'https://en.wikipedia.org/wiki/2021_NBA_playoffs'
    html = get_html(url)

    # create soup
    soup = BeautifulSoup(html, "html.parser")

    # find bracket we are interested in
    bracket_header = soup.find(id="Bracket")
    bracket_table = bracket_header.find_next("table")

    eastern_teams = bracket_table('td', {'style': 'border:1px solid #006;background-color:#87cefa;padding-left:0.3em;'})
    western_teams = bracket_table('td', {'style': 'border:1px solid #600;background-color:#ffaeb9;padding-left:0.3em'})

    teams = eastern_teams + western_teams
    links = [team.a for team in teams]

    # Initialize variables
    all_teams = []
    team_names = []
    team_urls = []

    # Extract values and find semifinalist
    for l in links:
        team_name =  l.get_text()
        team_url = l['href']

        if team_name in all_teams:
            if team_name in team_names:
                continue
            else:
                team_names.append(team_name)
                team_urls.append('https://en.wikipedia.org' + team_url)
        else:
            all_teams.append(team_name)

    return team_names, team_urls
   


def extract_players(team_url):
    """Extract players that played for a specific team in the NBA playoffs.

    Args:
        team_url (str): URL to the Wikipedia article of the season of a given
            team.

    Returns:
        player_names (list): A list of players names corresponding to the team whos URL was passed.
            semifinals.
        player_urls (list): A list of Wikipedia URLs corresponding to
            player_names of the team whos URL was passed.

    """

    # get html for each page using the team url you extracted before
    html = get_html(team_url)

    # make soup
    soup = BeautifulSoup(html, "html.parser")

    # find table we're interested in
    roster_header = soup.find(id="Roster")
    roster_table = roster_header.find_next("table")
    rows = roster_table.find_all("tr")

    # Initialize variables
    player_names = []
    player_urls = []

    # Extract player data
    for i in range(0, len(rows)):
        cells = rows[i].find_all("td")
        cells_text = [cell.get_text(strip=True) for cell in cells]

        if len(cells_text) == 7:
            rel_url = cells[2].find_next("a").attrs["href"]
            name = rel_url.split("_(")[0]
            name = name.replace('/wiki/', '').replace('_', ' ')

            player_names.append(name)
            player_urls.append('https://en.wikipedia.org' + rel_url)

    return player_names, player_urls


def extract_player_statistics(player_url):
    """Extract player statistics for NBA player.

    # Note: Make yourself familiar with the 2020-2021 player statistics wikipedia page and adapt the code accordingly.

    Args:
        player_url (str): URL to the Wikipedia article of a player.

    Returns:
        ppg (float): Points per Game.
        bpg (float): Blocks per Game.
        rpg (float): Rebounds per Game.

    """
    # As some players have incomplete statistics/information, you can set a default score, if you want.

    ppg = 0.0
    bpg = 0.0
    rpg = 0.0

    # get html
    html = get_html(player_url)

    # make soup
    soup = BeautifulSoup(html, "html.parser")

    # find header of NBA career statistics
    nba_header = soup.find(id="NBA_career_statistics")

    # check for alternative name of header
    if nba_header is None:
        nba_header = soup.find(id="NBA")

    try:
        # find regular season header
        # You might want to check for different spellings, e.g. capitalization
        # You also want to take into account the different orders of header and table
        regular_season_header = nba_header.find_next(id="Regular_season")

        # next we should identify the table
        nba_table = regular_season_header.find_next("table")

    except:
        try:
            # table might be right after NBA career statistics header
            nba_table = nba_header.find_next("table")

        except:
            return ppg, bpg, rpg

    # find nba table header and extract career row
    table_header = nba_table.find_all("th")
    rows = nba_table.find_all("tr")
    career_score_row = rows[-1].find_all("td")

    # find the columns for the different categories
    ppg = career_score_row[11].get_text().replace('\n', '')
    bpg = career_score_row[10].get_text()
    rpg = career_score_row[7].get_text()

    # Extract the scores from the different categories
    scores = [ppg, bpg, rpg]

    # Convert the scores extracted to floats
    # Note: In some cases the scores are not defined but only shown as '-'. In such cases you can just set the score to zero or not defined.
    for i in range(len(scores)):
        try:
            scores[i] = float(scores[i])
        except ValueError:
            scores[i] = 0.0

    return scores


def main():
    """
    Example usage.
    """

    players = []
    team_names, team_urls = extract_teams()
    for team_url in team_urls:
        players.append(extract_players(team_url))

    player_url='https://en.wikipedia.org/wiki/Seth_Curry#NBA'
    stats = extract_player_statistics(player_url)


if __name__ == '__main__':
    main()
