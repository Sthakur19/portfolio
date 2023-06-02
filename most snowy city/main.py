
from collections import Counter
import itertools
file = open("test_tasks.txt","r")
frequent_word = ""
frequency = 0 
words = []
 
# Traversing file line by line
for line in file:
     
    line_word = line.lower().replace(',','').replace('.','').split(" "); 
     
    # Adding them to list words
    for w in line_word[1:len(line_word):2]: 
        words.append(w); 
        new_list = list(zip(words[::2], words[1::2]))
    x= "snowy\n"
    Output = [tuple for tuple in new_list if any(x == i for i in tuple)]
 
counter=Counter(Output) 
# Counter is displying which city has maximum showny days
most_common = counter.most_common(1)[0][0][0]
print(most_common)

file.close()