import random
import string

from words import words


def get_valid_word(words):
    word = random.choice(words)  # randomly select a word from words list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


def hangman():
    word = get_valid_word(words).upper()
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # letters the user has guessed

    # getting user input
    while len(word_letters) > 0:
        #  letters used by user
        print("You have used these letters: ", " ".join(used_letters))

        # what is the current word being guessed
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print("You have already typed that letter.  Please try again!")

        else:
            print("Invalid character. Please try again!")

    num_guesses = len(used_letters)
    print(f"Congratulations you have solve the puzzle for the word {word} and it only took {num_guesses} guesses!")

hangman()
