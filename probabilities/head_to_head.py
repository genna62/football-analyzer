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
