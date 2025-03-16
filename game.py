#game.py
import time
def createNewPokemon():
    # DUMMY FUNCTION -> Will never exit
    while True:
        pass
def attackPokemon(list):
    # DUMMY FUNCTION -> Will never exit
    while True:
        pass
def welcome():
    print("Welcome to the game")
def main():
    game = True
    pokemonStorage = []
    welcome()
    while game:
        choice = input("What to you want to do?\n1: Create new pokemon\n2: Attack a pokemon\nQ:")
        if choice == "1":
            print("Create Pokemon")
            newPokemon = createNewPokemon()
            pokemonStorage.append(newPokemon)
        elif choice == "2":
            print("Attack Pokemon")
            attackPokemon(pokemonStorage)
        elif choice in ("q", "Q"):
            print("Bye")
            game = False
        else:
            print("Invalid option")
    time.sleep(1)
if __name__ == "__main__":
    main()