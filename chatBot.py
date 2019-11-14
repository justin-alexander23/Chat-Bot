import random
import time

print("Hello. I am a computer. What is your name? ")
name = input()
print("Hello " + name + ". It's nice to meet you. What is your favorite color")
fav_color = input()
if fav_color == "Blue" or fav_color=="blue":
    print("Wow blue is my favorite color too!")
else:
    print("I hate " + fav_color + ". My favorite color is Blue.")
print("Do you want to play a game?")
response = input()
if response == "Yes" or response =="yes":
    print("I am thinking of a number between 1 and 3. Guess what it is.")
    number = str(random.randint(1, 3))
    guess_1 = input()
    if guess_1 == number:
        print("Wow. You got it right. Good job.")
        print("Do you want to know what time it is?")
        response = input()

        if response == "Yes" or response == "yes" or response == "sure" or response == "Sure" or response == "okay" or response == "Okay":
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            print("The time is" + current_time)
            print("Goodbye")
        else:
            print("Okay. Goodbye.")

    elif guess_1 != number:
        print("That's not my number. Try again.")
    guess_2=input()
    if guess_2 == number:
        print("Wow. You got it right. Good job.")
        print("Do you want to know what time it is?")
        response = input()

        if response == "Yes" or response == "yes" or response == "sure" or response == "Sure" or response == "okay" or response == "Okay":
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            print("The time is" + current_time)
            print("Goodbye")
        else:
            print("Okay. Goodbye.")

    elif guess_2 != number: print("That's not my number. Try again.")
    guess_3=input()
    if guess_3 == number:
        print("Wow. You got it right. Good job.")
        print("Do you want to know what time it is?")
        response = input()

        if response == "Yes" or response == "yes" or response == "sure" or response == "Sure" or response == "okay" or response == "Okay":
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            print("The time is" + current_time)
            print("Goodbye")
        else:
            print("Okay. Goodbye.")

    elif guess_3 != number: print("That's not my number. Try again.")

else:
    print("Okay. Goodbye")
















