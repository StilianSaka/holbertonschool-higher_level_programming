import random

def guess_thenumber():
    target_number = random.randint(1, 100)
    attempt_number = 0
    imput_nr = 0
    while target_number != imput_nr:
        imput_nr = int(input("Please enter your number: "))
        attempt_number += 1
        if imput_nr > target_number:
            print("My number is lower than your number")
        if imput_nr < target_number:
            print("My number is higher than your number")
    if attempt_number <= 7:
        print("Congratulations you are quite logical or just lucky")
    elif 7 < attempt_number < 100:
        print("Try better next time!")
    else:
        print("Rrembe bastunin dhe ik behu coban se nuk je per kete pune")
    
   
   
guess_thenumber()