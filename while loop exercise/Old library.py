# target_book = input()
# counter = 0
#
# while True:
#     searching = input()
#     counter += 1
#     if searching == target_book:
#         print(f"You checked {counter - 1} books and found it.")
#         break
#     if searching == "No More Books":
#         print("The book you search is not here!")
#         print(f"You checked {counter - 1} books.")
#         break
#
#
target_book = input()
searching = input()
counter = 0

while target_book != searching and searching != "No More Books":
    counter += 1
    searching = input()
    if searching == target_book:
        print(f"You checked {counter} books and found it.")
        break
    if searching == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {counter} books.")
        break


