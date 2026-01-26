def premier_league(team):
    match team:
        case "Arsenal" | "Chelsea" | "Manchester City" | "Liverpool" | "Manchester United":
            return f"{team} is in Premier League"
        case _:
            return f"{team} is not in Premier League"

        
print(premier_league("Liverpool"))