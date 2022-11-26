import random
import string
from words import word
from hangman_visual import visual


def validation(words):
    chosen_word = random.choice(words)
    while '-' in chosen_word or ' ' in chosen_word:
        chosen_word = random.choice(words)

    return chosen_word.upper()


def game():
    the_word = validation(word)
    alphabets = set(string.ascii_uppercase)
    chosen_letters = set()
    lives = 7
    print('_ ' * len(the_word))
    while lives >= 0:

        guess_letter = input('guess the letters: ').upper()

        if guess_letter in alphabets - chosen_letters:
            chosen_letters.add(guess_letter)
            if guess_letter in the_word:
                show = [letter if letter in chosen_letters else '_' for letter in the_word]
                print(f'{guess_letter} is a right guess. You have used these letters', ' '.join(chosen_letters))
                print(' '.join(show))
                if ''.join(show) == the_word:
                    print('woah you won the game...!!')
                    break
            else:
                print(f'oops... {guess_letter} is a wrong guess. You have used these letters', ' '.join(chosen_letters))
                print(visual[lives])
                lives -= 1
        elif guess_letter in chosen_letters:
            print(f'You have already guessed the letter {guess_letter}')
        else:
            print('Invalid character')
    print('Sorry you lost')


game()
