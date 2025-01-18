flight = {}

def add_flight():
    try:
        flight_num = int(input("Enter flight number: "))
        if flight_num < 0:
            print("Flight num cannot be negative")
            return
        destination =  input("Enter destination: ")
        seat_cap = int(input("Enter seat capacity: "))

        flight[flight_num] = {"Destination": destination, "Seat Capacity": seat_cap}
        print("Flight added successfully!")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the flight number.")

add_flight()
