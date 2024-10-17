from collections import Counter

import nltk
from nltk.corpus import stopwords
import pandas as pd
import re
import string
import math
#Ran this only once, don't need to download multiple times
#nltk.download('stopwords')

# Naive function to calculate probabilities
def predict(review, positive_word_count, negative_word_count, bag_of_words, positive_prior, negative_prior):
    total_positive_words = sum(positive_word_count.values())
    total_negative_words = sum(negative_word_count.values())
    words = review.split()

    # Initialize probabilities with priors
    prob_positive = positive_prior
    prob_negative = negative_prior

    # Calculate probabilities for the review
    for word in words:
        if word in bag_of_words:
            positive_word_probability = positive_word_count.get(word, 0) / total_positive_words
            negative_word_probability = negative_word_count.get(word, 0) / total_negative_words

            # Multiply probabilities (instead of adding log probabilities)
            prob_positive *= positive_word_probability
            prob_negative *= negative_word_probability

    # Return the prediction based on which probability is higher
    if prob_positive > prob_negative:
        return "positive"
    else:
        return "negative"

# To Do
# keep track of word counts from positive reviews and negative reviews
# calculate prior probability
# calculate conditional probability e.g. word 'good' appears 12 times in positive reviews out of 50 occurrences. Probability is 12/50
# create a dataframe with a word and its label e.g. word: 'good' label: 'positive'

#String to store all reviews
lines = ""

#Maybe delete this and just read the positive_words and negative_words files and combine into one list
bag_of_words = ["amazing","well","lighter","jokes","satisfied","perfect","great","beautifully","highly","recommended",
                "best","thrilled","brilliant","clarity","invaluable","nice","works","love","gift","creative","explore",
                "good","awesome","excited","wonderful","fun","cool","entertaining","favorite","phenomenal","excellent",
                "stylish","durable","pleased","sturdy","safe","sleek","convenient","comfortable","affordable","fantastic",
                "happy","smooth","reliable","interesting","heartfelt","quick","outstanding","captivating","terrific",
                "adorable","awful","bad","boring","cheap","cracks","crap","crashes","crooked","damaged","debris","deceptive",
                "defective","degrading","dent","dirty","disappointed","disappointing","disgusting","dishonest","dissipate",
                "distortion","dull","flaw","flimsy","freezes","frustration","hassle","horrible","malfunctioned","off",
                "overheating","poor","predictable","questionable","ripped","ruin","simplistic","smelt","static","terrible",
                "thin","tiny","trashcan","ugly","uncomfortable","unfortunately","unresponsive","unwearable","useless",
                "wasted","weak","wreck"]
