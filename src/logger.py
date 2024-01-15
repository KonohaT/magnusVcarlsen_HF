import requests

class logger:
    def __init__(self, model_1: str, model_2: str):
        self.model_1 = model_1
        self.model_2 = model_2

    current_moves = "" #FEN notation
    cheat_attempts = "" #format?
    winner = ""

    #Internal Work
    def get_stockfish_results(self, prev_state: str, current_state: str, depth: int = 5) -> float:
        #returns the stockfish analysis of the last move
        #Example URL: https://stockfish.online/api/stockfish.php?fen=r2q1rk1/ppp2ppp/3bbn2/3p4/8/1B1P4/PPP2PPP/RNB1QRK1 w - - 5 11&depth=5&mode=eval
        current_FEN = "?fen=" + current_state
        prev_FEN = "?fen=" + prev_state
        
        endpoint = "https://stockfish.online/api/stockfish.php"
        current_extra = current_FEN + "&depth=" + str(depth) + "&mode=eval"
        prev_extra = prev_FEN + "&depth=" + str(depth) + "&mode=eval"
        current_response = requests.get(endpoint + current_extra)
        prev_response = requests.get(endpoint + prev_extra)

        #response format is: {'success': True, 'data': 'Total evaluation: -1.79 (white side)'}
        
        #return current_score - prev_score
    def format_game(self):
        pass

    #Interface with the Model Interface
    def add_legal_move(self, current_moves: str): #current_moves should be all moves so far, in FEN notation
        #updates sequence of moves stored
        pass
    def add_cheat(self, cheater_name: str):
        #adds cheats parallel to the sequence of moves
        pass
    def add_checkmate(self, winner_name: str):
        #logs the winner and stops recording
        pass

    #Interface with game_database
    def return_formatted_game(self, game_num: int):
        pass

    