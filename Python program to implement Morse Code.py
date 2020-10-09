# Python program to implement Morse Code Translator

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def englishToMorse(inp):
    morseFromEnglish = ''
    for letter in inp:
        if letter != ' ':
            # look for morse code and add space after char
            morseFromEnglish += MORSE_CODE_DICT[letter] + ' '
        else:
            morseFromEnglish += ' '  # 1 space indicates diff. char and 2 indicates diff. words
    return morseFromEnglish


def morsetoEnglish(inp):
    try:
        inp += ' '

        englishFromMorse = ''
        morseCodeForSingleChar = ''
        for letter in inp:
            if (letter != ' '):
                i = 0
                morseCodeForSingleChar += letter  # storing morse code of a single character

            else:
                i += 1  # if i = 1 that indicates a new character
                if i == 2:  # if i = 2 that indicates a new word
                    englishFromMorse += ' '  # space to separate words
                else:  # accessing the keys using their values
                    englishFromMorse += list(MORSE_CODE_DICT.keys())[list(
                        MORSE_CODE_DICT.values()).index(morseCodeForSingleChar)]
                    morseCodeForSingleChar = ''
        return englishFromMorse
    except:
        print("You Entered Wrong Morse Code")


choice = input(
    "Choose the conversion: \n \t 1.English To Morse Code \n \t 2.Morse Code To English \n \t")
if choice == '1':
    inp = input("Enter text to convert into Morse: \n \t \t")
    result = englishToMorse(inp.upper())
    print(result)
elif choice == '2':
    inp = input("Enter Morse Code:\n")
    result = morsetoEnglish(inp)
    print(result)
else:
    print("Enter right choice")
