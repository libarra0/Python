def run():
    # num_1 = int(input('Pick a integer: '))
    # num_2 = int(input('Pick another integer: '))
    
    # if num_1 > num_2:
    #     print('The first number is greater than the second')
    # elif num_1 < num_2:
    #     print('The second number is greater than the first')
    # else:
    #     print('Both numbers are equals')
    name_1 = input('What is the name of the first person? ')
    name_2 = input('What is the name of the second person? ')

    age_1 = int(input('What is the age of the first person? '))
    age_2 = int(input('What is the age of the second person? '))

    if age_1 > age_2:
        print(name_1 + ' is older than ' + name_2)
    elif age_1 < age_2:
        print(name_2 + ' is older than ' + name_1)
    else:
        print(name_1 + ' and '+ name_2 + ' have the same age')



if __name__ == '__main__':
    run()