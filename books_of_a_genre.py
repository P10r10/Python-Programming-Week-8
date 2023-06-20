from book import Book


def books_of_genre(books: list[Book], genre: str) -> list[Book]:
    return [book for book in books if book.genre == genre]


if __name__ == "__main__":
    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
    norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

    books = [
        python, everest, norma,
        Book("The Snowman", "Jo Nesbo", "crime", 2007),
    ]

    print("Books in the crime genre:")
    for book in books_of_genre(books, "crime"):
        print(f"{book.author}: {book.name}")
