import os 
import pandas as pd
from utils.load_data import load_team_data
from plots import plot_statistics

def calculate_home_win_draw_loss_percentage(team_name, season, team_data):
    """Calculate home win and draw percentage for a specific team in a specific season."""
    season_data = team_data[team_data['Season'] == season]
    
    home_games = season_data[season_data['HomeTeam'] == team_name]
    # print(home_games)
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
    # print(away_games)
    total_away_games = len(away_games)
    
    total_away_wins = len(away_games[away_games['FullTimeResult'] == 'A'])
    total_away_draws = len(away_games[away_games['FullTimeResult'] == 'D'])
    total_away_losses = len(away_games[away_games['FullTimeResult'] == 'H'])

    away_win_percentage = total_away_wins / total_away_games if total_away_games > 0 else 0
    away_draw_percentage = total_away_draws / total_away_games if total_away_games > 0 else 0
    away_losses_percentage = total_away_losses / total_away_games if total_away_games > 0 else 0

    return away_win_percentage, away_draw_percentage, away_losses_percentage

def win_draw_loss(team_to_search, seasons, head_to_head_directory): 
    # Load all team data from the head_to_head_data directory
    # Load all team data from the head_to_head_data directory
    all_team_data = []
    team_names = [f[:-4] for f in os.listdir(head_to_head_directory) if f.endswith('.csv')]  # Get team names from filenames
    print(team_names)
    for team_name in team_names:
        team_data = load_team_data(team_name, head_to_head_directory)
        if not team_data.empty:
            all_team_data.append(team_data)

    # Concatenate all data into one DataFrame
    all_team_data = pd.concat(all_team_data, ignore_index=True)

    # Initialize lists to hold statistics
    home_stats = {'win': [], 'draw': [], 'loss': []}
    away_stats = {'win': [], 'draw': [], 'loss': []}

    # Calculate statistics for each season
    for season in seasons:
        season = int(season)
        home_win_percentage, home_draw_percentage, home_loss_percentage = calculate_home_win_draw_loss_percentage(team_to_search, season, all_team_data)
        away_win_percentage, away_draw_percentage, away_loss_percentage = calculate_away_win_draw_loss_percentage(team_to_search, season, all_team_data)

        home_stats['win'].append(home_win_percentage)
        home_stats['draw'].append(home_draw_percentage)
        home_stats['loss'].append(home_loss_percentage)

        away_stats['win'].append(away_win_percentage)
        away_stats['draw'].append(away_draw_percentage)
        away_stats['loss'].append(away_loss_percentage)

    plot_statistics(seasons, home_stats, away_stats, team_to_search)
    