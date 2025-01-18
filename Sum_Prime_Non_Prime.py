while True:
    number_1 = input()
    number_2 = input()
    if number_1 or number_2 is 'stop':
        break
    elif int(number_1) < 0 or int(number_2) < 0:
        print("Number is negative.")
        continue

    prime_numbers_sum = 0
    while int(number_1) % 1 == 0 and int(number_1) % int(number_1) == 0 and int(number_1 > 1):
        prime_numbers_sum +=

#проблема е че така започнат кода с проверки, ще е дълъг. Имаш две числа и всяко едно има
# по два варианта, значи четири проверки...
    print(number_1, number_2)
