import os
from datetime import datetime, timedelta

# File paths (make sure these exist and have correct format)
BOOK_FILE = "library_books.txt"
MEMBER_FILE = "library_members.txt"
BORROW_FILE = "borrowed_books.txt"

# Ensure borrow file exists
if not os.path.exists(BORROW_FILE):
    open(BORROW_FILE, 'w').close()

# 📘 Utility Functions
def book_exists(book_id):
    with open(BOOK_FILE, 'r') as file:
        return any(line.strip().startswith(book_id + '-') for line in file)

def member_exists(member_id):
    with open(MEMBER_FILE, 'r') as file:
        return any(line.strip().startswith(member_id + '-') for line in file)

def update_book_quantity(book_id, delta):
    lines = []
    updated = False

    with open(BOOK_FILE, 'r') as file:
        lines = file.readlines()

    with open(BOOK_FILE, 'w') as file:
        for line in lines:
            parts = line.strip().split('-')
            if parts[0] == book_id:
                quantity = int(parts[4]) + delta
                if quantity < 0:
                    print("\n❌ Not enough copies available.\n")
                    return False
                parts[4] = str(quantity)
                file.write('-'.join(parts) + '\n')
                updated = True
            else:
                file.write(line)

    return updated


# ✅ Borrow Book
def borrow_book(book_id, member_id, loan_days=14):
    if not book_exists(book_id):
        print(f"\n❌ Book '{book_id}' not found.")
        return
    if not member_exists(member_id):
        print(f"\n❌ Member '{member_id}' not found.")
        return
    if not update_book_quantity(book_id, -1):
        return

    borrow_date = datetime.today().strftime('%Y-%m-%d')
    due_date = calculate_due_date(borrow_date, loan_days)

    with open(BORROW_FILE, 'a') as file:
        file.write(f"{book_id}-{member_id}-{borrow_date}-{due_date}-borrowed\n")

    print(f"\n✅ Book '{book_id}' borrowed by Member '{member_id}'. Due on {due_date}.\n")


# 🔁 Return Book
def return_book(book_id, member_id):
    found = False
    lines = []

    with open(BORROW_FILE, 'r') as file:
        lines = file.readlines()

    with open(BORROW_FILE, 'w') as file:
        for line in lines:
            parts = line.strip().split('-')
            if parts[0] == book_id and parts[1] == member_id and parts[4] == 'borrowed':
                parts[4] = 'returned'
                file.write('-'.join(parts) + '\n')
                update_book_quantity(book_id, 1)
                found = True
            else:
                file.write(line)

    if found:
        print(f"\n✅ Book '{book_id}' returned by Member '{member_id}'.\n")
    else:
        print(f"\n❌ No active borrow record found.\n")


# 🗓️ Due Date Calculator
def calculate_due_date(borrow_date, loan_period_days):
    borrow_dt = datetime.strptime(borrow_date, '%Y-%m-%d')
    due_dt = borrow_dt + timedelta(days=loan_period_days)
    return due_dt.strftime('%Y-%m-%d')


# ⏰ Overdue Checker
def check_overdue_books():
    today = datetime.today()
    print("\n📋 Overdue Books:\n")
    found = False

    with open(BORROW_FILE, 'r') as file:
        for line in file:
            book_id, member_id, borrow_date, due_date, status = line.strip().split('-')
            if status == 'borrowed':
                due_dt = datetime.strptime(due_date, '%Y-%m-%d')
                if due_dt < today:
                    days_overdue = (today - due_dt).days
                    print(f"Book ID: {book_id} | Member ID: {member_id} | Due: {due_date} | Overdue by {days_overdue} days")
                    found = True

    if not found:
        print("✅ No overdue books.\n")
