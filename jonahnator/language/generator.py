#!/usr/bin/env python
import os
import random
from markov import MarkovChain
from silly_nltk import PhraseGenerator


PATH = os.path.dirname(os.path.realpath(__file__))


def load_quotes():
    try:
        with open(PATH + '/quotes_data/quotes.txt', 'r') as quotes:
            txt = quotes.read()
    except IOError:
        raise IOError('Error: could not open text file')
    return txt


def random_markov_phrase():
    txt = load_quotes()
    # Create an instance of the markov chain. By default, it uses MarkovChain.py's location to
    # store and load its database files to. You probably want to give it another location, like so:
    mc = MarkovChain(PATH + '/quotes_data/markov_scores')
    # To generate the markov chain's language model, in case it's not present
    mc.generateDatabase(textSample=txt)

    # To let the markov chain generate some text, execute
    sentence = mc.generateString()
    generated_sentence = sentence[0].upper() + sentence[1:]
    if generated_sentence[-1] not in ['?', '!']:
        generated_sentence += '.'
    return generated_sentence


def random_nltk_phrase():
    txt = load_quotes()
    p = PhraseGenerator(txt)
    quote = random.choice(txt.split('\n'))
    seed = quote.split(' ')[0]
    return p(seed)
