import time

def factorial(n):
    answer = 1

    while n > 1:
        answer *= n
        n -= 1

    return answer

def r_factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n -1)

def run():
    n = 200000

    start = time.time()
    factorial(n)
    final = time.time()
    print(final - start)

    r_start = time.time()
    r_factorial(n)
    r_final = time.time()
    print(r_final - r_start)    


if __name__ == "__main__":
    run()