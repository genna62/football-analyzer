import os
import pandas as pd

from plots import plot_statistics, plot_win_probabilities

def load_team_data(team_name, directory='head_to_head_data'):
    """Load the team's match data from the CSV file."""
    file_path = os.path.join(directory, f"{team_name}.csv")
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        print(f"Data for team {team_name} not found.")
        return pd.DataFrame()

def head_to_head_probability(home_team, away_team, team_data_home, team_data_away):
    """Calculate head-to-head win percentages for full-time."""
    
    # Filter matches where home_team is the home team and away_team is the away team
    home_matches = team_data_home[(team_data_home['HomeTeam'] == home_team) & 
                                   (team_data_home['AwayTeam'] == away_team)]
    print(home_matches)
    # Filter matches where away_team is the home team and home_team is the away team
    away_matches = team_data_away[(team_data_away['HomeTeam'] == away_team) & 
                                   (team_data_away['AwayTeam'] == home_team)]
    print(away_matches)
    # Combine both sets of matches
    total_matches = len(home_matches) + len(away_matches)
    print(total_matches)
    
    if total_matches == 0:
        return (0, 0, 0)  # No matches
    
    # Calculate wins and draws
    home_wins = len(home_matches[home_matches['FullTimeResult'] == 'H'])  # Home wins when home_team is home
    away_wins = len(away_matches[away_matches['FullTimeResult'] == 'H'])  # Away wins when away_team is away
    draws = (len(home_matches[home_matches['FullTimeResult'] == 'D']) + 
             len(away_matches[away_matches['FullTimeResult'] == 'D']))

    # Calculate probabilities
    print(home_wins)
    home_win_percentage = home_wins / total_matches
    away_win_percentage = away_wins / total_matches
    draw_percentage = draws / total_matches

    return home_win_percentage, draw_percentage, away_win_percentage

def calculate_home_win_draw_loss_percentage(team_name, season, team_data):
    """Calculate home win and draw percentage for a specific team in a specific season."""
    season_data = team_data[team_data['Season'] == season]
    
    home_games = season_data[season_data['HomeTeam'] == team_name]
    total_home_games = len(home_games)
    
    total_home_wins = len(home_games[home_games['FullTimeResult'] == 'H'])
    total_home_draws = len(home_games[home_games['FullTimeResult'] == 'D'])
    total_home_losses = len(home_games[home_games['FullTimeResult'] == 'A'])

    home_win_percentage = total_home_wins / total_home_games if total_home_games > 0 else 0
    home_draw_percentage = total_home_draws / total_home_games if total_home_games > 0 else 0
    home_losses_percentage = total_home_losses / total_home_games if total_home_games > 0 else 0
  
    return home_win_percentage, home_draw_percentage, home_losses_percentage

def calculate_away_win_draw_loss_percentage(team_name, season, all_team_data):
    """Calculate away win and draw percentage for a specific team in a specific season."""
    season_data = all_team_data[all_team_data['Season'] == season]
    
    away_games = season_data[season_data['AwayTeam'] == team_name]
    print(away_games)
    total_away_games = len(away_games)
    
    total_away_wins = len(away_games[away_games['FullTimeResult'] == 'A'])
    total_away_draws = len(away_games[away_games['FullTimeResult'] == 'D'])
    total_away_losses = len(away_games[away_games['FullTimeResult'] == 'H'])

    away_win_percentage = total_away_wins / total_away_games if total_away_games > 0 else 0
    away_draw_percentage = total_away_draws / total_away_games if total_away_games > 0 else 0
    away_losses_percentage = total_away_losses / total_away_games if total_away_games > 0 else 0

    return away_win_percentage, away_draw_percentage, away_losses_percentage



