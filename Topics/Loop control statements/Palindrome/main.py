user_input = input()

for i in range(len(user_input) // 2):

    if user_input[i] != user_input[-(i + 1)]:
        print('Not palindrome')
        break
    elif i == len(user_input) // 2 - 1:
        print('Palindrome')
