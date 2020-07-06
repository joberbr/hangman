from random import randint

HANGMAN_PICS = {
    0: """
    +-----+
    |     |
    |
    |
    |
    |
===========  
""",
    1: """
    +-----+
    |     |
    |     0
    |
    |
    |
===========  
""",
    2: """
    +-----+
    |     |
    |     0
    |     |
    |
    |
===========  
""",
    3: """
    +-----+
    |     |
    |     0
    |    /|
    |
    |
===========  
""",
    4: """
    +-----+
    |     |
    |     0
    |    /|\\
    |
    |
===========  
""",
    5: """
    +-----+
    |     |
    |     0
    |    /|\\
    |    /
    |
===========  
""",
    6: """
    +-----+
    |     |
    |     0
    |    /|\\
    |    / \\
    |
===========  
""",
}

WORD_LIST = [
    "aardvark",
    "beetle",
    "caricature",
    "delphi",
    "eagle",
    "fern",
    "grasshopper",
    "helix",
    "Iowa",
    "jackelope",
    "kelvin",
    "llama",
    "Minnesota",
    "nettles",
    "orpheum",
    "picnic",
    "quail",
    "realization",
    "summer",
    "talons",
    "umbrella",
    "vertigo",
    "wombat",
    "xylophone",
    "Yellowstone",
    "zoophilia",
]

remaining_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def gameon_choice():
    choice = "wrong"
    while choice not in ["Y", "N"]:

        choice = input("Do you want to play Hangman? (Y or N): ").upper()

        if choice not in ["Y", "N"]:
            print("Sorry, I don't understand, please choose Y or N ")

    if choice == "Y":
        return True
    else:
        return False


def get_random_word(word_list):
    answer = word_list[randint(0, len(word_list) - 1)].upper()
    blank_answer = "_ " * len(answer)
    return answer, blank_answer


def display_game(word, num_incorrect):
    print(HANGMAN_PICS[num_incorrect])
    print(word)


def guess_letter():
    guess = "wrong"
    while guess not in remaining_letters:
        guess = input("Choose a letter: ").upper()

        if guess not in remaining_letters:
            print("Letter was already chosen. Guess again: ")

    remaining_letters.remove(guess)

    return guess, remaining_letters


def update_incorrect(guess, answer, incorrect):
    if guess not in answer:
        incorrect += 1
    return incorrect


def update_blank_word(answer, blank_answer, guess):
    positions = []
    count = 0
    for letter in answer:
        if letter == guess:
            positions.append(count)
        count += 1

    blank_list = list(blank_answer)

    for position in positions:
        blank_list[2 * position] = guess.upper()

    return "".join(blank_list)


def check_won_lost(answer, blank_answer, incorrect, game_on):
    if incorrect == 6 and answer != blank_answer.replace(" ", ""):
        game_on = False
        display_game(blank_answer, incorrect)
        print("You lost :( Better luck next time.")
        print(f"The answer is {answer}.")
    elif incorrect < 6 and answer == blank_answer.replace(" ", ""):
        game_on = False
        display_game(blank_answer, incorrect)
        print("You are a WINNER!!!!!")

    return game_on


incorrect = 0
game_on = True
game_on = gameon_choice()
answer, blank_answer = get_random_word(WORD_LIST)

while game_on:
    display_game(blank_answer, incorrect)
    guess, remaining_letters = guess_letter()
    incorrect = update_incorrect(guess, answer, incorrect)
    blank_answer = update_blank_word(answer, blank_answer, guess)
    game_on = check_won_lost(answer, blank_answer, incorrect, game_on)

    if game_on == False:
        game_on = gameon_choice()
        if game_on == True:
            incorrect = 0
            remaining_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            answer, blank_answer = get_random_word(WORD_LIST)
