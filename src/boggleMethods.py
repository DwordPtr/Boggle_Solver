import math
import random
import networkx as nx
"""Check 2d board for validitiy """
def is_valid_2d_board(board_cand):
    for col in board_cand:
        if len(col) != len(board_cand):
            return False
    return True
"""Convert the board from a 2d list to a 1d list """
def unravel_board(original_board):
   new_board = [] 
   for i in range(len(original_board)):
      for j in range(len(original_board[i])):
         new_board.append(original_board[i][j])
   return new_board
   
#This approach may look convoluted but its easier to do the math this way then crawl the list
#Its possible to scale to n dimmensions but given the combonatorical nature of the problem
#it'll become intractible fast

"""take a 1d list and treat it as a row major 2d array to build an adjacencyList""" 
def build_adjacency_list(board):
   board_length = len(board)
   side_length = math.sqrt(board_length)
   lines = []
   #build a list of lists with index numbers as the first elements of each member list
   for i in range(len(board)):
      line = ""
      line +=str(i)
      line+=" "
      above = False
      below = False
      right = False
      left = False
      #after appending the vertex number check for adjacent nodes
      if (i-side_length) >=0 : # above
         above = True
         line+=str(int(i-side_length))
         line +=" "
      if(i+side_length) < board_length: #below
         below = True
         line+=str(int(i+side_length))
         line+=" "
      if(i+1) % side_length != 0 : #right
         right = True
         line+=str(int(i+1))
         line+=" "
      if i % side_length !=0: #left
         left = True
         line+=str(int(i-1))
         line+= " "
      #now for the corners
      if left and above:
         line+=str(int((i-side_length) - 1))
         line+=" "
      if right and above:
         line+=str(int((i-side_length) + 1))
         line+=" "
      if left and below :
         line+=str(int((i + side_length) - 1))
         line+=" "
      if right and below:
         line+=str(int((i + side_length) + 1))
         line+=" "
      
      lines.append(line)
   
   return lines
"""Parse the graph for all paths of length n"""
def find_valid_paths(Graph,board,length): # path of len(n) has a string of len(n+1)
   results = []
   for paths in (nx.all_simple_paths(Graph,source_node,target_node,length) for target_node in Graph.nodes_iter() for source_node in Graph.nodes_iter()):
      results+=paths
   
   return results

"""take the paths and convert them to strings"""
def parse_result_paths(path_list,board):
   strings = []
   for path in range(len(path_list)):
      chars = []
      for node_num in range(len(path_list[path])):
         chars.append(board[int(path_list[path][node_num])])
         string = ''.join(chars)
      
      strings.append(string)

   return strings

"""run through the list and remove any duplicate strings """            
def remove_duplicate_strings(substrings):
   seen = set()
   result = []
   for item in substrings:
      if item not in seen:
         seen.add(item)
         result.append(item)
   
   return result

"""Remove words less than three in length """
def truncate_word_list(word_list,n):
   truncated_word_list = []
   for word in word_list:
      if len(word) >=3: #boggle only allows word_len >=3
         truncated_word_list.append(word)
   
   return truncated_word_list

"""Take user input into 2d boggle board """
def enter_boggle_board(side_length=4):
   board = []
   for y in range(side_length):
      row = []
      for x in range(side_length):
        board_index = input("enter index row: "+str(x)+" col: "+str(y)+": ")
        row.append(board_index)
      
      board.append(row)
   
   return board

"""searches substrings from valid words agains the list """
def check_substrings_for_words(word_list,substrings):
   valid_words = []
   substrings.sort()
   sub_i = 0
   words_in_dict = len(word_list)
   substrings_in_list = len(substrings)
   word_i = 0
   while sub_i < substrings_in_list and word_i < words_in_dict:
      if substrings[sub_i] == word_list[word_i]:
         valid_words.append(substrings[sub_i])
         sub_i+=1
         word_i+=1
      
      elif substrings[sub_i] > word_list[word_i]:
         word_i+=1

      elif substrings[sub_i] < word_list[word_i]:
         sub_i+=1

   return valid_words

""" Generate a random board as a 2d list"""  
def random_board_2d(length=4):
    board = []
    for y in range(length):
         row = []
         a_num = ord('a')
         z_num = ord('z')
         for i in range(length):
             row.append(chr(random.randrange(a_num,z_num+1)))
         board.append(row)
    return board

"""display a 2d board """
def display_2d_board(board):
    for x in range(len(board)):
        for y in range(len(board[x])):
            print(board[x][y], end= '   ')
        print()
              

    
