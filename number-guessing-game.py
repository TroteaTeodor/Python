import random

print("Enter a number range :")
range_min = input()
range_max = input()

number = random.randint(int(range_min),int(range_max))
print(number)
print("Guess a number between %s-%s :" % (range_min, range_max))
ok = True
while ok:
    intput1 = int(input())
    if intput1 < number:
        print("The number is higher! Try again: ")
    elif intput1 > number:
        print("The number is lower! Try again: ")
    else:
        print("You guessed the number corectly!")
        ok = False