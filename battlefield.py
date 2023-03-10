from human import Human
from ai import AI

class Battlefield:
    def __init__(self):
        self.player_one = Human(input("Please enter your Name: "))
        self.player_two = None

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
        user_validation = False
        while user_validation == False:
            game_type = input("Please type (one) for Single Player or (two) for Multiplayer: ")

            if game_type == "one":
                self.player_two = AI("Jake")
                user_validation = True
            elif game_type == "two":
                self.player_two = Human(input("Please enter your Name: "))
                user_validation = True
            else:
                print("Wrong input")
        
    def game_on(self):
        while self.player_one.wins <= 2 or self.player_two.wins <= 2:
            self.player_one.choose_gesture_method()
            self.player_two.choose_gesture_method()
            print(f"{self.player_one.name} chose {self.player_one.selected_gesture}")
            print(f"{self.player_two.name} chose {self.player_two.selected_gesture}")

            if self.player_one.selected_gesture == self.player_two.selected_gesture:
                print("This is a tie.  This will not count.  Please choose again.")
            if self.player_one.selected_gesture == "Rock" and self.player_two.selected_gesture == "Scissor":
                print(f"{self.player_one.selected_gesture} beat {self.player_two.selected_gesture}")
                print(f"{self.player_one.name} beat {self.player_two.name}!")
                self.player_one.wins += 1
            if self.player_one.selected_gesture == "Scissor" and self.player_two.selected_gesture == "Paper":
                print(f"{self.player_one.selected_gesture} beat {self.player_two.selected_gesture}")
                print(f"{self.player_one.name} beat {self.player_two.name}!")
                self.player_one.wins += 1
            if self.player_one.selected_gesture == "Paper" and self.player_two.selected_gesture == "Rock":
                print(f"{self.player_one.selected_gesture} beat {self.player_two.selected_gesture}")
                print(f"{self.player_one.name} beat {self.player_two.name}!")
                self.player_one.wins += 1
            if self.player_one.selected_gesture == "Rock" and self.player_two.selected_gesture == "Lizard":
                print(f"{self.player_one.selected_gesture} beat {self.player_two.selected_gesture}")
                print(f"{self.player_one.name} beat {self.player_two.name}!")
                self.player_one.wins += 1
            if self.player_one.selected_gesture == "Lizard" and self.player_two.selected_gesture == "Spock":
                print(f"{self.player_one.selected_gesture} beat {self.player_two.selected_gesture}")
                print(f"{self.player_one.name} beat {self.player_two.name}!")
                self.player_one.wins += 1
            if self.player_one.selected_gesture == "Spock" and self.player_two.selected_gesture == "Scissor":
                print(f"{self.player_one.selected_gesture} beat {self.player_two.selected_gesture}")
                print(f"{self.player_one.name} beat {self.player_two.name}!")
                self.player_one.wins += 1
            if self.player_one.selected_gesture == "Scissor" and self.player_two.selected_gesture == "Lizard":
                print(f"{self.player_one.selected_gesture} beat {self.player_two.selected_gesture}")
                print(f"{self.player_one.name} beat {self.player_two.name}!")
                self.player_one.wins += 1 
            if self.player_one.selected_gesture == "Lizard" and self.player_two.selected_gesture == "Paper":
                print(f"{self.player_one.selected_gesture} beat {self.player_two.selected_gesture}")
                print(f"{self.player_one.name} beat {self.player_two.name}!")
                self.player_one.wins += 1
            if self.player_one.selected_gesture == "Paper" and self.player_two.selected_gesture == "Spock":
                print(f"{self.player_one.selected_gesture} beat {self.player_two.selected_gesture}")
                print(f"{self.player_one.name} beat {self.player_two.name}!")
                self.player_one.wins += 1
            if self.player_one.selected_gesture == "Spock" and self.player_two.selected_gesture == "Rock":
                print(f"{self.player_one.selected_gesture} beat {self.player_two.selected_gesture}")
                print(f"{self.player_one.name} beat {self.player_two.name}!")
                self.player_one.wins += 1
            if self.player_two.selected_gesture == "Rock" and self.player_one.selected_gesture == "Scissor":
                print(f"{self.player_two.selected_gesture} beat {self.player_one.selected_gesture}")
                print(f"{self.player_two.name} beat {self.player_one.name}!")
                self.player_two.wins += 1
            if self.player_two.selected_gesture == "Scissor" and self.player_one.selected_gesture == "Paper":
                print(f"{self.player_two.selected_gesture} beat {self.player_one.selected_gesture}")
                print(f"{self.player_two.name} beat {self.player_one.name}!")
                self.player_two.wins += 1
            if self.player_two.selected_gesture == "Paper" and self.player_one.selected_gesture == "Rock":
                print(f"{self.player_two.selected_gesture} beat {self.player_one.selected_gesture}")
                print(f"{self.player_two.name} beat {self.player_one.name}!")
                self.player_two.wins += 1
            if self.player_two.selected_gesture == "Rock" and self.player_one.selected_gesture == "Lizard":
                print(f"{self.player_two.selected_gesture} beat {self.player_one.selected_gesture}")
                print(f"{self.player_two.name} beat {self.player_one.name}!")
                self.player_two.wins += 1
            if self.player_two.selected_gesture == "Lizard" and self.player_one.selected_gesture == "Spock":
                print(f"{self.player_two.selected_gesture} beat {self.player_one.selected_gesture}")
                print(f"{self.player_two.name} beat {self.player_one.name}!")
                self.player_two.wins += 1
            if self.player_two.selected_gesture == "Spock" and self.player_one.selected_gesture == "Scissor":
                print(f"{self.player_two.selected_gesture} beat {self.player_one.selected_gesture}")
                print(f"{self.player_two.name} beat {self.player_one.name}!")
                self.player_two.wins += 1
            if self.player_two.selected_gesture == "Scissor" and self.player_one.selected_gesture == "Lizard":
                print(f"{self.player_two.selected_gesture} beat {self.player_one.selected_gesture}")
                print(f"{self.player_two.name} beat {self.player_one.name}!")
                self.player_two.wins += 1 
            if self.player_two.selected_gesture == "Lizard" and self.player_one.selected_gesture == "Paper":
                print(f"{self.player_two.selected_gesture} beat {self.pplayer_one.selected_gesture}")
                print(f"{self.player_two.name} beat {self.player_one.name}!")
                self.player_two.wins += 1
            if self.player_two.selected_gesture == "Paper" and self.player_one.selected_gesture == "Spock":
                print(f"{self.player_two.selected_gesture} beat {self.player_one.selected_gesture}")
                print(f"{self.player_two.name} beat {self.player_one.name}!")
                self.player_two.wins += 1
            if self.player_two.selected_gesture == "Spock" and self.player_one.selected_gesture == "Rock":
                print(f"{self.player_two.selected_gesture} beat {self.player_one.selected_gesture}")
                print(f"{self.player_two.name} beat {self.player_one.name}!")
                self.player_two.wins += 1

            if self.player_one.wins == 3:
                print(f"Congrats {self.player_one.name} you have WON this match!!!")  
                break 
            if self.player_two.wins == 3:
                print (f"Congrats {self.player_two.name} you have WON this match!!!")
                break