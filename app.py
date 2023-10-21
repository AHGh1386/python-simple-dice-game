import random

def roll_dice():
    return random.randint(1, 6)

def play():
    player1_score = 0
    player2_score = 0

    while True:
        # Player 1's turn
        input("Player 1, press Enter to roll the dice...")
        tas = roll_dice()
        player1_score += dice_roll
        print("Player one rolled a", tas)
        print("Player one total score:", player1_score)

        if player1_score >= 100:
            print("Player one wins!")
            break
          
        input("Player 2, press Enter to roll the dice...")
        tas = roll_dice()
        player2_score += dice_roll
        print("Player two rolled a", tas)
        print("Player two total score:", player2_score)

        if player2_score >= 100:
            print("Player two wins!")
            break

if __name__ == "__main__":
    play()
