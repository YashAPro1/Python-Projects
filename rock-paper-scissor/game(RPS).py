import random
print("rock-👊","paper-🖐","scissor-✌️ ")

userwins = 0
compwins = 0
tie = 0
option = ["rock","paper","scissor","Test"]
inp = input("Do you want to play?: ")   

while inp.lower() == "yes":
    user_input = input("Type Rock/Paper/Scissor or Q to quit: ")
    if user_input.lower() == "q":
        quit()
    if user_input not in option:
        print("Enter only from Rock/Paper/Scissor")
        break
    random_num  = random.randint(0,2)
    comp_pick = option[random_num]
    print("Computer Picked",comp_pick + ".")
    
    if user_input == comp_pick:
        print("The Game tie")
        tie += 1
        continue

    elif user_input == "rock" and comp_pick == "scissor":
        print("You won!")
        userwins += 1
        print("Score ",'userwins',userwins,'compwins',compwins)
        continue
    elif user_input == "scissor" and comp_pick == "paper":
        print('You won!')
        userwins += 1
        print("Score ",'userwins',userwins,'compwins',compwins)
        continue
    elif user_input == "paper" and comp_pick == "rock":
        print("You won!")
        userwins += 1
        print("Score ",'userwins',userwins,'compwins',compwins)
        continue
    else:
        print("You lose :(")
        compwins += 1
        print("Score ",'userwins',userwins,'compwins',compwins)