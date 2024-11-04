import os
import pandas as pd

def create_directory(directory):
    """Create a directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def load_match_data(file_path):
    """Load match data from a CSV file."""
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

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

def append_to_csv(file_path, match_data):
    """Append match data to a CSV file."""
    match_df = pd.DataFrame([match_data])
    if os.path.exists(file_path):
        match_df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        match_df.to_csv(file_path, index=False)

def extract_head_to_head_data(years, base_directory, output_directory):
    """Extract head-to-head match data for each team from Premier League files."""
    create_directory(output_directory)

    for year in years:
        year_folder = os.path.join(base_directory, str(year), 'Premier League')
        
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

def main():
    # Define the base directory containing the yearly folders
    base_directory = 'data'  # Update this with your actual base directory
    output_directory = 'head_to_head_data'
    years = [2021, 2122, 2223, 2324, 2425]  # Specify the years to process

    # Extract head-to-head data
    extract_head_to_head_data(years, base_directory, output_directory)

if __name__ == "__main__":
    main()