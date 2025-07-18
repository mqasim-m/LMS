import os

DATA_FILE = "library_members.txt"

if not os.path.exists(DATA_FILE):
    open(DATA_FILE, 'w').close()

def register_member(member_id, name, email, phone):
    with open(DATA_FILE, 'a') as file:
        line = f"{member_id}-{name}-{email}-{phone}\n"
        file.write(line)
    print(f"\n✅ Member '{name}' registered successfully.\n")


def remove_member(member_id):
    found = False
    with open(DATA_FILE, 'r') as file:
        lines = file.readlines()

    with open(DATA_FILE, 'w') as file:
        for line in lines:
            if not line.strip().startswith(member_id + '-'):
                file.write(line)
            else:
                found = True

    if found:
        print(f"\n🗑️ Member ID '{member_id}' removed.\n")
    else:
        print(f"\n❌ Member ID '{member_id}' not found.\n")


def update_member_info(member_id, field, new_value):
    updated = False
    fields = ['member_id', 'name', 'email', 'phone']
    if field not in fields:
        print(f"\n❌ Invalid field. Choose from {fields[1:]}\n")
        return

    with open(DATA_FILE, 'r') as file:
        lines = file.readlines()

    with open(DATA_FILE, 'w') as file:
        for line in lines:
            line = line.strip()
            parts = line.split('-')
            if parts[0] == member_id:
                index = fields.index(field)
                parts[index] = new_value
                file.write('-'.join(parts) + '\n')
                updated = True
            else:
                file.write(line + '\n')

    if updated:
        print(f"\n✅ Member ID '{member_id}' updated successfully.\n")
    else:
        print(f"\n❌ Member ID '{member_id}' not found.\n")


def display_member_details(member_id):
    with open(DATA_FILE, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith(member_id + '-'):
                parts = line.split('-')
                print("\n📋 Member Details:")
                print(f"ID    : {parts[0]}")
                print(f"Name  : {parts[1]}")
                print(f"Email : {parts[2]}")
                print(f"Phone : {parts[3]}\n")
                return
    print(f"\n❌ Member ID '{member_id}' not found.\n")


# Interactive Menu
while True:
    print("📚 Library User Management System")
    print("1. Register Member")
    print("2. Remove Member")
    print("3. Update Member Info")
    print("4. Display Member Details")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        member_id = input("Enter Member ID: ")
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone: ")
        register_member(member_id, name, email, phone)

    elif choice == '2':
        member_id = input("Enter Member ID to remove: ")
        remove_member(member_id)

    elif choice == '3':
        member_id = input("Enter Member ID to update: ")
        field = input("Which field to update? (name/email/phone): ").lower()
        new_value = input(f"Enter new value for {field}: ")
        update_member_info(member_id, field, new_value)

    elif choice == '4':
        member_id = input("Enter Member ID to view: ")
        display_member_details(member_id)

    elif choice == '5':
        print("\n👋 Exiting. Goodbye!")
        break

    else:
        print("\n❌ Invalid choice. Please enter 1-5.\n")
