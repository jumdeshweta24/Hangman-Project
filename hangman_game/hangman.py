from game import HangmanGame
from visuals import HangmanVisuals

def main():
    hangman_game = HangmanGame()
    hangman_visuals = HangmanVisuals()

    print("Welcome to Hangman!")
    print(hangman_visuals.get_visual(hangman_game.attempts))
    print(hangman_game.display_word())

    while "_" in hangman_game.display_word() and hangman_game.attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in hangman_game.guessed_letters:
            print("You already guessed that letter.")
        elif guess in hangman_game.word:
            hangman_game.guessed_letters.append(guess)
            print("Correct!")
        else:
            hangman_game.guessed_letters.append(guess)
            hangman_game.attempts -= 1
            print(f"Incorrect! You have {hangman_game.attempts} attempts left.")

        print(hangman_visuals.get_visual(hangman_game.attempts))
        print(hangman_game.display_word())

    if "_" not in hangman_game.display_word():
        print("Congratulations! You guessed the word correctly: " + hangman_game.word)
    else:
        print("Out of attempts! The word was: " + hangman_game.word)
        print("Game Over!")

if __name__ == "__main__":
    main()
