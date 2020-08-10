import copy

class Pokemon:

    # All pokemon types
    pokemon_types = ["Normal", "Fire", "Water", "Grass", "Flying", "Fighting", "Poison", "Electric", "Ground", "Rock", "Psychic", "Ice", "Bug", "Ghost", "Steel", "Dragon", "Dark", "Fairy"]

    # Constructor. Default values for name, level and type
    def __init__(self, name = "Unknown", level = 1, type = "Fire"):
        self.knocked_out = False
        self.name = name
        if level <= 0:
            print("Level is invalid. Setting to 1.")
            self.level = 1
        else:
            self.level = level
        if type in self.pokemon_types:
            self.type = type
        else:
            print("Type not recognised. Setting type as Fire.")
            self.type = "Fire"
        self.max_health = 10 * self.level
        self.health = self.max_health

    def lose_health(self, health_lost):
        self.health -= health_lost
        self.knocked_out = self.knock_out()
        if (self.knocked_out):
            print("{name} has been knocked out!".format(name = self.name))
        else:
            print("{name} now has {health} health".format(name = self.name, health = self.health))

    def knock_out(self):
        if self.health <= 0:
            self.health = 0
            return True
        else:
            return False

    def attack_pokemon(self, opp_pokemon):
        damage = self.level

        print("{self_name} attacks {opp_name}!".format(self_name = self.name, opp_name = opp_pokemon.name))

        # Identify type and modify damage on strength or weakness
        if self.type == "Fire":
            if opp_pokemon.type in ["Bug", "Steel", "Grass", "Ice"]: # Strong against
                damage *= 2
            elif opp_pokemon.type in ["Rock", "Fire", "Water", "Dragon"]: # Weak against
                damage /= 2
        if self.type == "Water":
            if opp_pokemon.type in ["Ground", "Rock", "Fire"]: # Strong against
                damage *= 2
            elif opp_pokemon.type in ["Water", "Grass", "Dragon"]: # Weak against
                damage /= 2
        if self.type == "Grass":
            if opp_pokemon.type in ["Ground", "Rock", "Water"]: # Strong against
                damage *= 2
            elif opp_pokemon.type in ["Flying", "Poison", "Bug", "Steel", "Fire", "Grass", "Dragon"]: # Weak against
                damage /= 2
        if self.type == "Electric":
            if opp_pokemon.type in ["Flying", "Water"]: # Strong against
                damage *= 2
            elif opp_pokemon.type in ["Ground", "Grass", "Electric", "Dragon"]: # Weak against
                damage /= 2
        # Damage pokemon
        opp_pokemon.lose_health(damage)



class Trainer:
    def __init__(self, name, pokemons, potions = 1):
        self.name = name
        self.potions = potions
        # Pokemons passed in as list
        self.pokemons = pokemons
        # Added this to class to simplify logic of determining which Pokemons are knocked knocked out
        # If a Pokemon is knocked out they are removed from available_pokemons
        self.available_pokemons = pokemons
        self.current_pokemon = pokemons[0]

    def attack_trainer(self, opp_trainer):
        self.current_pokemon.attack_pokemon(opp_trainer.current_pokemon)

    def use_potion(self):
        self.current_pokemon.health += 100
        if self.current_pokemon.health > self.current_pokemon.max_health:
            self.current_pokemon.health = self.current_pokemon.max_health
        print("You healed {name}. {name} now has {health} health!".format(name = self.current_pokemon.name, health = self.current_pokemon.health))
        self.potions -= 1
        print("You now have {potions} potions.".format(potions = self.potions))

    def switch_pokemon(self):
        print("Enter number to choose your pokemon!")
        i = 1
        # Uses available_pokemons list to simplify logic
        for pokemon in self.available_pokemons:
            print(str(i) + ". " + pokemon.name)
            i += 1
        while True:
            try:
                chosen_pokemon = int(input(">>"))
                if chosen_pokemon < 1 or chosen_pokemon > len(self.available_pokemons):
                    print("Please enter number for Pokemon between 1 and {}".format(len(self.available_pokemons)))
                else:
                    chosen_pokemon -= 1
                    self.current_pokemon = self.available_pokemons[chosen_pokemon]
                    print("You choose {}!".format(self.current_pokemon.name))
                    break
            except ValueError:
                print("Oops!  That was not recognised. Try again...")

    # New function to restore pokemons between fights
    def restore_pokemons(self):
        for pokemon in self.pokemons:
            pokemon.health = pokemon.max_health
            print("{} is healed and now has {} health.".format(pokemon.name, pokemon.health))
        # Overwrite available_pokemons with pokemons (probably more reliable than adding them again in loop)
        self.available_pokemons = copy.deepcopy(self.pokemons)

    def choose_option(self):
        if self.potions > 0 and len(self.available_pokemons) > 1:
            print("Enter 1 to use potion and 2 to change Pokemon. Press Enter to continue.")
            user_choice = input()
            if user_choice == "1":
                self.use_potion()
                print("You have {} potions available.".format(self.potions))
            elif user_choice == "2":
                self.switch_pokemon()
            return
        elif self.potions > 0:
            print("Enter 1 to use potion.")
            user_choice = input()
            if user_choice == "1":
                self.use_potion()
                print("You have {} potions available.".format(self.potions))
            return
        elif len(self.available_pokemons) > 1:
            print("Enter 1 to change Pokemon.")
            user_choice = input()
            if user_choice == "1":
                self.switch_pokemon()
            return

pikachu = Pokemon("Pikachu", 10, "Electric")
charmander = Pokemon("Charmander", 10, "Fire")
weepinbell = Pokemon("Weepinbell", 5, "Grass")
venusaur = Pokemon("Venusaur", 15, "Grass")
luxray = Pokemon("Luxray", 12, "Electric")
snorlax = Pokemon("Snorlax", 13, "Normal")

ash = Trainer("Ash", [pikachu, charmander, weepinbell], 2)
team_rocket = Trainer("Team Rocket", [charmander, pikachu, weepinbell, venusaur], 2)

def check_pokemon_knocked_out(opp_team):
    if opp_team.current_pokemon.knocked_out:
        print("{}'s pokemon is knocked out!".format(opp_team.name))
        opp_team.available_pokemons.remove(opp_team.current_pokemon)
        return True
    else:
        return False

def check_pokemon_available(attack_team, opp_team):
    if len(opp_team.available_pokemons) == 0:
        print("{} has no more Pokemon available!".format(opp_team.name))
        print(attack_team.name + " wins!!!")
        return False
    else:
        opp_team.switch_pokemon()
        return True


def battle(your_team, their_team):
    pass

print("Pick your starting Pokemon!")
ash.switch_pokemon()
i = 1
while True:
    print("\nRound " + str(i) + "\n")
    ash.choose_option()
    ash.attack_trainer(team_rocket)
    if check_pokemon_knocked_out(team_rocket):
        if not check_pokemon_available(ash, team_rocket):
            break

    team_rocket.attack_trainer(ash)
    if check_pokemon_knocked_out(ash):
        if not check_pokemon_available(team_rocket, ash):
            break

    i += 1
