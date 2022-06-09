from sentences import get_determiner, get_noun, get_preposition, get_prepositional_phrase, get_verb
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    #1. Test single nouns
    single_nouns = [ "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    for _ in range(5):
        noun = get_noun(1)

        #very that the noun exist in the arr
        assert noun in single_nouns

    #2. test plural nouns
    plural_nouns = [ "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    for _ in range(5):
        noun = get_noun(2)

        assert noun in plural_nouns


def test_get_verb():
    #1. Test past verb
    past_verbs = [ "drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    for _ in range( 6 ):
        verb = get_verb(1, 'past')
        assert verb in past_verbs

    present_single_verbs = [ "drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes" ]
    for _ in range(6):
        verb = get_verb( 1, 'present' )
        assert verb in present_single_verbs

    present_plural_verbs = [ "drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write" ]
    for _ in range(6):
        verb = get_verb(2, 'present')
        assert verb in present_plural_verbs

    future_verbs = [ "will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    for _ in range(6):
        verb = get_verb(1, 'future')

        assert verb in future_verbs

def test_get_prepositional_phrase():
    phrase = get_prepositional_phrase(1)
    phrase_words = phrase.split(' ')
    assert len(phrase_words) == 3

    prepositions = [ 
        "about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
    ]
    single_determiners = ["a", "one", "the"]
    single_nouns = [ "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

    plural_determiners = ["two", "some", "many", "the"]
    plural_nouns = [ "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    assert phrase_words[0] in prepositions
    assert phrase_words[1] in single_determiners
    assert phrase_words[2] in single_nouns

    #testing plural 
    phrase_plural = get_prepositional_phrase(2)
    phrase_plural_words = phrase_plural.split(' ')
    assert len(phrase_plural_words) == 3

    assert phrase_plural_words[0] in prepositions
    assert phrase_plural_words[1] in plural_determiners
    assert phrase_plural_words[2] in plural_nouns

def test_get_preposition():
    words = [ 
        "about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
    ]
    preposition = get_preposition()

    assert preposition in words

pytest.main(["-v", "--tb=line", "-rN", __file__])