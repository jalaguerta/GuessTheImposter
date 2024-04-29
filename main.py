from words import WordList

"""
In this game there are 4 players and 1 secret word. 3 players know the word, 1 doesn't. You have to guess the imposter.
"""


def main():
    randomWord = WordList().returnRandomWord("celebrities")
    print("Welcome to the game!\n")
    print (f"Your word is {randomWord}")




if __name__ == "__main__":
    main()
    
