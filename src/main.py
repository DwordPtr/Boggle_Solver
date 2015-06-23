import sampleBoard
from boggleMethods import *
import networkx as nx
from datetime import datetime

def make_word_list(word_file_string):
   word_file = open(word_file_string)
   word_list = word_file.read()
   word_list = word_list.split('\n')
   
   return word_list

def main():
    maximum_word_length = input("Enter max word length: ")
    while type(maximum_word_length) != int and (int(maximum_word_length)<1 or int(maximum_word_length)>16 ):
        maximum_word_length = input("please input a real integer value: ")
    
    maximum_word_length = int(maximum_word_length)
    board = random_board_2d()
    display_2d_board(board)
    board = unravel_board(board) #change this soon
    #words have an n+1 length for an n length path
    word_list = make_word_list('word_lists/words')
    
    #make the graph
    adj = build_adjacency_list(board)
    G = nx.parse_adjlist(adj)
    substrings = find_valid_paths(G,board,maximum_word_length)
    valid_words = check_substrings_for_words(word_list,substrings)
    print(len(valid_words))
    for word in valid_words:
       print(word)


main()
