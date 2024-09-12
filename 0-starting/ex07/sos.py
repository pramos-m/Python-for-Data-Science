import sys

NESTED_MORSE = {
    " ": "/",
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--", 
    "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..",
    "9": "----.", "0": "-----",
}

def encode_morse(text):
    """
    This function encodes a string to Morse code.

    Parameters:
        text (str): The string to encode.

    Returns:
        str: The Morse code of the given string.

    Raises:
        AssertionError: If the given argument is not a string.
        AssertionError: If the given string contains non-alphanumeric
        characters.
    """
    assert isinstance(text, str), "wrong argument type"
    assert text.isalnum(), "the arguments are bad"
    
    return ''.join(NESTED_MORSE[char.upper()] for char in text)

def main():
    """
    Main function that processes input and calls the encoder.
    """
    if len(sys.argv) != 2:
        raise AssertionError("wrong number of arguments")
    
    text = sys.argv[1]
    try:
        morse_text = encode_morse(text)
        print(morse_text)
    except AssertionError as e:
        print("AssertionError:", e)

if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"{error.__class__.__name__}: {error}")
