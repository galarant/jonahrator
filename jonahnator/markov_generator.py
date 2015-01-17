#!/usr/bin/env python

from markov import MarkovChain


def load_quotes():
    try:
        with open('./quotes_data/quotes.txt', 'r') as quotes:
            txt = quotes.read()
    except IOError:
        raise IOError('Error: could not open text file')
    return txt


def random_phrase():
    txt = load_quotes()
    # Create an instance of the markov chain. By default, it uses MarkovChain.py's location to
    # store and load its database files to. You probably want to give it another location, like so:
    mc = MarkovChain("./quotes_data/markov_scores")
    # To generate the markov chain's language model, in case it's not present
    mc.generateDatabase(textSample=txt)

    # To let the markov chain generate some text, execute
    sentence = mc.generateString()
    generated_sentence = sentence[0].upper() + sentence[1:] + '.'
    return generated_sentence
