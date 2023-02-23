from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()



#Needs to assign a value of Rock, Paper, ect.. to self.selected_gesture
    def choose_gesture_method(self):
        self.selected_gesture = input(f"Please select one between this list:{self.gesture_list}: ")
        pass
