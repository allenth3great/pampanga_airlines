




def main():
    while True:
        print("\nWelcome to the Airline Management System!")
        print("\nWhat would you like to do?")
        print("1. Add")
        print("2. Book")
        print("3. View")
        print("4. Report")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_flight()
            elif choice == 2:
                book_flight()
            elif choice == 3:
                view_flight()
            elif choice == 4:
                report_flight()
            elif choice == 5:
                print("Thank you for using the Airline Management System!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for the choice.")    


# Run the program
if __name__ == "__main__":
    main()