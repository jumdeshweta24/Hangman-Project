import random

class HangmanGame:
    def __init__(self):
        self.words = ["python", "hangman", "developer", "coding", "challenge", "programmer", "computer", "algorithm", "debugging"]
        self.word = random.choice(self.words)
        self.guessed_letters = []
        self.attempts = 6

    def display_word(self):
        display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += "_"
        return display
