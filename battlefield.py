from human import Human
from ai import AI

class Battlefield:
    def __init__(self):
        self.player_one = ""
        self.player_two = ""

    def run_game(self):
        self.display_welcome()
        self.choose_game_type()
        self.game_on()
        pass

    def display_welcome(self):
        print("The game is easy beat the other player best out of of 3, Here are the rules:")
        print("Rock crushes Scissors")
        print("Scissors cuts Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitates Lizard")
        print("Lizard eats Paper")
        print("Paper disproves Spock")
        print("Spock vaporizes Rock")
        print("Easy enough right!!!! Let the games begin!")
              
    def choose_game_type(self):
        game_type = input("Please type (one) for Single Player or (two) for Multiplayer: ")

        if game_type == "one":
            self.player_one = Human()
            self.player_two = AI()
        if game_type == "two":
            self.player_one = Human()
            self.player_two = Human()
        # Assign either a Human class to self.player_two or AI() class to self.player two depending on user game type 
        pass

    def game_on(self):
        # A while loop
        # Call self.player.choose_gesture_method()
        # Comparison Logic if self.player_one.selected_gesture == "value" and self.player_two.selected_gesture == "value" add to self.player.wins +=1
        pass