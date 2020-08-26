def palindrome(word):
    word = word.replace(' ', '')
    word = word.lower()
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False


def run():
    word  = input("Write a word: ")
    is_palimdrome = palindrome(word)
    if is_palimdrome == True:
        print("It is palindrome")
    else:
        print("It is not palindrome")


if __name__ ==  '__main__':
    run()
