from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)



#Needs to assign a value of Rock, Paper, ect.. to self.selected_gesture
    def choose_gesture_method(self):
        user_input = int(input(f"Please select one between this list: Press 0 for {self.gesture_list[0]}, Press 1 for {self.gesture_list[1]}, Press 2 for {self.gesture_list[2]}, Press 3 for {self.gesture_list[3]}, Press 4 for {self.gesture_list[4]}: "))
        self.selected_gesture = self.gesture_list[user_input]
        
##if statements based on user input using string index number to locate the place in the list.  possible while loop around if statments

        
