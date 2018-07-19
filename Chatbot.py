# --- Define functions ---
def hangman():
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
            print(hangman, "\n")
        else:
            print("Incorrect.\n")
        j +=1
    print("Game over.\n")

def joke():
    firstjoke = input("\nCan bees fly in the rain?")
    print("Not without their yellow jackets.\n")

def haiku():
    import random
    first = ["An old silent pond...", "Autumn moonlight—", "In the twilight rain"]
    x = random.choice(first)
    second = ["A frog jumps into the pond,", "a worm digs silently", "these brilliant-hued hibiscus —"]
    y = random.choice(second)
    third = ["splash! Silence again.", "into the chestnut.", "A lovely sunset."]
    z = random.choice(third)
    print("\n" +x + '\n' + y + '\n' + z +"\n")

def guessthenumber():
    from random import randint
    i = 0
    num = randint(0, 20)
    for i in range(3):
        i += 1
        answer = input("\nPick a number")
        if (int(answer) == num):
            print("Congrats!\n")
            break
        elif (int(answer) > num):
            print("Guess lower.\n")
        elif (int(answer) < num):
            print("Guess higher.\n")
    print("The number was ",num,"\n")
def sum(num1, num2):
    return num1+num2

def diff(num1, num2):
    return num1-num2

def prod(num1, num2):
    return num1*num2

def quo(num1,num2):
    return num1/num2

def rpsgame():
    import random
    rps = ["rock", "paper", "scissors"]
    x = random.choice(rps)
    user = input("Rock, Paper, or Scissors?")
    if (user == "rock"):
        if (x == "rock"):
            print("\nThe computer picked rock. Draw!\n")
        elif (x == "paper"):
            print("\nThe computer picked paper. Computer wins!\n")
        elif (x == "scissors"):
            print("\nThe computer picked scissors. You win!\n")
        else:
            user = input("Rock, Paper, or Scissors?")
    elif (user == "paper"):
        if (x == "rock"):
            print("\nThe computer picked rock. You win!\n")
        elif (x == "paper"):
            print("\nThe computer picked paper. Draw!\n")
        elif (x == "scissors"):
            print("\nThe computer picked scissors. Computer wins!\n")
        else:
            user = input("Rock, Paper, or Scissors?")
    elif (user == "scissors"):
        if (x == "rock"):
            print("\nThe computer picked rock. Computer Wins\n!")
        elif (x == "paper"):
            print("\nThe computer picked paper. You win!\n")
        elif (x == "scissors"):
            print("\nThe computer picked scissors. Draw!\n")
        else:
            user = input("Rock, Paper, or Scissors?")
    else:
        user = input("Rock, Paper, or Scissors?")

def circle(rad):
    return 3.14*rad*rad

def triangle(num1,num2):
    return .5*num1*num2

def trap(base1,base2,height):
    return .5*base1*base2*height

# --- Main program ---
def main():
    greeting = ["hi", "hello", "what's up", "Hi", "Hello"]
    answer = input("Hello! I am a chatbot.")
    if (answer in greeting):
        print("What would you like to do?")
    else:
        print("This is a default response.")
    while True:
        game = input(" Press 1 to play hangman \n Press 2 to hear a joke \n Press 3 for a Haiku \n Press 4 to play guess the number \n Press 5 for a calculator \n Press 6 for area calculator \n Press 7 for rock, paper, scissors \n Press 8 to exit \n")
        if (game == "1"):
            hangman()
        elif (game == "2"):
            joke()
        elif (game == "3"):
            haiku()
        elif (game == "4"):
            guessthenumber()
        elif (game == "5"):
            while True:
                calculator = input("\n Press 1 to add two numbers \n Press 2 to subtract two numbers \n Press 3 to multiply two numbers \n Press 4 to divide two numbers \n Press 5 to exit \n")
                if (calculator == "1"):
                    num1 = input("Enter first number: ")
                    num2 = input("Enter second number: ")
                    result = sum(int(num1),int(num2))
                    print("Sum = ",result)
                elif (calculator == "2"):
                    num1 = input("Enter first number: ")
                    num2 = input("Enter second number: ")
                    result = diff(int(num1),int(num2))
                    print("Difference = ",result)
                elif (calculator == "3"):
                    num1 = input("Enter first number: ")
                    num2 = input("Enter second number: ")
                    result = prod(int(num1),int(num2))
                    print("Product = ",result)
                elif (calculator == "4"):
                    num1 = input("Enter first number: ")
                    num2 = input("Enter second number: ")
                    result = quo(int(num1),int(num2))
                    print("Quotient = ",result)
                elif (calculator == "5"):
                    break
                else:
                    calculator = input("\n Press 1 to add two numbers \n Press 2 to subtract two numbers \n Press 3 to multiply two numbers \n Press 4 to divide two numbers \n Press 5 to exit \n")
        elif (game == "6"):
            while True:
                areacalc = input("\n Press 1 to calculate the area of a square \n Press 2 to calculate the area of a circle \n Press 3 to calculate the area of a parallelogram \n Press 4 to calculate the area of a triangle \n Press 5 to calculate the area of a trapezoid \n Press 6 to exit \n")
                if (areacalc == "1"):
                    len = input("Enter length: ")
                    result = prod(int(len),int(len))
                    print("Area = ",result)
                elif (areacalc == "2"):
                    rad = input("Enter radius: ")
                    result = circle(int(rad))
                    print("Area = ",result)
                elif (areacalc == "3"):
                    num1 = input("Enter length: ")
                    num2 = input("Enter width: ")
                    result = prod(int(num1),int(num2))
                    print("Area = ",result)
                elif (areacalc == "4"):
                    num1 = input("Enter base: ")
                    num2 = input("Enter height: ")
                    result = triangle(int(num1),int(num2))
                    print("Area = ",result)
                elif (areacalc == "5"):
                    base1 = input("Enter base 1: ")
                    base2 = input("Enter base 2: ")
                    height = input("Enter height: ")
                    result = trap(int(base1),int(base2),int(height))
                    print("Area = ",result)
                elif (areacalc == "6"):
                    break
                else:
                    areacalc = input("\n Press 1 to calculate the area of a square \n Press 2 to calculate the area of a circle \n Press 3 to calculate the area of a parallelogram \n Press 4 to calculate the area of a triangle \n Press 5 to calculate the area of a trapezoid \n Press 6 to exit \n")
        elif (game == "7"):
            rpsgame()
        elif (game == "8"):
            break
        else:
            game = input(" Press 1 to play hangman \n Press 2 to hear a joke \n Press 3 for a Haiku \n Press 4 to play guess the number \n Press 5 for a calculator \n Press 6 to exit \n")

# Setup code that runs main() function.
if __name__ == "__main__":
  main()
