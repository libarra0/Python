import random

def binary_search(bin_list, start, final, target):
    print(f'Searching {target} between {bin_list[start]} and {bin_list[final - 1]}')
    
    if start > final:
        return False
    
    means = (start + final) // 2

    if bin_list[means] == target:
        return True
    elif bin_list[means] < target:
        return binary_search(bin_list, means + 1, final, target)
    else:
        return binary_search(bin_list, start, means - 1, target)
    

def run():
    size_of_the_list = int(input("How big will the list be? "))
    target = int(input("What number do you want to find? "))
    
    bin_list = sorted([random.randint(0, 100) for i in range(size_of_the_list)])

    found = binary_search(bin_list, 0, len(bin_list), target)

    print(bin_list)
    print(f'The element {target} {"is" if found else "is not"} in the list')


if __name__ == "__main__":
    run()