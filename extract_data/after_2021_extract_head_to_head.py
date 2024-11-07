import sys
import os

# Get the parent directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the utils directory to the system path
utils_path = os.path.join(parent_dir, 'utils')
sys.path.append(utils_path)

# Now you can import load_data
from load_data import load_match_data  # Replace some_function with the actual function you want to use
from create import create_directory
from append import append_to_csv
# from ..utils.append import append_to_csv
# from ..utils.create import create_directory
# from ..utils.load_data import load_match_data

def extract_match_info(row, year):
    """Extract relevant match information from a row."""
    return {
        'Season': year,
        'Date': row['Date'],
        'HomeTeam': row['HomeTeam'],
        'AwayTeam': row['AwayTeam'],
        'HalfTimeHomeScore': row['HTHG'],
        'HalfTimeAwayScore': row['HTAG'],
        'HalfTimeResult': row['HTR'],
        'FullTimeHomeScore': row['FTHG'],
        'FullTimeAwayScore': row['FTAG'],
        'FullTimeResult': row['FTR'],
        'HomeCorners': row['HC'],
        'AwayCorners': row['AC'],
        'TotalCorners': row['HC'] + row['AC']
    }


def extract_head_to_head_data(years, base_directory, output_directory, league_name):
    """Extract head-to-head match data for each team from Premier League files."""
    create_directory(output_directory)

    for year in years:
        year_folder = os.path.join(base_directory, str(year), league_name)
        
        if not os.path.exists(year_folder):
            print(f"Folder does not exist: {year_folder}")
            continue
        
        for filename in os.listdir(year_folder):
            if filename.endswith('.csv'):
                file_path = os.path.join(year_folder, filename)
                print(f"Processing file: {file_path}")

                df = load_match_data(file_path)

                for _, row in df.iterrows():
                    match_data = extract_match_info(row, year)
                    team_file_path = os.path.join(output_directory, f"{match_data['HomeTeam']}.csv")
                    append_to_csv(team_file_path, match_data)

def extract_league_head_to_head_data():
    # Define the base directory containing the yearly folders
    base_directory = 'data'  # Update this with your actual base directory
    league_name = 'Liga I' # Change the name of the league which has the teams
    output_directory = f'{league_name}_head_to_head_data'
    years = [2021, 2122, 2223, 2324, 2425]  # Specify the years to process

    # Extract head-to-head data
    extract_head_to_head_data(years, base_directory, output_directory, league_name)


extract_league_head_to_head_data()