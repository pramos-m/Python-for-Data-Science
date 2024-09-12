from ft_filter import ft_filter
import sys

def main():
    # 1. Verification of the number of arguments given and its type
    # 2. Split the string given into a list of words
    # 3. Use of lamba list comprehenstion to filter the worlds that lenght are bigger than number has given as argument
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad") # El primer argumento es un string
    try: # Verificar tipos de argumentos
        number = int(sys.argv[2])
        text = str(sys.argv[1])
    except ValueError:
        raise AssertionError("the arguments are bad")
    # Convertir el string en una lista de palabras
    words = text.split()

    # Usar lambda y comprensión de listas para filtrar las palabras
    filtered_words = list(filter(lambda word: len(word) > number, words))

    print(filtered_words)
if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"{error.__class__.__name__}: {error}")
