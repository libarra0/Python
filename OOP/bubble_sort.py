import random

def bubble_sort(new_list):
    n = len(new_list)

    for i in range(n):
        for j in range(0, n - i - 1):

            if new_list[j] > new_list[j + 1]: # O(n) * O(n) = O(n * n) = O(n**2)
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
    
    return new_list

def run():
    size_of_the_list = int(input("How big will the list be? "))

    new_list = [random.randint(0, 100) for i in range(size_of_the_list)]
    print(new_list)

    sorted_list = bubble_sort(new_list)
    print(sorted_list)


if __name__ == "__main__":
    run()