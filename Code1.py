import os

BOOK_FILE = "library_books.txt"

# Create the file if it doesn't exist
if not os.path.exists(BOOK_FILE):
    open(BOOK_FILE, 'w').close()


def add_book(book_id, title, author, isbn, quantity):
    with open(BOOK_FILE, 'r') as file:
        for line in file:
            if line.strip().startswith(book_id + '-'):
                print(f"\n⚠️ Book ID '{book_id}' already exists.\n")
                return

    with open(BOOK_FILE, 'a') as file:
        line = f"{book_id}-{title}-{author}-{isbn}-{quantity}\n"
        file.write(line)
    print(f"\n✅ Book '{title}' added to catalog.\n")


def remove_book(book_id):
    removed = False
    with open(BOOK_FILE, 'r') as file:
        lines = file.readlines()

    with open(BOOK_FILE, 'w') as file:
        for line in lines:
            if not line.strip().startswith(book_id + '-'):
                file.write(line)
            else:
                removed = True

    if removed:
        print(f"\n🗑️ Book ID '{book_id}' removed from catalog.\n")
    else:
        print(f"\n❌ Book ID '{book_id}' not found.\n")


def update_book_quantity(book_id, new_quantity):
    updated = False

    with open(BOOK_FILE, 'r') as file:
        lines = file.readlines()

    with open(BOOK_FILE, 'w') as file:
        for line in lines:
            parts = line.strip().split('-')
            if parts[0] == book_id:
                parts[4] = str(new_quantity)
                file.write('-'.join(parts) + '\n')
                updated = True
            else:
                file.write(line)

    if updated:
        print(f"\n✅ Quantity updated for Book ID '{book_id}'.\n")
    else:
        print(f"\n❌ Book ID '{book_id}' not found.\n")


def display_all_books():
    print("\n📚 All Books in Library Catalog:\n")
    with open(BOOK_FILE, 'r') as file:
        lines = file.readlines()
        if not lines:
            print("No books found.")
            return
        for line in lines:
            book_id, title, author, isbn, quantity = line.strip().split('-')
            print(f"ID: {book_id} | Title: {title} | Author: {author} | ISBN: {isbn} | Quantity: {quantity}")
    print()


# 🧭 Menu Interface
while True:
    print("\n📘 Library Book Management")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Update Book Quantity")
    print("4. Display All Books")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == '1':
        book_id = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        isbn = input("Enter ISBN: ")
        quantity = input("Enter Quantity: ")
        add_book(book_id, title, author, isbn, quantity)

    elif choice == '2':
        book_id = input("Enter Book ID to remove: ")
        remove_book(book_id)

    elif choice == '3':
        book_id = input("Enter Book ID to update quantity: ")
        new_quantity = input("Enter new quantity: ")
        update_book_quantity(book_id, new_quantity)

    elif choice == '4':
        display_all_books()

    elif choice == '5':
        print("\n👋 Exiting Book Management. Goodbye!")
        break

    else:
        print("\n❌ Invalid choice. Please enter 1-5.\n")
