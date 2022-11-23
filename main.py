import random
n = random.randrange(1, 10)
guess = int(input(" guess a number between 1 and 10, Enter any number: "))
while n != guess:
    if guess < n:
        print("Too low almost there")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Wooh there you went a bit too high")
        guess = int(input("Enter number again: "))
    else:
        break
print("congratulations you did it!!")
