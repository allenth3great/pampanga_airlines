def view_flight_details():
    flight_number = int(input("Enter flight number: "))
    flight = flights.get(flight_number)
    
    if flight:
        print("Flight Details:")
        print(f"- Destination: {flight['destination']}")
        print(f"- Available Seats: {flight['available_seats']}")
        print("- Passengers:")
        if flight['passengers']:
            for i, passenger in enumerate(flight['passengers'], start=1):
                print(f"  {i}. {passenger['name']} (Seat: {passenger['seat']})")
        else:
            print("  No passengers booked.")
    else:
        print("Flight not found.")

if __name__ == "__main__":
    view_flight_details()
