def play_round(player,opponent):
    """
    Calculate the points based on win lose or draw
    win = 6 points
    draw = 3 points
    lose = 0 points
    """

    if player == "rock":
        if opponent == "scissors":
            return 6
        elif opponent == "rock":
            return 3
        else:
            return 0
    
    elif player == "paper":
        if opponent == "rock":
            return 6
        elif opponent == "paper":
            return 3
        else:
            return 0
    
    elif player == "scissors":
        if opponent == "paper":
            return 6
        elif opponent == "scissors":
            return 3
        else:
            return 0


opponent_choice = {
    "A": "rock",
    "B": "paper",
    "C": "scissors"
}

my_choice = {
    "X": {
        "points": 1,
        "move": "rock"
    },
    "Y": {
        "points": 2,
        "move": "paper",
    },
    "Z": {
        "points": 3,
        "move": "scissors"
    }
}


with open("day2/input2.txt", "r") as f:
    lines = f.readlines()
    total_points = 0
    for line in lines:
        moves = line.split(" ")
        opponent_move = moves[0]
        my_move = moves[1].strip()

        # Add points for chosen move
        total_points += my_choice[my_move]["points"]

        total_points += play_round(player=my_choice[my_move]["move"], opponent=opponent_choice[opponent_move])


print(total_points)

        


