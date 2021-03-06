""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    f = open(file_name).read()
    f = f[6200:-18820]
    f = f.replace('--', ' ')
    f = f.split()
    index = 0
    for item in f:
        f[index] = item.strip(string.punctuation).lower()
        index += 1
    return f


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    pass
    f = word_list
    d = {}
    h = []
    for word in word_list:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    for key in d:
        h.append((d[key],key))
    h.sort(reverse = True, key = lambda hist : hist[0])
    return h[0:n]

if __name__ == "__main__":
    mines = get_word_list('Solomon.txt')
    mines = get_top_n_words(mines, 100)
    for item in mines:
        print(str(item[0]) + ": " + item[1])
    #print("Running WordFrequency Toolbox")
    #print(string.punctuation)
