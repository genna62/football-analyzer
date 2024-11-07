import os
import pandas as pd

from probabilities.head_to_head import head_to_head_probability
from probabilities.individual_team_win_loss_draw import win_draw_loss
from utils.load_data import load_team_data


# def predict_outcome(home_team, away_team):
#     """Predict the outcome of a match between home_team and away_team."""
#     home_data = load_team_data(home_team)
#     away_data = load_team_data(away_team)

#     home_win, draw, away_win = head_to_head_probability(home_team, away_team, home_data, away_data)

#     print(f"Head-to-Head Win Percentages for {home_team} vs {away_team}:")
#     print(f"Home Win: {home_win:.2%}, Draw: {draw:.2%}, Away Win: {away_win:.2%}")

#     # Plot the win probabilities
#     plot_win_probabilities(home_team, away_team, home_win, draw, away_win)

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
    
    # Plot the statistics
    team_to_search = 'Barcelona'
    seasons = [2021, 2122, 2223, 2324, 2425]
    home_team_head_to_head_directory = 'Serie A_head_to_head_data'
    away_team_head_to_head_directory = 'Liga I_head_to_head_data'
    # win_draw_loss(team_to_search, seasons, head_to_head_directory)


    home_team = "lazio"
    away_team = "porto"
    home_data = load_team_data(home_team, home_team_head_to_head_directory)
    away_data = load_team_data(away_team, away_team_head_to_head_directory)

    home_win, draw, away_win = head_to_head_probability(home_team, away_team, home_data, away_data)

    print(f"Head-to-Head Win Percentages for {home_team} vs {away_team}:")
    print(f"Home Win: {home_win:.2%}, Draw: {draw:.2%}, Away Win: {away_win:.2%}")
    # # Example usage
    # home_team = 'Man United'
    # away_team = 'Chelsea'
    
    # predict_outcome(home_team, away_team)
    # display_corner_probabilities(home_team, away_team)

if __name__ == "__main__":
    main()