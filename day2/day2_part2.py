def pick_move(opponent, outcome):
    """
    lose
    draw
    win
    """
    if opponent == "rock":
        if outcome == "lose":
            return "scissors"
        elif outcome == "draw":
            return "rock"
        elif outcome == "win":
            return "paper"
    
    elif opponent == "paper":
        if outcome == "lose":
            return "rock"
        elif outcome == "draw":
            return "paper"
        elif outcome == "win":
            return "scissors"
    
    elif opponent == "scissors":
        if outcome == "lose":
            return "paper"
        elif outcome == "draw":
            return "scissors"
        elif outcome == "win":
            return "rock"


opponent_choice = {
    "A": "rock",
    "B": "paper",
    "C": "scissors"
}

outcomes = {
    "X": {
        "outcome": "lose",
        "points": 0
    },
    "Y": {
        "outcome": "draw",
        "points": 3
    },
    "Z": {
        "outcome": "win",
        "points": 6
    }
}

point_values = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}


with open("day2/input2.txt", "r") as f:
    lines = f.readlines()
    total_points = 0
    for line in lines:
        moves = line.split(" ")
        opponent_move_key = moves[0]
        outcome_key = moves[1].strip()

        opponent_move = opponent_choice[opponent_move_key]

        outcome = outcomes[outcome_key]["outcome"]
        outcome_points = outcomes[outcome_key]["points"]

        my_move = pick_move(opponent=opponent_move, outcome=outcome)

        total_points += point_values[my_move]
        total_points += outcome_points

        


print(total_points)

        


