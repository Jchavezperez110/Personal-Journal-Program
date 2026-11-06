#LAB ACTIVITY: PERSONAL JOURNAL PROGRAM

entry_count = 0

def add_entry(entry):
    global entry_count

    try:
        with open("journal.txt", "a") as file:
            entry_count += 1
            file.write(f"Entry {entry_count}: {entry}\n")

        print("Your journal entry has been saved!")
        print("Entries saved this run:", entry_count)

    except OSError:
        print("Sorry, there was a problem saving your journal entry.")

def read_entries():
    try:
        with open("journal.txt", "r") as file:
            contents = file.read()
            print("\n--- MY JOURNAL ---")
            print(contents)

    except FileNotFoundError:
        print("Your journal is empty. Write an entry first!")

while True:
    print("\nPERSONAL JOURNAL")
    print("1. Add a journal entry")
    print("2. Read journal entries")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        entry = input("\nWhat would you like to write about today? ")
        add_entry(entry)

    elif choice == "2":
        read_entries()

    elif choice == "3":
        print("Goodbye! Thanks for using your journal.")
        break

    else:
        print("Please choose a valid option.")

