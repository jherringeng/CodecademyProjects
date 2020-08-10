import random

money = 100

#Write your game of chance functions here
def play_heads_or_tails(money):
    print("\nYou are now playing heads or tails.")
    print("Guess whether the coin flip is heads or tails.")
    player_bet = get_player_bet()
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
        money = game_over(money)
    return money

def play_cho_han(money):
    print("\nYou are now playing Cho-Han.")
    print("Guess whether adding 2 dice is odd or even.")
    player_bet = get_player_bet()
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
        money = game_over(money)
    return money

def play_highest_card(money):
    print("\nYou are now playing Highest Card.")
    print("Whoever picks the highest card wins. Aces are valued at 11. Jack, Queen and King are valued at 10.")
    player_bet = get_player_bet()
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
        money = game_over(money)
    else:
        print("You drew. Bet has been returned.")
    return money

def play_roulette(money):
    print("\nYou are now playing roulette.")
    print("Bet on where the ball will land. Bet on single numbers or groups of numbers such as odd and even.")
    player_bet = get_player_bet()
    player_call = None
    while True:
        try:
            player_call = get_player_call()
            if not player_call:
                continue
            player_call_int = int(player_call)
            if player_call_int > 36 or player_call_int < 1:
                print("Enter a number between 1 and 36")
            else:
                print("You bet on: ${}".format(player_call_int))
                break
        except ValueError:
            player_call = player_call.lower()
            if player_call not in ["odd", "even", "high", "low"]:
                print("Please enter a valid bet.")
            else:
                break
    roulette_wheel = range(-1, 37)
    roulette_result = random.choice(roulette_wheel)
    if roulette_result == -1:
        roulette_result = "00"
        print("The roulette wheel spun {}.".format(roulette_result))
    else:
        print("The roulette wheel spun {}.".format(str(roulette_result)))
    if roulette_result <= 0:
        print("You lost!!!")
        money -= player_bet
        money = game_over(money)
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
        elif player_call == "high" and roulette_result >= 19:
            print("You won!!!")
            money += player_bet
        else:
            print("You lost!!!")
            money -= player_bet
            money = game_over(money)
    else:
        print("You lost!!!")
        money -= player_bet
        money = game_over(money)

    return money

def game_over(money):
    if money <= 0:
        print("You are out of money. Better luck next time!")
        print("Your money has been reset.")
        money = 100

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

def get_player_call():
    player_call = None
    while True:
        player_call = input("What do you call? ")
        if not player_call:
            print("You need to input what you are betting on!")
        else:
            break

    return player_call

def get_player_bet():
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
            print("Oops!  That was no valid bet. Try again...")

    return player_bet

#Call your game of chance functions here
money = play_roulette(money)
money = play_highest_card(money)
money = play_heads_or_tails(money)
money = play_cho_han(money)
