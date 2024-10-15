from collections import Counter
import pandas as pd
import re
import string

# To Do
# - get rid of punctuation
# get rid of contractions
# make list of words to keep, get rid of all else
# separate all reviews so Positives are all together and Negatives are all together
# figure out how to read only the first 50 lines of the txt file, then the next 50
# keep track of word counts from positive reviews and negative reviews
# calculate prior probability
# calculate conditional probability e.g. word 'good' appears 12 times in positive reviews out of 50 occurrences. Probability is 12/50
# create a dataframe with a word and its label e.g. word: 'good' label: 'positive'

#String to store all reviews
lines = ""

# Open and read the file, specify encoding because I get an error otherwise
with open('reviews.txt', 'r', encoding='utf-8') as f:
    # Read the lines, convert to lowercase, store in lines variable
    lines = f.read().lower() # Note: append .lower() to have all words in lines be lowercase
    #print(type(lines))
    print(lines)

# This pattern splits string on one or more spaces and the colon
pattern = '[\s+:]'
# Split using re
lines = re.split(pattern, lines)
#Create a dict for storing all unique words. Note: maybe create two Counters; one for incrementing when a word appears in a postivie review, another for when a word appears in a negative review
wordCount = Counter(lines)

# Create a list of words to be removed from Counter
ignore = ["the", "a", "i", "if", "and", "it", "to", "this", "of", "for", "is", "with", "my", "that", "are", "was",
          "they", "these", "but", "in", "it\'s", "book", "so", "have", "only", "you", "on", "after", "will", "had",
          "as", "from", "do", "got", "just", "any", "were", "read", "all", "be", "both", "buy", "make"]
print(wordCount)
print()
# Loop to remove unnecessary words from wordCount Counter
for x in ignore:
    if x in wordCount:
        del wordCount[x]
print(wordCount)
# Populating words dict with unique words and their frequencies
# for x in lines:
#     words[x] += 1
#
# print(words.most_common(10))