positive_word_count = {}
negative_word_count = {}
# Open and read the file, specify encoding because I get an error otherwise
with open('reviews.txt', 'r', encoding='utf-8') as f:

    # Modifications to this function:
    # Have a list of positive and negative words available
    # Read line by line
    # Use an if statement to determine if the review is positive or not
    # If the review is positive check for which words from positive_list are in there
    # Place that word into a dict (if it isn't already in there) then increment the counter
    # This is so I can keep track of the number of times certain words appear in positive and negative reviews
    # Note: need to know how many times positive words appear in negative reviews and how many times negative words appear in positive reviews

    # Read the lines, convert to lowercase, store in lines variable
    #lines = f.readline().lower() # Note: append .lower() to have all words in lines be lowercase

    # Modification Needed: modify the for loop so it will read x number of lines
    train_split = 0.5

    # Lines is a list
    lines = f.readlines()
    print(type(lines))
    # Index represents the line number to stop reading reviews for training. The rest of the reviews will be read in for testing
    index = math.floor(len(lines) * train_split)
    print(index)
    # Modify list to remove punctuation, newline, make all characters lowercase. Also, only read i lines.
    for i in range(index):
        # Change list so that punctuation, newline is removed and characters are all lower
        lines[i] = lines[i].translate(str.maketrans('', '', string.punctuation)).strip().lower()
        #print(lines[i])
        if "positive" in lines[i]:
            words = lines[i].split()
            for word in words:
                if (word not in positive_word_count) and (word in bag_of_words):
                    positive_word_count[word] = 1
                elif (word in positive_word_count) and (word in bag_of_words):
                    positive_word_count[word] += 1
        elif "negative" in lines[i]:
            words = lines[i].split()
            for word in words:
                if (word not in negative_word_count) and (word in bag_of_words):
                    negative_word_count[word] = 1
                elif (word in negative_word_count) and (word in bag_of_words):
                    negative_word_count[word] += 1
        # for word in split_review:
        #     # Extract positive and negative words from positive and negative reviews
        #     if "positive" in lines[i]:
        #         if (lines[i] not in positive_word_count) and (lines[i] in bag_of_words):
        #             positive_word_count[word] = 1
        #         elif (lines[i] in positive_word_count) and (lines[i] in bag_of_words):
        #             positive_word_count[word] += 1
        #     elif "negative" in lines[i]:
        #         for word in lines[i]:
        #             if (word not in negative_word_count) and (word in bag_of_words):
        #                 negative_word_count[word] = 1
        #             elif (word in negative_word_count) and (word in bag_of_words):
        #                 negative_word_count[word] += 1
    #lines = lines.translate(str.maketrans('', '', string.punctuation)).strip()
    # for line in lines:
    #     #print(line)
    #     line = line.translate(str.maketrans('', '', string.punctuation)).strip().lower()
    #     line = line.split()
    #     #print(type(line))
    #     if "positive" in line:
    #         for word in line:
    #             if (word not in positive_word_count) and (word in bag_of_words):
    #                 positive_word_count[word] = 1
    #             elif (word in positive_word_count) and (word in bag_of_words):
    #                 positive_word_count[word] += 1
    #     elif "negative" in line:
    #         for word in line:
    #             if (word not in negative_word_count) and (word in bag_of_words):
    #                 negative_word_count[word] = 1
    #             elif (word in negative_word_count) and (word in bag_of_words):
    #                 negative_word_count[word] += 1


    # for line in f:
    #     #print(line)
    #     line = line.translate(str.maketrans('', '', string.punctuation)).strip().lower()
    #     line = line.split()
    #     #print(type(line))
    #     if "positive" in line:
    #         for word in line:
    #             if (word not in positive_word_count) and (word in bag_of_words):
    #                 positive_word_count[word] = 1
    #             elif (word in positive_word_count) and (word in bag_of_words):
    #                 positive_word_count[word] += 1
    #     elif "negative" in line:
    #         for word in line:
    #             if (word not in negative_word_count) and (word in bag_of_words):
    #                 negative_word_count[word] = 1
    #             elif (word in negative_word_count) and (word in bag_of_words):
    #                 negative_word_count[word] += 1
print(positive_word_count)
print(negative_word_count)
    # Remove everything except the colon
    # remove = string.punctuation
    # remove = remove.replace(":", "")
    # pattern = r"[{}]".format(re.escape(remove))
    # lines = re.sub(pattern, "", lines)
    # print(type(lines))
    #lines = lines.translate(str.maketrans('', '', string.punctuation))
    #print(lines)

#lines = lines.split()
#print(lines)
# Now with punctuation removed, split string on colon. Place first half and second half into tuple
# pattern2 = '[:]'
# # Split using re
# lines = re.split(pattern, lines)
# print(lines)
# print(len(lines))
#lines = lines.split(':')
#print(lines)
#maybe convert lines back into string, then do split on \n
#print(lines)

# # This pattern splits string on one or more spaces and the colon
# pattern = '[\s+:]'
# # Split using re
# lines = re.split(pattern, lines)
# #Create a dict for storing all unique words. Note: maybe create two Counters; one for incrementing when a word appears in a postivie review, another for when a word appears in a negative review
# wordCount = Counter(lines)
#
# # Create a list of words to be removed from Counter
# ignore = ["the", "a", "i", "if", "and", "it", "to", "this", "of", "for", "is", "with", "my", "that", "are", "was",
#           "they", "these", "but", "in", "it\'s", "book", "so", "have", "only", "you", "on", "after", "will", "had",
#           "as", "from", "do", "got", "just", "any", "were", "read", "all", "be", "both", "buy", "make"]
# stop_words = set(stopwords.words('english'))
# print(wordCount)
# print(len(wordCount.keys()))
# print(wordCount.most_common(100))
# print()
# # Loop to remove unnecessary words from wordCount Counter
# for x in stop_words:
#     if x in wordCount:
#         del wordCount[x]
# print(wordCount)
# print(len(wordCount.keys()))
# print(wordCount.most_common(100))
# Populating words dict with unique words and their frequencies
# for x in lines:
#     words[x] += 1
#
# print(words.most_common(10))