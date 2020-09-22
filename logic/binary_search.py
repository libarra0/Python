def run():
    objective = int(input("Choose an integer: "))
    epsilon = 0.001
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



if __name__ == "__main__":
    run()