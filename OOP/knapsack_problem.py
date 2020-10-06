iteration = 0

def backpack(backpack_size, weights, values, n):
    global iteration

    iteration +=1
    print(f'Iterations {iteration} trying with n = {n}')

    if n == 0 or backpack_size == 0:
        return 0
    
    if weights[n - 1] > backpack_size:
        return backpack(backpack_size, weights, values, n -1)

    return max(values[n - 1] + backpack(backpack_size - weights[n - 1], weights, values, n-1), 
    backpack(backpack_size, weights, values, n -1))

def run():
    values = [60, 100, 120]
    weights = [10, 20, 30]
    backpack_size = 50
    n = len(values)

    result = backpack(backpack_size, weights, values, n)
    print(result)
    print(f'With a knapsack that can carry only {backpack_size} kg you can only add elements equivalents to ${result} \n\t {backpack_size} kg can carry ${result}')

    print()
    print(f'Total iterations =  {iteration}')


if __name__ == "__main__":
    run()