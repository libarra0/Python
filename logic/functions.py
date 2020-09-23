def enumeration(objective):
    answer = 0

    while answer**2 < objective:
        print(answer)
        answer += 1

    if answer**2 == objective:
        print(f"The square root of {objective} is {answer}")
    else:
        print(f"{objective} does not have an exact square root")

def approximation(objective, epsilon):
    step = epsilon**2
    answer = 0.0
        
    while abs(answer**2 - objective) >= epsilon and answer <= objective:
        print(abs(answer**2 - objective), answer)
        answer += step
            
    if abs(answer**2 - objective) >= epsilon:
        print(f"The square root of {objective} was not found")
    else:
        print(f"The square root of {objective} is {answer}")

def binary_search(objective, epsilon):
    floor = 0.0
    ceil = max(1.0, objective)
    answer = (ceil + floor) / 2

    while abs(answer**2 - objective) >= epsilon:
        print(f"floor = {floor}, ceil = {ceil}, answer = {answer}")
        if answer**2 < objective:
            floor = answer
        else:
            ceil = answer
        
        answer  = (ceil + floor) / 2
    
    print(f"The square root of {objective} is {answer}")

def main_menu():
    target = True

    while target:
        print("""Choose one of the following options: 
        1.- Enumeration
        2.- Approximation
        3.- Binary Search
        4.- Exit
        """)
        
        menu_option = input("Choose the correct value: ")

        if menu_option == "1":
            objective = int(input("Choose an integer: "))
            enumeration(objective)
        elif menu_option == "2":
            objective = int(input("Choose an integer: "))
            epsilon = float(input("Choose a float value for epsilon:"))
            approximation(objective, epsilon)
        elif menu_option == "3":
            objective = int(input("Choose an integer: "))
            epsilon = float(input("Choose a float value for epsilon:"))
            binary_search(objective, epsilon)
        elif menu_option == "4":
            print("Goodbye!")
            break
        elif menu_option == "":
            print("Choose the correct value \n")
        else:
            print("Choose the correct value \n")




def run():
    main_menu()


if __name__ == "__main__":
    run()