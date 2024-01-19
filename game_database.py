import chess
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from typing import Dict
from logger import Logger
import time
import numpy as np

class GameDatabase:
    def __init__(self):
        self.db = []
        pass
    
    def add_game(self, game: Dict[str, str]):
        self.db.append(game)

    def display_game(self, game_num: int): #Displays analytics for a specific game
        game = self.db[game_num]

        fig, axs = plt.subplots(2,2)
        width = 0.4

        def list_sets_graph(data_list: [], axs_pos: [], title, width = 0.4):
            white_data = data_list[::2]
            black_data = data_list[1::2]
            x = np.arange(len(white_data))

            axs[axs_pos[0], axs_pos[1]].set_xticks(x, [x for x in range(len(white_data))])
            axs[axs_pos[0], axs_pos[1]].bar(x - (width/2), white_data, width, color = "navajowhite")
            axs[axs_pos[0], axs_pos[1]].bar(x + (width/2), black_data, width, color = "saddlebrown")
            axs[axs_pos[0], axs_pos[1]].legend(["White", "Black"]) 



        #plot time per move, with data for each model
        time_title = "Seconds Per Move"
        list_sets_graph(game[time_title], axs_pos=[0,0], title=time_title)

        #plot cheating per model
        cheat_title = "Cheat Attempts Per Move"
        list_sets_graph(game["Cheat Attempts"], axs_pos=[1,0], title = cheat_title)

        #stockfish analysis of each player over time


        #plt.show()
        st.pyplot(fig)
        pass


    def display_tournament(self): #Displays analytics for the entire tournament

        df = pd.DataFrame(self.db)

        #heatmap of tournament winrates
        
        #bar chart of tournament winrates
        win_results = df["Winner"].value_counts()
        print(win_results.rank())

        names = ["steve", "bob", "emily"]
        nums = [1,2,3]

        fig, axs = plt.subplots(2,1)
        axs[0].plot(win_results)
        axs[1].bar(names, nums)

        st.pyplot(fig)
        
        

if __name__ == "__main__":
    test_logger = Logger("ChessGPT", "ChatGPT")
    test_logger.add_cheat("ChessGPT")
    time.sleep(1)
    test_logger.add_legal_move("e4")
    time.sleep(1)
    test_logger.add_legal_move("e4 e6")
    time.sleep(2)
    test_logger.add_legal_move("e4 e6 Nf3")
    test_logger.add_checkmate("ChessGPT")
    #test_logger.add_legal_move("e4 e5")
    formatted = test_logger.return_formatted_game()

    test_logger_2 = Logger("ChessGPT", "BERT")
    test_logger_2.add_checkmate("BERT")
    formatted_2 = test_logger_2.return_formatted_game()

    test_logger_3 = Logger("ChessGPT", "BERT")
    test_logger_3.add_checkmate("ChessGPT")
    formatted_3 = test_logger_3.return_formatted_game()

    db = GameDatabase()
    db.add_game(formatted)
    db.add_game(formatted_2)
    db.add_game(formatted_3)

    db.display_game(0)
