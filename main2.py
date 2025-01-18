# main.py

def main():
    print("Welcome to the Airlines Management System!\n")
    
    while True:
        action = input("What would you like to do? (add/book/view/report/exit): ").lower()
        
        if action == "add":
            print("You chose to add a flight.")
            # Add flight logic here
        elif action == "book":
            print("You chose to book a flight.")
            # Book flight logic here
        elif action == "view":
            print("You chose to view flight details.")
            import view  # Assuming view.py is in the same directory
            flight_number = int(input("Enter flight number: "))
            view.view_flight_details(flight_number)
        elif action == "report":
            print("You chose to generate a report.")
            # Report generation logic here
        elif action == "exit":
            print("Exiting the Airlines Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please choose from add, book, view, report, or exit.")

if __name__ == "__main__":
    main()
