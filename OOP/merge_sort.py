import random

def merge_sort(new_list):
    if len(new_list) > 1:
        means = len(new_list) // 2
        left = new_list[:means]
        right = new_list[means:]
        print(left, '*' * 5, right)

        # Recursive calling in each half
        merge_sort(left)
        merge_sort(right)

        # Iterators to cycle through two sublists
        i = 0
        j = 0
        #Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                new_list[k] = left[i]
                i += 1
            else:
                new_list[k] = right[j]
                j += 1
            
            k += 1

        while i < len(left):
            new_list[k] = left[i]
            i +=1
            k +=1

        while j < len(right):
            new_list[k] = right[j]
            j += 1
            k += 1

        print(f'Left  {left}, Rigth {right} ')
        print(new_list)
        print('-' * 50)

    return new_list


def run():
    size_of_the_list = int(input("How big will the list be? "))

    new_list = [random.randint(0, 100) for i in range(size_of_the_list)]
    print(new_list)
    print('-' * 20)

    sorted_list = merge_sort(new_list)
    print(sorted_list)


if __name__ == "__main__":
    run()