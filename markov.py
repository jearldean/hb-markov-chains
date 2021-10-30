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

    words = text_string.split(" ")

    for i in range(len(words)-2):
        key_tuple = (words[i], words[i+1])
        next_word = words[i+2]
        # https://stackoverflow.com/questions/12905999/python-dict-how-to-create-key-or-append-an-element-to-key
        chains.setdefault(key_tuple,[next_word]).append(next_word)
    return chains


def make_text(chains, seed_word):
    """Return text from chains."""

    possible_seed_tuples = []
    for each_key in chains:
        if each_key[0] == seed_word:
            possible_seed_tuples.append(each_key)
    try:
        seed_tuple = choice(possible_seed_tuples)
    except IndexError:
        return f"Uh oh; '{seed_word}' is not a good seed_word for this text."
    words = [f"{seed_tuple[0]} {seed_tuple[1]}"]

    while True:
        
        possible_values = chains.get(seed_tuple)

        try:
            seed_tuple = (seed_tuple[1], choice(possible_values))
            words.append(seed_tuple[1])
        except TypeError:
            break

    return ' '.join(words)


for input_path in ['gettysburg.txt', 'green-eggs.txt', 'the_boy_who_lived.txt']:

    # Open the file and turn it into one long string
    try:
        input_text = open_and_read_file(input_path)
    except FileNotFoundError:
        print(f"Uh oh; '{input_path}' is not a good input_path.")
        break

    # Just make the seed word the first word of the text. Makes text natural-sounding.
    seed_word = input_text.split(" ")[0]

    # Get a Markov chain
    chains = make_chains(input_text)

    # Produce random text
    random_text = make_text(chains, seed_word)

    divider = "-=" * 40
    print(f"From {input_path}:\n{random_text}\n\n{divider}-\n")
