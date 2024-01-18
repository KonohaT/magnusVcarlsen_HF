import chess
import random
import streamlit as st

def cleanup_output(text, prompt, extra_len):
        section = text[len(prompt):]
        st.write("Proposed Move: " + section)
        valid_letters = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h']
        valid_pieces = ['p','P','k','K','q','Q','r','R','b','B', 'n', 'N']
        valid_numbers = ['1','2','3','4','5','6','7','8']

        #if there are any syntatically moves in this string for pieces
        countr = 0
        while countr < len(section) - 3:
          if(section[countr] in valid_pieces and section[countr + 1] in valid_letters and section[countr + 2] in valid_numbers):
            #print(section[countr:countr+3])
            return ' ' + section[countr:countr+3]
          countr+=1
        
        #variant for capturing!
        countr = 0
        while countr < len(section) - 4:
          if(section[countr] in valid_pieces and section[countr + 1] == 'x' and section[countr + 2] in valid_letters and section[countr + 3] in valid_numbers):
            #print(section[countr:countr+3])
            return ' ' + section[countr:countr+5]
          countr+=1

        #same as moves but for pawns
        countr = 0
        while countr < len(section) - 2:
          if(section[countr] in valid_letters and section[countr+1] in valid_numbers):
            #print(section[countr:countr+2])
            return ' ' + section[countr:countr+2]
          countr+=1

        #variant for capturing!
        countr = 0
        while countr < len(section) -4:
          if(section[countr] in valid_letters and section[countr+1] == 'x' and section[countr+2] in valid_letters and section[countr + 3] in valid_numbers):
            #print(section[countr:countr+2])
            return ' ' + section[countr:countr+4]
          countr+=1
        
        return ' e8'

class AInstance:
    def __init__(self, type, generator):
        self.type = type
        self.game_end = False
        self.generator = generator        

    #All this does it take the gamestate and add the ai-generated result to it
    def move(self, game_state):
        if(self.type == "gpt2-medium-chess"):
            prompt = "1-0 2700 1350 " + game_state
            extra_len = 7
        else:
            prompt = game_state
            extra_len = 5
        countr = 0
        while True:
            generated_text = self.generator(prompt, max_length=len(prompt) + extra_len, num_return_sequences=1)[0]['generated_text']
            selected_move = cleanup_output(generated_text, prompt, extra_len)
            
            #if this move is valid then return it
            proposed_board = game_state + selected_move
            if(verify_move(proposed_board)):
                return proposed_board
            countr+=1
            #goes fifty times until the AInstance object flags itself as "ended" (fundamentally unable to make a valid move)
            if(countr > 50):
                self.game_end = True
                break

    def check_if_end(self):
        return self.game_end

def verify_move(string):
    board = chess.Board()
    st.write("Board: " + string + "\n")
    for move in string.split():
      #if this move makes no sense it will return false and the game will try again to generate a good move
      try:
        board.push_san(move)
      except:
        return False
    if(board.is_valid):
      return True
    return False

def check_mate(string):
  #simulates mate idk
    if(random.randrange(0,100) == 4):
        st.write("H")
        return True
    return False

def print_game(string):
    st.write("Some kind of visualization for the chess board based on this string: " + string)

def make_move(instance, game_state):
    st.write(instance.type + "'s move")
    return_state = game_state
    return_state = instance.move(game_state)
    game_ongoing = True
    if(instance.check_if_end()):
        st.write("This player claims they can't make a valid move after 50 tries: " + instance.type)
        game_ongoing = False
    if(check_mate(return_state)):
        st.write("This player claims mates: " +  instance.type)
        game_ongoing = False
    return(return_state, game_ongoing)


def main():
    if(random.randint(0,1) == 1):
        white = AInstance("gpt2", generator)
        black = AInstance("gpt2-medium-chess", generator2)
        st.write("Gpt2 is White and Gpt2 Optimized is Black\n")
    else:
        white = AInstance("gpt2-medium-chess", generator2)
        black = AInstance("gpt2", generator)
        st.write("Gpt2 is Black and Gpt2 Optimized is White\n")

    game_state = "e4 e5"
    game_ongoing = True
    while game_ongoing:
        game_state, game_ongoing = make_move(white, game_state)
        if not game_ongoing:
            print_game(game_state)
            break
        game_state, game_ongoing = make_move(black, game_state)
        if not game_ongoing:
            print_game(game_state)
            break
main()