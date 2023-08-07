# Sample data (replace this with actual data from a database or API)
ipl_teams = ['Chennai Super Kings', 'Mumbai Indians', 'Royal Challengers Bangalore', 'Kolkata Knight Riders', 'Delhi Capitals', 'Punjab Kings', 'Rajasthan Royals', 'Sunrisers Hyderabad']
team_players = {
    'Chennai Super Kings': ['MS Dhoni', 'Suresh Raina', 'Ravindra Jadeja', 'Ambati Rayudu'],
    'Mumbai Indians': ['Rohit Sharma', 'Jasprit Bumrah', 'Hardik Pandya', 'Kieron Pollard'],
    'Royal Challengers Bangalore': ['Virat Kohli', 'AB de Villiers', 'Yuzvendra Chahal', 'Glenn Maxwell'],
    # Add more teams and players here
}
tournament_history = {
    '2021': 'Chennai Super Kings',
    '2020': 'Mumbai Indians',
    '2019': 'Mumbai Indians',
    # Add more tournament history here
}

def display_teams():
    print("IPL Teams:")
    for idx, team in enumerate(ipl_teams, start=1):
        print(f"{idx}. {team}")

def display_players(team_name):
    if team_name in team_players:
        print(f"Players of {team_name}:")
        for idx, player in enumerate(team_players[team_name], start=1):
            print(f"{idx}. {player}")
    else:
        print(f"Team '{team_name}' not found in IPL.")

def display_tournament_history():
    print("IPL Tournament History:")
    for year, winner in tournament_history.items():
        print(f"{year}: {winner}")

if __name__ == "__main__":
    print("Welcome to IPL Information App!")
    while True:
        print("\nOptions:")
        print("1. Display IPL Teams")
        print("2. Display Players of a Team")
        print("3. Display IPL Tournament History")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            display_teams()
        elif choice == '2':
            team_name = input("Enter team name: ")
            display_players(team_name)
        elif choice == '3':
            display_tournament_history()
        elif choice == '4':
            print("Thank you for using the IPL Information App!")
            break
        else:
            print("Invalid choice. Please try again.")
