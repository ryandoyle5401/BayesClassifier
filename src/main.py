import string
import math


def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        # Lines is a list
        lines = f.readlines()
        return lines


def create_pbag_of_words(file):
    with open(file, 'r', encoding='utf-8') as f:
        # positve_words is a list, remove trailing newline
        positive_words = [word.strip() for word in f.readlines()]

    return positive_words


def create_nbag_of_words(file):
    with open(file, 'r', encoding='utf-8') as f:
        # negative_words is a list, remove trailing newline
        negative_words = [word.strip() for word in f.readlines()]

    return negative_words


def train_split(lines, split, positive_word_count, negative_word_count, bag_of_words):
    # Index represents the line number to stop reading reviews for training. The rest of the reviews will be read in for testing
    index = math.floor(len(lines) * split)
    # Modify list to remove punctuation, newline, make all characters lowercase. Also, only read i lines.
    for i in range(index):
        # Change list so that punctuation, newline is removed and characters are all lower
        lines[i] = lines[i].translate(str.maketrans('', '', string.punctuation)).strip().lower()
        # Count bag of word occurrences in positive reviews
        # If label is positive, lines[i] is a positive review
        if "positive" in lines[i]:
            # Split to analyze individual words
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


def test_split(lines, split, positive_word_count, negative_word_count, bag_of_words):
    # Index represents where train_split stopped
    index = math.floor(len(lines) * split)
    # Start reading from the index to the end of the list
    for i in range(index, len(lines)):
        # Process the line: remove punctuation, newline, and convert to lowercase
        lines[i] = lines[i].translate(str.maketrans('', '', string.punctuation)).strip().lower()
        # Count occurrences in the bag of words for positive reviews
        if "positive" in lines[i]:
            words = lines[i].split()
            for word in words:
                if (word not in positive_word_count) and (word in bag_of_words):
                    positive_word_count[word] = 1
                elif (word in positive_word_count) and (word in bag_of_words):
                    positive_word_count[word] += 1
        # Count occurrences in the bag of words for negative reviews
        elif "negative" in lines[i]:
            words = lines[i].split()
            for word in words:
                if (word not in negative_word_count) and (word in bag_of_words):
                    negative_word_count[word] = 1
                elif (word in negative_word_count) and (word in bag_of_words):
                    negative_word_count[word] += 1


def main():
    #bag_of_words = []
    positive_word_count = {}
    negative_word_count = {}
    train_split = 0.5
    # Get bag of words
    positive_bag_of_words = create_pbag_of_words("positive_words.txt")
    negative_bag_of_words = create_nbag_of_words("negative_words.txt")
    print(positive_bag_of_words)
    print(negative_bag_of_words)
    # Read file
    lines = read_file("reviews.txt")

if __name__ == "__main__":
    main()