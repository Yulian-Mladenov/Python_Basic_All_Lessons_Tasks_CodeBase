open_browser_tabs = int(input())
salary = int(input())

Facebook = 150
Instagram = 100
Reddit = 50
Penalty = salary

for website_number in range(1, open_browser_tabs + 1):
    website_name = input()
    if website_name == 'Facebook':
        Penalty -= Facebook
    elif website_name == 'Instagram':
        Penalty -= Instagram
    elif website_name == 'Reddit':
        Penalty -= Reddit
    if Penalty <= 0:
        print("You have lost your salary.")
        break
else:
    print(Penalty)
