guessword = input("Give us a word!")
guessword = guessword.lower()
i=0
hangman=[]
while i<len(guessword):
    hangman.append('_')
    i+=1
j=0
while j<6:
    guessletter = input("Guess the letter.")
    if guessletter in guessword:
        indexguessletter = guessword.index(guessletter)
        hangman[indexguessletter] = guessletter
        print(hangman)
    else:
        print("Incorrect.")
    j +=1
print("Game over.")
