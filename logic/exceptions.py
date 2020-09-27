def divide_elements_of_the_list(my_list, my_divider):
    try:
        return[i / my_divider for i in my_list]
    except ZeroDivisionError as e:
        print(e)
        return my_list


def run():
    my_list = list(range(10))
    my_divider = 0

    print(divide_elements_of_the_list(my_list, my_divider))


if __name__ == "__main__":
    run()