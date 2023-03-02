
class Player:

    def __init__(self, name):
        self.gesture_list = ["Rock", "Paper", "Scissor", "Lizard" , "Spock"] #Add list of gestures 'Rock', "Paper"..
        self.wins = 0
        self.selected_gesture = ""
        self.name = name