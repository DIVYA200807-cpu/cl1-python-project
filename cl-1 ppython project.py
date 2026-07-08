print("==== MY LIBRARY BOOK ORGANISER ====")
books = ["python basic", "data science", "AI",
         "fundamentals", "web development"]

print("\nOriginal Book List:")
print(books)

books.append("machine learning")
print("\nafter adding a book:")
print(books)

books.remove("data science")
print("\nAfter Removing a Book:")
print(books)


print("\nTotal Number of Books:", len(books))


print("\nFirst Book:", books[0])


print("First Three Books:", books[:3])


books.sort()
print("\nBooks in Sorted Order:")
print(books)


books.reverse()
print("\nBooks in Reverse Order:")
print(books)


librarian = {
    "Name": "Divya",
    "Library": "City Library",
    "Experience": 3
}

print("\nLibrarian Details:")
print(librarian)


print("Librarian Name:", librarian["Name"])


librarian["Experience"] = 4


librarian["City"] = "Delhi"


del librarian["Library"]

print("\nUpdated Librarian Details:")
print(librarian)


book_ids = [101, 102, 103, 104]
book_names = books

book_directory = dict(zip(book_ids, book_names))

print("\nBook Directory:")
print(book_directory)


print("\n===== FINAL SUMMARY =====")
print("Books:", books)
print("Number of Books:", len(books))
print("Librarian Information:", librarian)
print("Book Directory:", book_directory)
print("\nProject Completed Successfully!")
