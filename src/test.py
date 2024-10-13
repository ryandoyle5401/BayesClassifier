from collections import Counter
import pandas as pd
import re


#String to store all reviews
lines = ""

# Open and read the file, specify encoding because I get an error otherwise
with open('reviews.txt', 'r', encoding='utf-8') as f:
    # Read the lines, convert to lowercase, store in lines variable
    lines = f.read().lower() # Note: append .lower() to have all words in lines be lowercase
    #print(type(lines))
    print(lines)

#Create a dict for storing all unique words. Note: maybe create two Counters; one for incrementing when a word appears in a postivie review, another for when a word appears in a negative review
wordCount = Counter(lines.split())
print(wordCount)
# Populating words dict with unique words and their frequencies
# for x in lines:
#     words[x] += 1
#
# print(words.most_common(10))