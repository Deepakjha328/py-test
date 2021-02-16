import random

def run_guess(guess,answer):
    if 0<guess<11:
        if guess == answer:
            print("You are genious")
            return True
    else:
        print("Wrong Guess! try agian")
        return False

answer = random.randint(1, 10)
if __name__ =='__main__':
    while True:
        try:
            guess = int(input("Guess a number 1~10: "))
            if run_guess(guess, answer):
                break
        except ValueError:
            print("Please enter a right input")
            continue


