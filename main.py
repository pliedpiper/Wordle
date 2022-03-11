import random
import sys
import pygame

pygame.init()

WIDTH, HEIGHT = 500, 700

white = (225, 255, 255)
grey = (128, 128, 128)
black = (0, 0, 0)
teal = (3, 218, 198)
green = "#43a047"
purple = (97, 120, 226)
yellow = (226, 203, 97)
red = (125, 55, 77)
turn = 0
alphabet_array_one = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
alphabet_array_two = ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
alphabet_array_three =  ['u', 'v', 'w', 'x', 'y', 'z']

board = [[" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "]]
lines = []
with open("wordle-nyt-answers-alphabetical.txt") as f:
    lines = [line.rstrip() for line in f]
print(lines)




fps = 60
timer = pygame.time.Clock()
huge_font = pygame.font.Font('freesansbold.ttf', 56)

small_font = pygame.font.Font('freesansbold.ttf', 30)
alphabet_font = pygame.font.Font('freesansbold.ttf', 10)

secret_word = lines[random.randint(0, len(lines)-1)]


game_over = False
letters = 0
turn_active = True

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("KORDLE")

def draw_board():
    global turn
    global board
    for col in range (0, 5):
        for row in range(0 ,6):
            pygame.draw.rect(screen, purple, (col * 100 + 12, row * 100 + 12, 75, 75), 3, 5)
            piece_text = huge_font.render(board[row][col], True, black)
            screen.blit(piece_text, (col * 100 + 30, row * 100 + 25))

    pygame.draw.rect(screen, teal, (5, turn * 100 + 5, WIDTH  - 10, 90), 3, 5)
def draw_alphabet():
    for i in range(len(alphabet_array_one)):
        piece_text = small_font.render(alphabet_array_one[i], True, black)
        screen.blit(piece_text, (i * 50 + 500,  100 + 25))
    for i in range(len(alphabet_array_two)):
        piece_text = small_font.render(alphabet_array_two[i], True, black)
        screen.blit(piece_text, (i * 50 + 500,  200 + 25))
    for i in range(len(alphabet_array_three)):
        piece_text = small_font.render(alphabet_array_three[i], True, black)
        screen.blit(piece_text, (i * 50 + 500, 300 + 25))

def check_words():
    global turn
    global board
    global secret_word
    for col in range(0, 5):
        for row in range(0, 6):
            if secret_word[col] == board[row][col] and turn > row:
                pygame.draw.rect(screen, green, (col * 100 + 12, row * 100 + 12, 75, 75), 0, 5)
            elif board[row][col] in secret_word and turn > row:
                pygame.draw.rect(screen, yellow, (col * 100 + 12, row * 100 + 12, 75, 75), 0, 5)



running = True
while running:
    timer.tick()
    screen.fill(red)
    check_words()
    draw_board()
  #  draw_alphabet()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and letters > 0:
                board[turn][letters -1] = ' '
                letters -= 1
            if event.key == pygame.K_RETURN and not game_over:
                turn += 1
                letters = 0
            if event.key == pygame.K_RETURN and game_over:
                secret_word = lines[random.randint(0, len(lines) - 1)]
                turn = 0
                letters = 0
                game_over = False
                board = [[" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " "]]
        if event.type == pygame.TEXTINPUT and turn_active and not game_over:
            entry = event.__getattribute__("text")
            board[turn][letters] = entry
            letters += 1

    for row in range(0, 6):
        guess = board[row][0] + board[row][1] + board[row][2] + board[row][3] + board[row][4]
        if guess == secret_word and row < turn:
            game_over = True


    if letters == 5:
        turn_active = False
    if letters < 5:
        turn_active = True

    if turn == 6:
        game_over = True
        loser_text = small_font.render('Loser! Correct Word: ' + secret_word, True, white)
        screen.blit(loser_text, (40, 610))

    if game_over and turn < 6:
        winner_text = huge_font.render('You win!', True, white)
        screen.blit(winner_text, (40, 610))

    pygame.display.update()


def fetchWords():
    f = open('valid-wordle-words.txt', 'r')
    lines = f.readlines()
    for word in lines:
        word.strip()
    f.close()

    return lines


def compare_strings(guess, correct):
    location_out = "Letters in correct location: "
    letter_out = "Letters in word but not in correct location: "
    "correct spot "
    "correct letter "
    if len(guess) == 5:
        for i in range(5):
            if guess[i] in correct:
                if guess[i] == correct[i]:
                    location_out += guess[i]
                else:
                    letter_out += guess[i]

    output = location_out + "\n" + letter_out
    return output


def oldWordle():
    wordle = True
    while wordle:
        turn = 0
        start_menu_running = True
        while start_menu_running:
            start = input(
                "Welcome to Kaden's recreation of WORDLE(KORDLE). To play, type the letter p and press enter. To quit, "
                "type q and press enter.")
            if start == "p":
                start_menu_running = False
            elif start == "q":
                sys.exit()
            else:
                print(
                    "That is not a correct input. Please type the letter p and press enter to play, or the letter q "
                    "and press enter to quit.\n\n")

        print("\n\n-----------------------")
        print("        WORDLE")
        print("-----------------------")
        print(
            "\n\nGuess the WORDLE in six tries.\n\nEach guess must be a valid five-letter word. Hit the enter button "
            "to submit.\n\nAfter each guess, the outline of the letters will change to show how close your guess was "
            "to the word ")
        input("Type any letter and press enter to continue")

        words = fetchWords()
        correct_word = words[random.randint(0, 12972)]
        correct_word = correct_word.strip()
        correct_array = list(correct_word)

        output_array = [["" for i in range(5)] for j in range(6)]
        alphabet_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',  'm', 'n', 'o', 'p', 'q',
                          'r', 's',
                          't', 'u', 'v', 'w', 'x', 'y', 'z']

        playing = True

        while playing:

            word_len = False
            print("\n------------------------\n")
            for row in output_array:
                print(row)

            for i in alphabet_array:
                print(i + " ", end="")

           # print(correct_word)

            guess = input("type your guess: ")
          #  if not guess + "\n" in words:



            if guess == correct_word:
                print("\n\n\n-------------------")
                print("\nYou win!\n")
                print("-------------------\n\n\n")

                break

            if guess == "adieu":
                print("----------------------------------------------------------------------")
                input(
                    "\n|Hello Lyndey. did you think I didnt know your starting word? how cute...\n hehe love you "
                    "press anything to continue")
                print("----------------------------------------------------------------------")

            guess_array = list(guess)
            for letter in guess_array:
                if letter not in correct_array and letter in alphabet_array:
                    alphabet_array.remove(letter)

            if len(guess) == 5:
                word_len = True
            if len(guess) != 5:
                print("\n!!!!---Word must be 5 letters long---!!!!")
                input("Press enter to continue:")
            while word_len:
                print("\n" + compare_strings(guess, correct_word))
                turn += 1

                output_array[turn - 1][0] += guess[0]
                output_array[turn - 1][1] += guess[1]
                output_array[turn - 1][2] += guess[2]
                output_array[turn - 1][3] += guess[3]
                output_array[turn - 1][4] += guess[4]

                word_len = False
            if turn == 6:
                print("\n\n")
                for row in output_array:
                    print(row)
                print("\n\n\n--------------------------")
                print("\nYou did not guess the Word\n")
                print("--------------------------\n\n\n")
                print(correct_word)

                break



