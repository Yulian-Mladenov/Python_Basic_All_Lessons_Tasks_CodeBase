# This is first approach, very basic
# word = input()
#
# while word != 'Stop':
#     print(word)
#     word = input()

# Second approach
# word = input('Please write here your word: ')
#
# while word != 'Stop':
#     print('Not match, please try again')
#     word = input('Please write your next try here: ')
# else:
#     print(f'Successful access with word: {word}')

# Third approach - this approach is working, but is printing two times message to read data.
# while True:
#     word = input('Please write here your word: ')
#     if word != "Stop":
#         print('Not match, please try again')
#         word = input('Please write here your next try: ')
#     else:
#         print(f'Successful access with word: {word}')
#         break


# Fourth approach - this approach is working, but is printing two times message to read data
# while True:
#     word = input('Please write here your word: ')
#     if word == "Stop":
#         print(f'Successful access with word: {word}')
#         break
#     else:
#         word = input('Not match, please write here your next try: ')


# Fifth approach - is working but is very basic.
# while True:
#     word = input()
#     if word == 'Stop':
#         print(word)
#         break


# Sixth approach - a bit better than previous
# while True:
#     word = input('Please write here your word: ')
#     if word == "Stop":
#         print(f'Successful access with word: {word}')
#         break

# Seventh approach - the shortest and functional
# while True:
#     word = input('Please write here your word: ')
#     if word == "Stop":
#         print(f'Successful access with word: {word}')
#         break
#     else:
#         print('Not match, please write here your next try on the next line')
