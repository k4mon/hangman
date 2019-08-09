import os
import random


class Hangman:
    def __init__(self):
        self.words = []

    def start(self, language):
        self.load_words(language)
        self.game_loop()

    def load_words(self, language):
        with open(f"dictionaries/{language}.txt", 'r') as wordfile:
            self.words.extend([line.strip() for line in wordfile.readlines()])

    def pick_a_word(self):
        return self.words[random.randint(0, len(self.words) - 1)]

    def game_loop(self):
        game = True
        lives = 9
        while game:
            word = self.pick_a_word()
            guesses = set()
            current_guess = []
            for x in word:
                current_guess.append("_")
            while True:
                print(f"Zgadujesz słowo: {' '.join(current_guess)}")
                guess = input("podaj literke (bądź spacje) lub zgadnij całe słowo: ")
                if guess == word:
                    print("Wygrana!")
                    lives += 2
                    break
                elif guess in guesses:
                    lives -= 1
                    print("Juz to próbowałeś...")
                elif len(guess) == 1 and guess in word:
                    guesses.add(guess)
                    current_guess = []
                    for x in word:
                        if any(x == y for y in guesses):
                            current_guess.append(x)
                        else:
                            current_guess.append("_")
                else:
                    lives -= 1
                    print(f"nie trafione! zostało żyć: {lives}")
                if lives == 0:
                    print(f"przegrana! słowo do zgadnięcia to: {word}")
                    game = False
                    break


def main():
    available_languages = [x.split(".")[0] for x in os.listdir("dictionaries")]
    language = input(f"Wybierz język z {available_languages}: ")
    if language not in available_languages:
        print("Niestety, nie mamy słownika dla tego języka. Papa!")
        exit(1)
    Hangman().start(language)


main()
