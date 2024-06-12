#NEW EDIT


# Define current division structure
current_divisions = {
    "AFC East": ["Team1", "Team2", "Team3", "Team4"],
    "AFC North": ["Team5", "Team6", "Team7", "Team8"],
    "AFC South": ["Team9", "Team10", "Team11", "Team12"],
    "AFC West": ["Team13", "Team14", "Team15", "Team16"],
    "NFC East": ["Team17", "Team18", "Team19", "Team20"],
    "NFC North": ["Team21", "Team22", "Team23", "Team24"],
    "NFC South": ["Team25", "Team26", "Team27", "Team28"],
    "NFC West": ["Team29", "Team30", "Team31", "Team32"]
}

# Function to display current division structure
def display_divisions(divisions):
    for division, teams in divisions.items():
        print(f"{division}:")
        for team in teams:
            print(f"  - {team}")
        print()

# Function to propose new realignment
def realign_divisions(new_divisions):
    print("Proposed Division Realignment:")
    display_divisions(new_divisions)

# Display current divisions
print("Current Division Structure:")
display_divisions(current_divisions)

# Define proposed new division structure
new_divisions = {
    "AFC East": ["Team1", "Team5", "Team9", "Team13"],
    "AFC North": ["Team2", "Team6", "Team10", "Team14"],
    "AFC South": ["Team3", "Team7", "Team11", "Team15"],
    "AFC West": ["Team4", "Team8", "Team12", "Team16"],
    "NFC East": ["Team17", "Team21", "Team25", "Team29"],
    "NFC North": ["Team18", "Team22", "Team26", "Team30"],
    "NFC South": ["Team19", "Team23", "Team27", "Team31"],
    "NFC West": ["Team20", "Team24", "Team28", "Team32"]
}
# Propose new realignment
realign_divisions(new_divisions)
