import os
import pandas as pd

def append_to_csv(file_path, match_data):
    """Append match data to a CSV file."""
    match_df = pd.DataFrame([match_data])
    if os.path.exists(file_path):
        match_df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        match_df.to_csv(file_path, index=False)