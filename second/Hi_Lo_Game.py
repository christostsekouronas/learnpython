low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Pres ENTER to start")    #we have written this in order to let the computer WAIT until the user press the ENTER (so the input is ENTER)

guess = 1
while True:
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? Enter h or l, or c if my guess is correct".format(guess).casefold())


    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess.
        pass
    elif high_low == "l":
        # Guess lower. The high end of the range becomes one less than the guess.
        pass
    elif high_low == "c":
        print("I got it in {} guess!".format(guess))

    else:
        print("Please enter h, l or c")