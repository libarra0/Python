def run():
    objective = int(input("Choose an integer: "))
    answer = 0

    while answer**2 < objective:
        print(answer)
        answer += 1

    if answer**2 == objective:
        print(f"The square root of {objective} is {answer}")
    else:
        print(f"{objective} does not have an exact square root")


if __name__ == "__main__":
    run()