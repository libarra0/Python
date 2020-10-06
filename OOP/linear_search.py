import random

def linear_search(lin_list, objective):
    match = False

    for element in lin_list:
        if element == objective:
            match = True
            break
    
def run():
    size_of_the_list = int(input("How big will the list be? "))
    objective = int(input("What number do you want to find? "))
    
    lin_list = [random.randint(0, 100) for i in range(size_of_the_list)]

    found = linear_search(lin_list, objective)
    print(lin_list)
    print(f'The element {objective} {"is" if found else "is not"} in the list')



if __name__ == "__main__":
    run()