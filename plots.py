import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def plot_statistics(seasons, home_stats, away_stats, team_name):
    """Plot line graphs for home and away statistics."""
    
    # Home statistics
    plt.figure(figsize=(12, 6))
    plt.plot(seasons, home_stats['win'], marker='o', label='Home Win Percentage')
    plt.plot(seasons, home_stats['draw'], marker='o', label='Home Draw Percentage')
    plt.plot(seasons, home_stats['loss'], marker='o', label='Home Loss Percentage')
    plt.title(f"{team_name} Home Statistics Over Seasons")
    plt.xlabel('Season')
    plt.ylabel('Percentage')
    plt.ylim(0, 1)
    plt.xticks(seasons)
    plt.legend()
    plt.grid()

    # Away statistics
    plt.figure(figsize=(12, 6))
    plt.plot(seasons, away_stats['win'], marker='o', label='Away Win Percentage')
    plt.plot(seasons, away_stats['draw'], marker='o', label='Away Draw Percentage')
    plt.plot(seasons, away_stats['loss'], marker='o', label='Away Loss Percentage')
    plt.title(f"{team_name} Away Statistics Over Seasons")
    plt.xlabel('Season')
    plt.ylabel('Percentage')
    plt.ylim(0, 1)
    plt.xticks(seasons)
    plt.legend()
    plt.grid()
    plt.show()

def plot_win_probabilities(home_team, away_team, home_win, draw, away_win):
    """Plot win probabilities for a match."""
    labels = [f"{home_team} Win", "Draw", f"{away_team} Win"]
    probabilities = [home_win, draw, away_win]

    plt.figure(figsize=(8, 5))
    plt.bar(labels, probabilities, color=['blue', 'orange', 'red'])
    plt.ylim(0, 1)
    plt.ylabel('Probability')
    plt.title(f"Win Probabilities: {home_team} vs {away_team}")
    plt.show()