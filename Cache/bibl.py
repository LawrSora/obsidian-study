books = []

def dob_book(title, author, year):
    books.append({'title': title, 'author': author, 'year': year})

def search_by_name(title):
    return [book for book in books if book['title'] == title]

def pokaz_all_books():
    def get_year(book):
        return book['year']
    sorted_books = sorted(books, key=get_year)
    for book in sorted_books:
        print("Название:", {book['title']}, "Автор:", {book['author']}, "Год:", {book['year']})

def remove_book(title):
    global books
    books = [book for book in books if book['title'] != title]

def count_books():
    return len(books)

def filter_by_author(author):
    return [book['title'] for book in books if book['author'] == author]

def get_oldest_and_newest():
    if not books:
        return None, None
    years = [book['year'] for book in books]
    oldest = min(years)
    newest = max(years)
    oldest_books = [book for book in books if book['year'] == oldest]
    newest_books = [book for book in books if book['year'] == newest]
    return oldest_books, newest_books

dob_book("Колобок", "Пушкин", 1000)
dob_book("Война и мир", "Толстой", 2000)
dob_book("Преступление и наказание", "Федор Достоевский", 2024)

print("Все книги:")
pokaz_all_books()

print("Поиск книги 'Колобок':")
print(search_by_name("Война и мир"))

print("Количество книг:", count_books())

print("Книги Федора Достоевского:")
print(filter_by_author("Федор Достоевский"))

oldest, newest = get_oldest_and_newest()
print("Самая старая книга:", oldest)
print("Самая новая книга:", newest)

remove_book("Колобок")
print("Количество книг после удаления:", count_books())