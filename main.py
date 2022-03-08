import random
import sys
def fetchWords():
    f = open('valid-wordle-words.txt', 'r')
    lines = f.readlines()
    for word in lines:
        word = word.strip()
    f.close()

    return lines

def compare_strings(a, correct):
    location_out = "Letters in correct location: "
    letter_out = "Letters in word but not in correct location: "
    correct_location = "correct spot "
    correct_letter = "correct letter "
    if len(a) == 5:
        for i in range(5):
            if a[i] in correct:
                if a[i] == correct[i]:
                    location_out += a[i]
                else:
                    letter_out += a[i]


    output = location_out + "\n" + letter_out
    return output




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
    correct_array = list(correct_word)
    #correct_word = "duals"
    #correct_array = list(correct_word)
    output_array = [["" for i in range(5)] for j in range(6)]
    alphabet_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    playing = True
    turn = 0

    while playing and turn < 7:
        print("\n------------------------\n")
        for row in output_array:
            print(row)

        for i in alphabet_array:
            print(i + " ", end="")
        print(correct_word)
        print("type your guess: ")
        guess = input().strip("\n")


        print(guess)
        print(correct_word)
        print(list(guess))
        print(list(correct_word))

        if list(guess) == list(correct_word):
            print("You win!")
            sys.exit()

        if guess == "adieu":
            print("----------------------------------------------------------------------")
            adieu = input("\n|Hello Lyndey. did you think I didnt know your starting word? how cute...\n hehe love you press anything to continue")
            print("----------------------------------------------------------------------")


        guess_array = list(guess)
        for letter in guess_array:
            if letter not in correct_array and letter in alphabet_array:
                alphabet_array.remove(letter)



        if not len(guess) == 5:
            print("the length of your guess needs to be 5 letters. No more no less.")
            playing = True






        print("\n" + compare_strings(guess, correct_word))
        turn +=1

        output_array[turn - 1][0] += guess[0]
        output_array[turn - 1][1] += guess[1]
        output_array[turn - 1][2] += guess[2]
        output_array[turn - 1][3] += guess[3]
        output_array[turn - 1][4] += guess[4]
        if turn == 5:
            print(correct_word)
            playing = False
    print("Bummer! You werent able to guess the worldle. play again?")


























if __name__ == "__main__":
    main()