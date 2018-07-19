from random import randint
i = 0
num = randint(0, 20)
for i in range(3):
    print(i)
    i += 1
    answer = input("Pick a number")

    if (int(answer) == num):
        print("Congrats!")
        break
    elif (int(answer) > num):
        print("Guess lower.")
    elif (int(answer) < num):
        print("Guess higher.")
