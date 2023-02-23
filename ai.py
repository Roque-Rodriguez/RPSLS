from player import Player
import random


class AI(Player):
    def __init__(self):
        super().__init__()



#Randomly choose a gesture and store in self.selected_gesture
    def choose_gesture_method(self):
        self.selected_gesture = random.choice(self.gesture_list)
        print(f"AI choose {selected_gesture}")
