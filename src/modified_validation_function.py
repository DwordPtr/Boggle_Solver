def check_substrings_for_words_revised(word_list,substrings):
   valid_words = []
   substrings.sort()
   sub_i = 0
   words_in_dict = len(word_list)
   word_i = 0
   while current_candidate > words_in_dict:
      if substrings[sub_i] == word_list[word_i]:
         valid_words.append(substrings[sub_i]
         sub_i++
         word_i++
      
      elif substrings[sub_i] > word_list[word_i]:
         sub_i++
         word_i++

      else:
         word_i++

   return valid_words
      
