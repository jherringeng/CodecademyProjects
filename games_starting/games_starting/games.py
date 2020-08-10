import random

# Starting money. Passed to play games and other functions
money = 100

#Write your game of chance functions here
def play_heads_or_tails(money):
    print("\nYou are now playing heads or tails.")
    print("Guess whether the coin flip is heads or tails.")
    player_bet = get_player_bet(money)
    player_call = None
    print("Enter heads or tails:")
    while True:
        player_call = get_player_call()
        if not player_call:
            continue
        player_call = player_call.lower()
        if player_call not in ["heads", "tails"]:
            print("Please enter (heads) or (tails).")
        else:
            break
    coin_flip = get_coin_flip()
    print("The coin flip came up {}.".format(coin_flip))
    if (player_call == coin_flip):
        print("You won!!!")
        money += player_bet
    else:
        print("You lost!!!")
        money -= player_bet

    return money

def play_cho_han(money):
    print("\nYou are now playing Cho-Han.")
    print("Guess whether adding 2 dice is odd or even.")
    player_bet = get_player_bet(money)
    player_call = None
    print("Enter odd or even:")
    while True:
        player_call = get_player_call()
        if not player_call:
            continue
        player_call = player_call.lower()
        if player_call not in ["odd", "even"]:
            print("Please enter (odd) or (even).")
        else:
            break
    dice_1, dice_2, dice_roll, result = get_cho_han_roll()
    print("You roll a {} and a {} making {}.".format(dice_1, dice_2, dice_roll))
    if (player_call == result):
        print("You won!!!")
        money += player_bet
    else:
        print("You lost!!!")
        money -= player_bet

    return money

def play_highest_card(money):
    print("\nYou are now playing Highest Card.")
    print("Whoever picks the highest card wins. Aces are valued at 11. Jack, Queen and King are valued at 10.")
    player_bet = get_player_bet(money)
    cards = {"Ace": 11, "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
        "Jack": 10, "Queen": 10, "King":10}
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    your_card = random.choice(list(cards.keys()))
    your_suit = random.choice(suits)
    print("You pick the {} of {}.".format(your_card, your_suit))
    while True:
        house_card = random.choice(list(cards.keys()))
        house_suit = random.choice(suits)
        if your_card != house_card or your_suit != house_suit:
            break
    print("House picks the {} of {}.".format(house_card, house_suit))

    if cards[your_card] > cards[house_card]:
        print("You won!!!")
        money += player_bet
    elif cards[your_card] < cards[house_card]:
        print("You lost!!!")
        money -= player_bet
    else:
        print("You drew. Bet has been returned.")

    return money

def play_roulette(money):
    print("\nYou are now playing roulette.")
    print("Bet on where the ball will land. Bet on single numbers or groups of numbers such as odd and even.")
    player_bet = get_player_bet(money)
    player_call = None
    while True:
        # Try to convert player call to an int to bet on single numbers
        try:
            player_call = get_player_call()
            if not player_call:
                continue
            player_call_int = int(player_call)
            if player_call_int > 36 or player_call_int < 1:
                print("Enter a number between 1 and 36")
            else:
                print("You bet on number {}.".format(player_call_int))
                break
        # Exception used for text input of player calls
        except ValueError:
            player_call = player_call.lower()
            if player_call not in ["odd", "even", "high", "low"]:
                print("Please enter a valid bet.")
            else:
                print("You bet on {}.".format(player_call))
                break

    # Number -1 used as 00 placement
    roulette_wheel = range(-1, 37)
    roulette_result = random.choice(roulette_wheel)
    # Text formatted to replace -1 with 00
    if roulette_result == -1:
        roulette_result = "00"
        print("The roulette wheel spun {}.".format(roulette_result))
    else:
        print("The roulette wheel spun {}.".format(str(roulette_result)))

    # Identify results and give winnings or losses
    if roulette_result <= 0:
        print("You lost!!!")
        money -= player_bet
    elif (player_call == roulette_result):
        print("You won!!!")
        money += 35 * player_bet
    elif player_call in ["odd", "even", "high", "low"]:
        if player_call == "even" and roulette_result % 2 == 0:
            print("You won!!!")
            money += player_bet
        elif player_call == "odd" and roulette_result % 2 == 1:
            print("You won!!!")
            money += player_bet
        elif player_call == "low" and roulette_result <= 18:
            print("You won!!!")
            money += player_bet
        elif player_call == "high" and roulette_result > 18:
            print("You won!!!")
            money += player_bet
        else:
            print("You lost!!!")
            money -= player_bet

    else:
        print("You lost!!!")
        money -= player_bet

    return money

def get_cho_han_roll():
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_roll = dice_1 + dice_2
    if dice_roll % 2 == 0:
        result = "even"
    else:
        result = "odd"
    return dice_1, dice_2, dice_roll, result

def get_coin_flip():
    coin_flip = None
    coin_flip_bool = random.randint(0, 1)
    if  coin_flip_bool == 0:
        coin_flip = "heads"
    else:
        coin_flip = "tails"
    return coin_flip

# Gets what the player is betting on. Repeats until input given
def get_player_call():
    player_call = None
    while True:
        player_call = input("What do you call? ")
        if not player_call:
            print("You need to input what you are betting on!")
        else:
            break

    return player_call

# Gets the players bet. Repeats until valid bet given
def get_player_bet(money):
    print("You have ${}".format(money))
    while True:
        try:
            player_bet = int(input("Enter your bet: "))
            if player_bet > money:
                print("You don't have enough money")
                print("You have ${}".format(money))
            elif player_bet < 0:
                print("You can't bet negative amounts!")
            elif player_bet == 0:
                print("You must make a bet to play!")
            else:
                print("Your bet is: ${}".format(player_bet))
                break
        except ValueError:
            print("Oops! That was not a valid bet. Try again...")

    return player_bet

# Gets the players choice of game. Repeats until valid input given. Does not check if valid game
def get_game_choice():
    while True:
        try:
            print("\nEnter number to choose a game.")
            print("1: Coin Toss, 2: Cho Han, 3: Highest Card, 4: Roulette")
            game_choice = int(input("Which game do you want to play: "))
            break
        except ValueError:
            print("Oops! That was not a valid input. Try again...")

    return game_choice

# Function for the player to choose and play games.
def play_games(money):
    print("Welcome to the Codecademy Casino!\n")

    while True:
        if money <= 0:
            print("You are out of money! Please gamble responsibly.")
            break
        else:
            print("You have ${}".format(money))
            game_choice = get_game_choice()
            # May replace the following with function calls from a list
            if game_choice == 1:
                print("You chose Coin Toss.\n")
                money = play_heads_or_tails(money)
            elif game_choice == 2:
                print("You chose Cho Han.\n")
                money = play_cho_han(money)
            elif game_choice == 3:
                print("You chose Highest Card.\n")
                money = play_highest_card(money)
            elif game_choice == 4:
                print("You chose Roulette.\n")
                money = play_roulette(money)
            else:
                print("Oops! You did not choose a valid game.")

# Calls the casino to play games. Main function
play_games(money)