def predict_outcome(home_team, away_team):
    """Predict the outcome of a match between home_team and away_team."""
    home_data = load_team_data(home_team)
    away_data = load_team_data(away_team)

    home_win, draw, away_win = head_to_head_probability(home_team, away_team, home_data, away_data)

    print(f"Head-to-Head Win Percentages for {home_team} vs {away_team}:")
    print(f"Home Win: {home_win:.2%}, Draw: {draw:.2%}, Away Win: {away_win:.2%}")

    # Plot the win probabilities
    plot_win_probabilities(home_team, away_team, home_win, draw, away_win)

# def calculate_corner_distribution(team_data):
#     """Calculate corner distributions for given team data."""
#     corners = team_data['TotalCorners']
#     mean_corners = corners.mean()
#     std_corners = corners.std()

#     # Generate a range of corner counts for the distribution
#     corner_range = np.arange(0, 16)  # Corners from 0 to 15
#     pdf = norm.pdf(corner_range, mean_corners, std_corners)  # Probability Density Function

#     return corner_range, pdf

# def plot_corner_distribution(corner_range, pdf, team_name):
#     """Plot the corner distribution for a team."""
#     plt.figure(figsize=(10, 6))
#     plt.plot(corner_range, pdf, marker='o')
#     plt.fill_between(corner_range, pdf, alpha=0.3)
#     plt.title(f"Corner Distribution for {team_name}")
#     plt.xlabel('Number of Corners')
#     plt.ylabel('Probability Density')
#     plt.xlim(0, 15)
#     plt.ylim(0, max(pdf) * 1.1)
#     plt.grid()
#     plt.show()

# def corner_probability_distribution(home_team, away_team):
#     """Calculate corner distribution for both teams."""
#     home_data = load_team_data(home_team)
#     away_data = load_team_data(away_team)

#     home_corners_range, home_pdf = calculate_corner_distribution(home_data)
#     away_corners_range, away_pdf = calculate_corner_distribution(away_data)

#     return home_corners_range, home_pdf, away_corners_range, away_pdf

# def display_corner_probabilities(home_team, away_team):
#     """Display corner probabilities for both teams."""
#     home_range, home_pdf, away_range, away_pdf = corner_probability_distribution(home_team, away_team)

#     # plot_corner_distribution(home_range, home_pdf, home_team)
#     # plot_corner_distribution(away_range, away_pdf, away_team)

def main():
    # Load all team data from the head_to_head_data directory
     # Load all team data from the head_to_head_data directory
    all_team_data = []
    team_names = [f[:-4] for f in os.listdir('head_to_head_data') if f.endswith('.csv')]  # Get team names from filenames

    for team_name in team_names:
        team_data = load_team_data(team_name)
        if not team_data.empty:
            all_team_data.append(team_data)

    # Concatenate all data into one DataFrame
    all_team_data = pd.concat(all_team_data, ignore_index=True)

    # Specify team and season range to analyze
    team_name = 'Brighton'

    seasons = [2021, 2122, 2223, 2324]

    # Initialize lists to hold statistics
    home_stats = {'win': [], 'draw': [], 'loss': []}
    away_stats = {'win': [], 'draw': [], 'loss': []}

    # Calculate statistics for each season
    for season in seasons:
        season = int(season)
        home_win_percentage, home_draw_percentage, home_loss_percentage = calculate_home_win_draw_loss_percentage(team_name, season, all_team_data)
        away_win_percentage, away_draw_percentage, away_loss_percentage = calculate_away_win_draw_loss_percentage(team_name, season, all_team_data)

        home_stats['win'].append(home_win_percentage)
        home_stats['draw'].append(home_draw_percentage)
        home_stats['loss'].append(home_loss_percentage)

        away_stats['win'].append(away_win_percentage)
        away_stats['draw'].append(away_draw_percentage)
        away_stats['loss'].append(away_loss_percentage)

    # Plot the statistics
    
    plot_statistics(seasons, home_stats, away_stats, team_name)
    

    # Example usage
    home_team = 'Man United'
    away_team = 'Chelsea'
    
    predict_outcome(home_team, away_team)
    # display_corner_probabilities(home_team, away_team)

if __name__ == "__main__":
    main()