#!/usr/bin/python3

import re
import sys
from select import select


# Checks each word for validity and then adds up their dominant letter totals.
def get_dominant_letter_count(word_list, valid_word):
    """
    :param word_list: a list of words composing a sentence.
    :param valid_word: a regex string defining the acceptance criteria being matched.
    :return: returns the total of dominant characters across all words in the sentence.
    """
    total = 0
    for word in word_list:
        if valid_word.match(word):
            # Find max count for each word.
            max_count = max([word.count(x) for x in word])
            # Add the dominant counts up.
            total += max_count
    return total


def main():
    sentences = ''

    # Check the number of arguments to see if a filename was provided as input.
    if len(sys.argv) > 1:
        # Enforces the input file extensions.
        if sys.argv[1].lower().endswith('.txt'):
            try:
               fin = open(sys.argv[1], 'r')
               sentences = fin.read().lower()
            # Catches file IO errors where the file does not exist.
            except IOError:
                print('ERROR: Invalid filename. File could not be found.')
                return
        # Catches all invalid filename extension types.
        else:
            print('ERROR: Invalid input file extension. Only accepts \'.txt\' files.')
            return

    # Checks to see if stdin has been assigned to a device, i.e. input was provided.
    elif select([sys.stdin,], [], [], 0.0)[0]:
        sentences = sys.stdin.read().lower()

    # Creates a list of words by splitting the input using whitespace as a delimiter.
    word_list = sentences.split()
    # Regex expression that accepts only alphabetic strings possibly sandwiched by whitespace
    valid_word = re.compile('^\s?[a-zA-Z]+\s?$',)

    # Total number of dominant letters from all words across all sentences.
    count = get_dominant_letter_count(word_list, valid_word)
    print(count)
    return count


if __name__ == '__main__':
    main()
