import random

def roll_dice():
    return random.randint(1, 6)

def move_player(position, roll):
    new_position = position + roll
    if new_position in snakes:
        print(f"Oops! Snake at {new_position}, sliding down to {snakes[new_position]}")
        return snakes[new_position]
    elif new_position in ladders:
        print(f"Great! Ladder at {new_position}, climbing up to {ladders[new_position]}")
        return ladders[new_position]
    return new_position

snakes = {
    16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78
}

ladders = {
    2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 78: 98
}

def play_game():
    player_positions = [0, 0]
    player_names = ["Player 1", "Player 2"]
    turn = 0
    
    while True:
        input(f"{player_names[turn]}'s turn. Press Enter to roll the dice...")
        roll = roll_dice()
        print(f"{player_names[turn]} rolled a {roll}")
        
        new_position = move_player(player_positions[turn], roll)
        
        if new_position > 100:
            print("Roll exceeds 100, try again next turn!")
        else:
            player_positions[turn] = new_position
        
        print(f"{player_names[turn]} is now at position {player_positions[turn]}\n")
        
        if player_positions[turn] == 100:
            print(f"{player_names[turn]} wins the game!")
            break
        
        turn = 1 - turn  

if __name__ == "__main__":
    play_game()
