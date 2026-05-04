amount = round(float(input()) * 100)
coins = 0

coins += amount // 200  # монети от 2лв
amount %= 200

coins += amount // 100  # монети от 1лв
amount %= 100

coins += amount // 50  # монети от 0,50лв
amount %= 50

coins += amount // 20  # монети от 0,20лв
amount %= 20

coins += amount // 10  # монети от 0,10лв
amount %= 10

coins += amount // 5  # монети от 0,05лв
amount %= 5

coins += amount // 2  # монети от 0,02лв
amount %= 2

coins += amount // 1  # монети от 0,01лв
amount %= 1

print(coins)