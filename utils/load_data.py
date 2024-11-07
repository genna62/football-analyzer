import os
import pandas as pd

def load_team_data(team_name, directory):
    """Load the team's match data from the CSV file."""
    file_path = os.path.join(directory, f"{team_name}.csv")
    print(file_path)
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        print(f"Data for team {team_name} not found.")
        return pd.DataFrame()


def load_match_data(file_path):
    """Load match data from a CSV file."""
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error