import random
import TextArt as tx

def check_complete(blanks):
    if "_" in blanks: return False
    else:
        print("You Won!")
        return True


def play_game():
    with open('words.txt') as f:
        word_list = f.read().splitlines()

    chosen_word = str(random.choice(word_list)).lower()
    print(chosen_word)

    blanks = []
    lives = 6
    for _ in chosen_word:
        blanks.append("_")
    print(f"{blanks}")

    while not check_complete(blanks):
        guess = input("Guess a New Letter:\n")
        if guess in chosen_word:
            if guess in blanks:
                print("You have already guessed this letter")
            else:
                for idx in range(len(chosen_word)):
                    if chosen_word[idx] == guess:
                        blanks[idx] = guess
        else:
            lives -= 1
            print(f"You guessed '{guess}' which is not in the word. You loose a life")
            print("---------------------")
            print(tx.stages[lives])
            if lives == 0:
                print("You Loose!")
                break

        print(f"{blanks}")


