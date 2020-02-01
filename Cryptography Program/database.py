# Creating Database of Characters with its values
from settings import Settings


def characters():
    """Creating list of characters."""
    s = Settings()
    
    list_of_chars = s.space + s.capital_letters + s.full_stop + s.question_mark
    
    characters = list(map(chr, list_of_chars))
    
    return characters


def letters():
    """Creating database of list of characters with its values."""
    letters = {}
    i = 0
    for character in characters():
        if character in characters():
            letters[character] = i
        i += 1
    
    return letters
