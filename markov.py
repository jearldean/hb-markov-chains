"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text = open(file_path).read()

    return text
    


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    text_string = text_string.replace("\n", "\n ")
    words = text_string.split(" ")
    if '' in words:
        words.remove('')

    for i in range(len(words)-2):
        key_tuple = (words[i], words[i+1])
        next_word = words[i+2]
        # https://stackoverflow.com/questions/12905999/python-dict-how-to-create-key-or-append-an-element-to-key
        if key_tuple in chains:
            existing_list = chains[key_tuple]
            existing_list.append(next_word)
            chains[key_tuple] = existing_list  # existing_list is really a new_list.
        else:
            chains[key_tuple] = [next_word] 
    return chains


def make_text(chains, seed_word):
    """Return text from chains."""


    #key_words = choice(list(chains.keys()))
    for each_key in chains:
        if each_key[0] == seed_word:
            next_pair = each_key
    words = [f" {next_pair[0]} {next_pair[1]}"]

    while True:

        #a_random_key_from_chains_dict = choice(list(chains.keys()))
        
        possible_values = chains.get(next_pair)

        try:
            next_pair = (next_pair[1], choice(possible_values))
            words.append(next_pair[1])
        except TypeError:
            break

        #print(words)

    #print(a_random_key_from_chains_dict)

    return ' '.join(words)


input_path = 'gettysburg.txt'
seed_word = "Four"


#input_path = 'green-eggs.txt'
#seed_word = "Would"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains, seed_word)

print(random_text)