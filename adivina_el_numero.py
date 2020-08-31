import random

def run():
    ran_number = random.randint(1, 100)
    chosen_number = int(input("Choose a number from 1 to 100: "))
    while chosen_number != ran_number:
        if chosen_number < ran_number:
            print("Look for a bigger number")
        else:
            print("Look for a lower number")
            
        chosen_number= int(input("Choose another number: "))

    print("You win!") 


if __name__ == '__main__':
    run()