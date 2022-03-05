import random
import sys
def fetchWords():
    f = open('valid-wordle-words.txt', 'r')
    lines = f.readlines()
    for word in lines:
        word = word.strip()
    f.close()

    return lines

def compare_strings(a, correct_word):
    out = ""
    if len(a) == 5:
        for i in range(5):
            if a[i] in correct_word:
                if a[i] == correct_word[i]:
                    out += correct_word[i]
                else:
                    out += a[i]
    return out




def main():
    start_menu_running = True
    while start_menu_running:
        start = input("Welcome to Kaden's recreation of WORDLE. To play, type the letter p and press enter. To quit, type q and press enter.")
        if start == "p":
            start_menu_running = False
        elif start == "q":
            sys.exit()
        else:
            print("That is not a correct input. Please type the letter p and press enter to play, or the letter q and press enter to quit.\n\n")

    print("\n\n-----------------------")
    print("        WORDLE")
    print("-----------------------")
    print("\n\nGuess the WORDLE in six tries.\n\nEach guess must be a valid five-letter word. Hit the enter button to submit.\n\nAfter each guess, the outline of the letters will change to show how close your guess was to the word ")
    input("Type any letter and press enter to continue")

    words = fetchWords()
    correct_word = words[random.randint(0, 12972)]
    output_array = [[[] for i in range(5)] for j in range(6)]
    alphabet_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for row in output_array:
        print(row)

    for i in alphabet_array:
        print(i +" ", end="")
    print(correct_word)
    playing = True
    turn = 0

    while playing:
        guess = input("type your guess:")

        if not len(guess) == 5:
            print("the length of your guess needs to be 5 letters. No more no less.")
            playing = True

        if guess == correct_word:
            print("You win!")
            playing = False

        print(compare_strings(guess, correct_word))























if __name__ == "__main__":
    main()