def classify_books(*args, **kwargs):
    fiction_books = []
    non_fiction_books = []

    book_titles = {}
    for genre, title in args:
        book_titles[title] = genre

    for isbn, title in kwargs.items():
        genre = book_titles.get(title)
        if genre == "fiction":
            fiction_books.append((isbn, title))
        elif genre == "non_fiction":
            non_fiction_books.append((isbn, title))

    fiction_books.sort(key=lambda x: x[0])
    non_fiction_books.sort(key=lambda x: x[0], reverse=True)

    output = ""

    if fiction_books:
        output += "Fiction Books:\n"
        for isbn, title in fiction_books:
            output += f"~~~{isbn}#{title}\n"

    if non_fiction_books:
        output += "Non-Fiction Books:\n"
        for isbn, title in non_fiction_books:
            output += f"***{isbn}#{title}\n"

    return output.strip()
ssssssssssssssssssssssssssssssssssssssss