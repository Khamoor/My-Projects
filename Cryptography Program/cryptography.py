from database import letters
import encryption_functions as ef
import decryption_functions as df


def cipher_text(text, letters):
    """Converting numbers into encrypted text."""
    shifted_index = ef.indexing_of_letters(text, letters)
    new_text = ''
    for index in shifted_index:
        for keys, values in letters.items():
            if values == index:
                new_text += keys
    
    return new_text


def plain_text(text, letters):
    """Converting numbers into plain text."""
    numbers = df.multiplied_matices_into_list(text, letters)
    old_text = ''
    for index in numbers:
        for keys, values in letters.items():
            if values == index:
                old_text += keys
    
    return old_text


l = letters()
text = input("Enter your Message to Encode: ")
new_text = cipher_text(text, l)
print(new_text)
print(plain_text(new_text, l))
