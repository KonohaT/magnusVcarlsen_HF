import chess
import matplotlib.pyplot as pyplot
import pandas as pd
from typing import Dict
from logger import Logger

class GameDatabase:
    def __init__(self):
        self.db = []
        pass
    
    def add_game(self, game: Dict[str, str]):
        self.db.append(game)

    def display_game(self, game_num: int): #Displays analytics for a specific game
        pass
    def display_tournament(self): #Displays analytics for the entire tournament

        df = pd.DataFrame(self.db)
        print(df)

        #heatmap of tournament winrates
        
        #bar chart of tournament winrates 

        pass

if __name__ == "__main__":
    test_logger = Logger("ChessGPT", "ChatGPT")
    test_logger.add_cheat("ChessGPT")
    test_logger.add_legal_move("e4")
    test_logger.add_checkmate("ChessGPT")
    #test_logger.add_legal_move("e4 e5")
    formatted = test_logger.return_formatted_game()

    test_logger_2 = Logger("ChessGPT", "BERT")
    test_logger_2.add_checkmate("BERT")
    formatted_2 = test_logger_2.return_formatted_game()

    db = GameDatabase()
    db.add_game(formatted)
    db.add_game(formatted_2)

    db.display_tournament()
