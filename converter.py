import alphaToBrailleMap

CAPITAL = chr(10272)
NUMBER = chr(10300)
UNRECOGNIZED = '?'

quotes = True

def is_braille(char):
    # Return true if a char is braille.
    if len(char) > 1:
        return False
    return char in alphaToBrailleMap.letters \
        or char in alphaToBrailleMap.numbers \
        or char in alphaToBrailleMap.punctuation \
        or char in alphaToBrailleMap.contractions \
        or char == CAPITAL \
        or char == NUMBER

def find_utf_code(char):
    # Find the UTF code of a particular character. Used what an unidentified char is found.
    if len(char) != 1:
        return -1
    for i in range(0, 55000):
        if char == chr(i):
            return i

def extract_words(string):
    # Split up a sentence based on whitespace (" ") and new line ("\n") chars.
    words = string.split(" ")
    result = []
    for word in words:
        temp = word.split("\n")
        for item in temp:
            result.append(item)
    return result

def trim(word):
    # Remove punctuation around a word. Example: cat." becomes cat
    while len(word) != 0 and not word[0].isalnum():
        word = word[1:]
    while len(word) != 0 and not word[-1].isalnum():
        word = word[:-1]
    return word

def number_handler(word):
    # Replace each group of numbers in a word to their respective braille representation.
    if word == "":
        return word
    result = word[0]
    if word[0].isdigit():
        result = NUMBER + alphaToBrailleMap.numbers.get(word[0])
    for i in range(1, len(word)):
        if word[i].isdigit() and word[i-1].isdigit():
            result += alphaToBrailleMap.numbers.get(word[i])
        elif word[i].isdigit():
            result += NUMBER + alphaToBrailleMap.numbers.get(word[i])
        else:
            result += word[i]
    return result


def capital_letter_handler(word):
    # Put the capital escape code before each capital letter.
    if word == "":
        return word
    result = ""
    for char in word:
        if char.isupper():
            result += CAPITAL + char.lower()
        else:
            result += char.lower()
    return result

def char_to_braille(char):
    # Convert an alphabetic char to braille.
    if is_braille(char):
        return char
    elif char == "\n":
        return "\n"
    elif char == "\"":
        global open_quotes
        if open_quotes:
            open_quotes = not open_quotes
            return alphaToBrailleMap.punctuation.get("“")
        else:
            open_quotes = not open_quotes
            return alphaToBrailleMap.punctuation.get("”")
    elif char in alphaToBrailleMap.letters and char.isupper():
        return CAPITAL + alphaToBrailleMap.letters.get(char)
    elif char in alphaToBrailleMap.letters:
        return alphaToBrailleMap.letters.get(char)
    elif char in alphaToBrailleMap.punctuation:
        return alphaToBrailleMap.punctuation.get(char)
    else:
        print("Unrecognized Symbol:", char, "with UTF code:", find_utf_code(char))
        return UNRECOGNIZED

def word_to_braille(word):
    # Convert an alphabetic word to braille.
    if word in alphaToBrailleMap.contractions:
        return alphaToBrailleMap.contractions.get(word)
    else:
        result = ""
        for char in word:
            result += char_to_braille(char)
        return result

def build_braille_word(trimmed_word, shavings, index, braille):
    # Translate a trimmed word to braille then re-attach the shavings.
    if shavings == "":
        braille += word_to_braille(trimmed_word)
    else:
        for i in range(0, len(shavings)):
            if i == index and trimmed_word != "":
                braille += word_to_braille(trimmed_word)
            braille += word_to_braille(shavings[i])
        if index == len(shavings):  # If the shavings are all at the beginning.
            braille += word_to_braille(trimmed_word)
    return braille

def convertToGrade1(string) :
    brilleStr = ''

    return string

def convertToGrade2(string) :

    braille = ""
    words = extract_words(string)
    
    for word in words:
        word = number_handler(word)
        word = capital_letter_handler(word)
        trimmed_word = trim(word)
        untrimmed_word = word
        index = untrimmed_word.find(trimmed_word)
        shavings = untrimmed_word.replace(trimmed_word, "")
        braille = build_braille_word(trimmed_word, shavings, index, braille) + " "

    print()

    return braille[:-1]

str = input("enter a string: ")
print(convertToGrade2(str))