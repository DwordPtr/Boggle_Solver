max_length = 16
substrings_per_max_length_string = 0
for i in range(3,max_length+1):
   substrings_per_max_length_string+=(max_length - i)

print(substrings_per_max_length_string)
