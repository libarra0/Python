def run():
    objective = int(input("Choose an integer: "))
    epsilon = 0.0001
    step = epsilon**2
    answer = 0.0

    while abs(answer**2 - objective) >= epsilon and answer <= objective:
        print(abs(answer**2 - objective), answer)
        answer += step

    if abs(answer**2 - objective) >= epsilon:
        print(f"The square root of {objective} was not found")
    else:
        print(f"The square root of {objective} is {answer}")


if __name__ == "__main__":
    run()