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
    maximum_word_length = 10 #input("Enter max word length: ")
    #maximum_word_length = int(maximum_word_length)
    board = sampleBoard.board
    board = unravel_board(board)
    word_list = truncate_word_list(make_word_list('words'),maximum_word_length)

    #print("board unraveled")
    adj = build_adjacency_list(board)
    #print("Adjacecny List made")
    G = nx.parse_adjlist(adj)
    #print("Graph made")
    substring_paths = find_valid_paths(G,board,maximum_word_length)
    substrings = remove_duplicate_strings(parse_result_paths(substring_paths,board))
    valid_words = check_substrings_for_words_revised(word_list,substrings)
    print(len(valid_words))
    for word in valid_words:
       print(word)


main()
