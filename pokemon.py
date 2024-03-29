import random
import time
import sys
# changes

health_stats = random.randint(40, 50)
other_stats = random.randint(6, 8)

class Player:
    def __init__(self,name, pokemon_list):
        self.name = name
        self.pokemon_list = pokemon_list
    
    def get_name(self):
        self.name = input("Enter the name you would like to go by: ")
    
    def slow_print(self, text):
        for char in text:
            print(char, end="", flush = True)
            time.sleep(.07)

class Type:
    def __init__(self, name, weaknesses, strengths):
        self.name = name
        self.weaknesses = weaknesses
        self.strengths = strengths

fire = Type("Fire", weaknesses="water", strengths="grass")
water = Type("Water", weaknesses="Grass", strengths="Fire")
grass = Type("Grass", weaknesses="Fire", strengths="water") 

def choose_pokemon():


    attempts = 0
    while attempts < 4:
        print("Choose your Pokemon:")
        print("1. Charmander")
        print("2. Squirtle")
        print("3. Bulbasaur")
        pok_choice = input('Enter the number of your choice (1-3): ')

        if pok_choice == "1":
            return Pokemon("Charmander", health=health_stats, attack=other_stats, defense=other_stats,
                           special_atk=other_stats, special_def=other_stats, speed=other_stats, type=fire, move1="Ember", move2="Scractch", move3="Growl")
        elif pok_choice == "2":
            return Pokemon("Squirtle", health=health_stats, attack=other_stats, defense=other_stats,
                           special_atk=other_stats, special_def=other_stats, speed=other_stats, type=water, move1 = "Bubble", move2="Scractch", move3="Growl")
        elif pok_choice == "3":
            return Pokemon("Bulbasaur", health=health_stats, attack=other_stats, defense=other_stats,
                           special_atk=other_stats, special_def=other_stats, speed=other_stats, type=grass ,move1 = "Vine Whip", move2="Scractch", move3="Growl")
        else:
            print("Invalid choice. Please choose between (1-3)")
            attempts += 1
            if attempts == 4:
                print("You failed to choose a Pokemon! You get a Magikarp...")
                return Pokemon("Magikarp", health=30, attack=other_stats, defense=other_stats,
                    special_atk=other_stats, special_def=other_stats, speed=other_stats, type=water , move1 = "Bubble", move2="Scractch", move3="Growl")

def choose_opponent(player_type):
    if player_type == fire:
        return Pokemon("Squirtle", health=health_stats, attack=other_stats, defense=other_stats,
                           special_atk=other_stats, special_def=other_stats, speed=other_stats, type=water  ,move1 = "Bubble", move2="Scractch", move3="Growl")
    elif player_type == water:
        return Pokemon("Bulbasaur", health=health_stats, attack=other_stats, defense=other_stats,
                           special_atk=other_stats, special_def=other_stats, speed=other_stats, type=grass  ,move1 = "Vine Whip", move2="Scractch", move3="Growl")
    elif player_type == grass:
        return Pokemon("Charmander", health=health_stats, attack=other_stats, defense=other_stats,
                           special_atk=other_stats, special_def=other_stats, speed=other_stats, type=fire, move1 = "Ember", move2="Scractch", move3="Growl")
    else:
        return Pokemon("Charmander", health=health_stats, attack=other_stats, defense=other_stats,
                           special_atk=other_stats, special_def=other_stats, speed=other_stats, type=fire  ,move1 = "Ember", move2="Scractch", move3="Growl")

class Pokemon:
    def __init__(self, name, health, attack, defense, special_atk, special_def, speed, type, move1, move2, move3):
        self.name = name 
        self.health = health
        self.attack = attack
        self.defense = defense
        self.special_atk = special_atk
        self.special_def = special_def
        self.speed = speed
        self.type = type
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3

    def first_turn(self, speed,opponent):
        if self.speed > opponent.speed:
            pass
def battle_interface(player, opponent):
    while True:
        print("\n What will you do")
        print("1. Fight")
        print("2. Bag")
        print("3. Pokemon")
        print("4. Run Away")

        cho = input('ENter your choice (1-4): ')

        if cho == "1":
            print("\nChoose a move:")
            print(f"1. {player.move1}")
            print(f"2. {player.move2}")
            print(f"3. {player.move3}")
            move_choice = input("Enter the number of your choice (1-3): ")
        elif cho ==  2:
            print(None)
        elif cho == "3":
            pass
        elif cho == "4":
            sys.exit
        else:
            print("Invalid Choice.")

def main():
    story_mode = input("Do you wish to skip the dialogue: [Yes/No]").lower()
    if story_mode == "yes":
        print("Hello Trainer! Choose a Pokemon to accompany you on your adventures.")
        chosen_pokemon = choose_pokemon()
        print(f"You chose {chosen_pokemon.name}!")

        opponent_pokemon = choose_opponent(chosen_pokemon.type)
        #print(f"Your opponent chooses {opponent_pokemon.name}!")
        print("Great choice! Here a Gift")
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(1)
        if i == 2:
            print("\n", end="")
            
        print('You have received a Pokedex')
        time.sleep(2)

        print("let the battle begin")
        print(f"The opponent sends {opponent_pokemon.name} ")

        print(battle_interface(chosen_pokemon, opponent_pokemon))

    else:
        player = Player("",[])
        print("Before you stands Professor Birch, excitment unconcealed in his eyes ")
        print("\n")#-----------------------------
        player.slow_print('''"Greetings, young Trainer! Welcome to the world of Pokemon! I am Professor Birch, a Pokemon Researcher"''')
        print("\n")#-----------------------------

        player.slow_print("He geatures excitedly towards the surroundings")
        print("\n")#-----------------------------

        player.slow_print('''"As you can see, our world is filled with an various amount of pokemon, each with their own abliities."''')
        print("\n")#-----------------------------

        player.slow_print("He pauses as he reaches into his hag before pulling out a Pokedex")
        print("\n")#-----------------------------

        player.slow_print('''"Behold, the Pokédex! A wondrous tool to aid you on your path to Pokémon mastery. With it, you'll record data on every encounter"''')
        print("\n")#-----------------------------

        player.slow_print("'Now, before your journery, you must choose your first Pokemon companion',Professor Birch says with anticaption'I'm interrested in what you'll choose '")
        chosen_pokemon = choose_pokemon()
        print(f"You chose {chosen_pokemon.name}!")
        opponent_pokemon = choose_opponent(chosen_pokemon.type)
        print("\n")#-----------------------------
        player_name = input("Oh yes, what's your name: ")
        player.slow_print("With a warm smile Profesor Birch hands you the Pokedex")
        print("\n")#-----------------------------

        player.slow_print("Take this Pokedex, it time to start you Pokemon journey. Battle, explore, and make friends along the way as you rise to the top of the Pokemon world. YOUR DESINTY AWAITS!!!!")
        print("\n")#-----------------------------

        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(1)
        if i == 2:
            print("\n", end="")
            
        player.slow_print('You have received a Pokedex')
        print("\n")#-----------------------------
        player.slow_print("As you step out of Professor Birch Lab")
        print("\n")#-----------------------------
        # this part will be added later 
        names = ["Elizabeth","Alexis","Josh","Ryan"]
        rival = random.choice(names)
        player.slow_print(f"Trainer {rival} challenges you")
        print("\n")#-----------------------------
        print(f"The opponent sends {opponent_pokemon.name} ")

        print(battle_interface(chosen_pokemon, opponent_pokemon))





    

    

if __name__ == "__main__":
    main()
