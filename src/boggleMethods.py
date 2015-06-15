import math
import networkx as nx
"""take a 2d list and return a 1d list with index s 0 - n-1 """
def unravel_board(original_board):
   new_board = [] 
   for i in range(len(original_board)):
      for j in range(len(original_board[i])):
         new_board.append(original_board[i][j])
   return new_board

"""take a 1d list and treat it as a row major 2d array to build an adjacencyList """
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
"""return a list of valid substrings of length n """
def find_valid_paths(Graph,board,length):
   results = []
   for paths in (nx.all_simple_paths(Graph,source_node,target_node,length) for target_node in Graph.nodes_iter() for source_node in Graph.nodes_iter()):
      results+=paths
   
   return results

def parse_result_paths(path_list,board):
   strings = []
   for path in range(len(path_list)):
      chars = []
      for node_num in range(len(path_list[path])):
         chars.append(board[int(path_list[path][node_num])])
         string = ''.join(chars)
      
      strings.append(string)

   return strings
            
def remove_duplicate_strings(substrings):
   seen = set()
   result = []
   for item in substrings:
      if item not in seen:
         seen.add(item)
         result.append(item)
   
   return result

def truncate_word_list(word_list,n):
   truncated_word_list = []
   for word in word_list:
      if len(word) <= n and len(word) >=3: #boggle only allows word_len >=3
         truncated_word_list.append(word)
   
   return truncated_word_list
def check_substrings_for_words(word_list,substrings):
   valid_words = []
   for word_candidate in substrings:
      for word in word_list:
         if word_candidate == word:
            valid_words.append(word_candidate)

   return valid_words

def enter_boggle_board():
   board = []
   for y in range(4):
      row = []
      for x in range(4):
        board_index = input("enter index row: "+str(x)+" col: "+str(y)+": ")
        row.append(board_index)
      
      board.append(row)
   
   return board

#make this main search
def check_substrings_for_words_revised(word_list,substrings):
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


def check_substrings_for_words_bin(word_list,substrings):
   valid_words = []
   for substring in substrings:
      imax = len(word_list) - 1
      imin = 0
      while imax >= imin:
         imid = int((imax+imin)/2)
         if substring == word_list[imid]:
            valid_words.append(substring)
            break

         elif substring < word_list[imid]:
            imax = imid - 1

         else: 
            imin = imid + 1

   return valid_words
   
def check_substrings_for_words_bin_2(word_list,substrings):
   valid_words = []
   for word in word_list:
      imax = len(substrings) - 1
      imin = 0
      while imax >= imin:
         imid = int((imax+imin)/2)
         if word == substrings[imid]:
            valid_words.append(word)
            break

         elif word < substrings[imid]:
            imax = imid - 1

         else:
            imin = imid+1

   return valid_words

