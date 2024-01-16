import requests
import re

class logger:
    def __init__(self, model_1: str, model_2: str):
        self.model_1 = model_1
        self.model_2 = model_2

    current_moves = "" #UCI notation
    cheat_attempts = [0] #logs the number of cheat attempts for every move in order 
    winner = ""

    #Interface with the Model Interface
    def add_legal_move(self, current_moves: str): #current_moves should be all moves so far, in UCI notation
        self.current_moves = current_moves
        self.cheat_attempts.append(0)
        
    def add_cheat(self, cheater_name: str):
        self.cheat_attempts[-1] += 1

    def add_checkmate(self, winner_name: str):
        #logs the winner and stops recording
        pass

    #Internal Work
    def get_stockfish_results(self, prev_state: str, current_state: str, depth: int = 5) -> float: #Takes current and previous FEN states. Can be refactored to only need one UCI current state
        #returns the stockfish analysis of the last move as a positive float
        #Example URL: https://stockfish.online/api/stockfish.php?fen=r2q1rk1/ppp2ppp/3bbn2/3p4/8/1B1P4/PPP2PPP/RNB1QRK1 w - - 5 11&depth=5&mode=eval
        current_FEN = "?fen=" + current_state
        prev_FEN = "?fen=" + prev_state
        
        endpoint = "https://stockfish.online/api/stockfish.php"
        current_extra = current_FEN + "&depth=" + str(depth) + "&mode=eval"
        prev_extra = prev_FEN + "&depth=" + str(depth) + "&mode=eval"
        current_response = requests.get(endpoint + current_extra)
        prev_response = requests.get(endpoint + prev_extra)

        current_string = str(current_response.json())
        prev_string = str(prev_response.json())

        current_score = float(re.findall(r"-?\d*\.*\d+", current_string)[0]) #Positive means white is winning and vice versa
        prev_score = float(re.findall(r"-?\d*\.*\d+", prev_string)[0])
        
        
        return abs(current_score) - abs(prev_score) #Positive numbers mean the player that made the move is better off
    def format_game(self):
        pass

    #Interface with game_database
    def return_formatted_game(self):
        pass
        """
        if self.winner == "":
            raise RuntimeError("Game is not yet completed")
            pass

        else:
            game = {"UCI": self.current_moves, "Cheat Attempts": self.cheat_attempts}
            return game
        """
    
#Testing section
if __name__ == "__main__":
    new_logger = logger("ChessGPT", "ChatGPT")
    current_board = "r2q1rk1/1pp2ppp/3bbn2/p2p4/8/1B1P4/PPP2PPP/RNB1QRK1 w - - 5 11" #make sure to include the additional notation at the end
    prev_board = "r2q1rk1/ppp2ppp/3bbn2/3p4/8/1B1P4/PPP2PPP/RNB1QRK1 w - - 5 11"
    print(str(new_logger.get_stockfish_results(prev_board, current_board)))
    