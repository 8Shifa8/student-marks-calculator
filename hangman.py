# Hangman
import random


words = [
    "python",
    "bumblebee",
    "unicorn",
    "octopus",
    "elephant",
    "jigsaw",
    "galaxy",
    "platypus",
    "falcon",
    "trampoline",
    "igloo",
    "telescope",
    "tyrannosaurus",
    "carousel",
    "lighthouse",
    "parachute",
    "rollercoaster",
    "metamorphosis",
    "galapagos",
    "narwhal",
    "raccoon",
    "marzipan",
    "thermometer",
    "chrysanthemum",
    "iguana",
    "asteroid",
    "gyroscope",
]


def print_display(display):
    print("".join(display))


def update_display_word(word, display, guess):
    for i in range(len(word)):
        if word[i] == guess:
            display[i] = guess


def start_game():
    word = random.choice(words)
    display = ["_" for i in range(len(word))]
    attempts = 15
    guessed_letters = []

    print("Let's play Hangman!")
    print_display(display)
    print("The number of letters is", len(word))
    print()

    while attempts > 0 and "_" in display:
        print_display(display)
        guess = input("Guess a letter:").lower()

        if guess == "exit":
            print("Goodbye!")
            return

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        guessed_letters.append(guess)

        if len(guess) > 1:
            print("Please input a single letter!")
            continue

        if guess in word:
            update_display_word(word, display, guess)
            print("That was Correct!")

        else:
            print("Inorrect guess!")
            attempts -= 1

        print("Attempts left:", attempts)
        print()

    if "_" not in display:
        print("You won! The word was", word)
    elif attempts == 0:
        print("You lost!The word was:", word)


start_game()
