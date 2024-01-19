class ModelInterface:
    def __init__(self, model_name: str):
        pass
        self.current_moves = ""
    
    

    #Appends model's next move to the current UCI moves and returns them
    def get_next_move(self):
        pass

    #Inputs the current UCI moves with the opponent's move at the end
    def add_opp_move(self, moves: str): 
        pass

    #Checks if the last move is legal
    def is_legal(self, move: str):
        pass

