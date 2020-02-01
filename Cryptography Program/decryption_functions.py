import encryption_functions as ef
from settings import Settings
from database import letters


def text_to_individual_characters(text):
    """Converting Text Message into individual characters of list."""
    text_length = len(text)
    
    if text_length % 2 != 0:
        text += ' '
    
    chars = []
    
    for char in text:
        chars.append(char)
    
    return chars, text


def characters_to_values(text, letters):
    """Converting individual characters of list with its defined values."""
    chars, text = text_to_individual_characters(text)
    values = []
    
    for char in chars:
        keys = letters.keys()
        if char in keys:
            values.append(letters[char])
    
    return values, text


def values_to_matrices(text, letters):
    """Converting list of values into 1 x 2 matrix of matrices."""
    values, text = characters_to_values(text, letters)
    
    text_length = len(text)
    start = 0   # starting range of list
    end = 2     # ending range of list
    
    matrices = []
    for n in range(0,text_length // 2):
        matrices.append(values[start : end])
        start = end
        end += 2
        
    return matrices


def multiply_matrices_by_A_inverse(text, letters):
    """
    Multiplying matrices by A inverse matrix to change cipher text 
    into message.
    """
    matrices = values_to_matrices(text, letters)
    
    s = Settings()
    A_inv = s.A_inverse()
    
    y = []
    for matrix in matrices:
        r = [0, 0]
        for i in range(len(matrix)):
            for j in range(len(A_inv)):
                r[i] += matrix[j] * A_inv[j][i]
        y.append(r)
    
    return y


def multiplied_matices_into_list(text, letters):
    """Converting list of matrices into list of numbers."""
    y = multiply_matrices_by_A_inverse(text, letters)
    
    numbers = []
    for i in y:
        numbers += i
    
    return numbers

def indexing_of_letterss(text, letters):
    """
        Creating list of old index numbers that were shifted while creating 
        cipher text.
    """
    num1, text = characters_to_values(text, letters)
    num2 = ef.multiplied_matices_into_list(text, letters)
    
    num3 = list(map(lambda m, n : m - n, num1, num2))
    
    old_index = list(map(lambda m, n : m - n, num1, num3))
    
    return old_index, text


def indexing_of_letters(text, letters):
    """
        Creating list of index numbers that how much place the actual messege
        letters shifted by multiplying the matrices with defined matrix A.
    """
    numbers = multiplied_matices_into_list(text, letters)
    
    shifted_index = []
    
    for number in numbers:
        letters_length = len(letters)
        n = letters_length
        k = -1
        if number < 0:
            number *= -1    # Muliplying by -1 to make number positive
            for j in range(number):
                letters_length -= 1
                if letters_length < 1:
                    letters_length = n
            z = letters_length
        elif number > letters_length -1:
            for j in range(number):
                k += 1
                if k > n - 2:
                    k = -1
            z = k
        else:
            z = number
            
        shifted_index.append(z)
    
    return shifted_index


