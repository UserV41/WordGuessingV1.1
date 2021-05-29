import random


def main():
    # The game continue to play until the user want to stop.
    wanna_play = True
    while wanna_play:
        # 1)Ask the user for numbers of attempts
        INITIAL_GUESSES = input_guesses()
        # 2)Take a word from database;
        secret_word = get_word()
        # 3)Play the game;
        play_game(secret_word, INITIAL_GUESSES)
        # 4)Play again the game ?
        wanna_play = play_again()


def input_guesses():
    # The function check if the value got from Input is positive and a Integer.
    while True:
        INITIAL_GUESSES = input("How many attempts you want to have for the game? ")
        print("\n")
        try:
            INITIAL_GUESSES = int(INITIAL_GUESSES)
            if INITIAL_GUESSES < 1:
                print("Please write a positive integer value.")
                continue
            break
        except ValueError:
            print("Please write a positive integer value.")
    return INITIAL_GUESSES


def get_word():
    # It takes all the words from a TXT file.
    LEXICON_FILE = "Lexicon.txt"
    # 1)Take a file with all the word; 2)Put it in a list; 3)Choose a random word;
    with open(LEXICON_FILE, "r") as f:
        word_list = f.read().split()
    secret_word = random.choice(word_list)
    return secret_word


def play_game(secret_word, INITIAL_GUESSES):
    # The play_game() is divided in 3 function which each will focus on a precise function.
    answer, secret_word_list = start_game(secret_word, INITIAL_GUESSES)
    INITIAL_GUESSES = main_game_code(INITIAL_GUESSES, answer, secret_word_list, secret_word)
    win_or_lose(INITIAL_GUESSES, secret_word)


def start_game(secret_word, INITIAL_GUESSES):
    # We put the word in a list and give an idea to the User how many letters there is inside.
    answer = []
    secret_word_list = list(secret_word)
    for letter in range(len(secret_word)):
        answer.append("-")
    print("The word now looks like this: " + "".join(answer))
    print("You have " + str(INITIAL_GUESSES) + " guesses left.")
    print("\n")
    return answer, secret_word_list


def main_game_code(INITIAL_GUESSES, answer, secret_word_list, secret_word):
    # The function will continue to ask the user for letter until he finished all the attempt or guess the word.
    while answer != secret_word_list:
        if INITIAL_GUESSES != 0:
            print("\n")
            player_answer = (str(input("Type a single letter here, then press enter: "))).upper()
            # the (while) function will make sure the user can't put more than one letter as input
            while len(player_answer) != 1:
                print("Guess should only be a single character.")
                print("\n")
                player_answer = (str(input("Type a single letter here, then press enter: "))).upper()
            if player_answer in secret_word:
                print("The guess is correct.")
                for x in range(len(secret_word)):
                    if player_answer == secret_word[x]:
                        answer[x] = player_answer
                print("".join(answer))
            else:
                print("There are no " + player_answer + "'s in the word")
                print("The word now looks like this: " + "".join(answer))
                INITIAL_GUESSES = INITIAL_GUESSES - 1
            print("You have " + str(INITIAL_GUESSES) + " guesses left.")
        else:
            break
    return INITIAL_GUESSES


def win_or_lose(INITIAL_GUESSES, secret_word):
    # 1)Decide if the player either have lost or won.
    if INITIAL_GUESSES == 0:
        print("Sorry, you lost. The secret word is: " + secret_word)
        print("\n")
    elif INITIAL_GUESSES != 0:
        print("Congratulations, the word is: " + secret_word)
        print("\n")


def play_again():
    #ask the user if he wants to play again.
    while True:
        wanna_play = input("You still wanna play another game ? YES or NO.").upper()
        if wanna_play == "YES":
            wanna_play = True
            break
        elif wanna_play == "NO":
            wanna_play = False
            break
        else:
            print("Please insert YES or NO.")
            continue
    return wanna_play



if __name__ == "__main__":
    main()
