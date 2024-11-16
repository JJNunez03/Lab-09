
from flights import Flights




def main():
    filename = "flights.json"
    flight_schedule = Flights(filename)




    while True:
        print("\n*** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU ***")
        print("1. Add flight")
        print("2. Print flight schedule")
        print("3. Set flight schedule filename")
        print("9. Exit the program")




        choice = input("\nEnter menu choice: ")
       
        if choice == "1":
            origin = input("Enter origin: ")
            destination = input("Enter destination: ")
            flight_number = input("Enter flight number: ")
            departure = input("Enter departure time (HHMM): ")
            arrival = input("Enter arrival time (HHMM): ")
            next_day = input("Is arrival next day (Y/N): ").upper()
            if flight_schedule.add_flight(origin, destination, flight_number, departure, next_day, arrival):
                print("Flight added successfully.")
            else:
                print("Invalid departure or arrival time format.")
       
        elif choice == "2":
            print("\n================== FLIGHT SCHEDULE ==================")
            print("Origin Destination Number Departure  Arrival Duration")
            print("====== =========== ====== ========= ======== ========")
            for flight in flight_schedule.get_flights():
                print(f"{flight['origin']:6} {flight['destination']:11} {flight['flight_number']:6} "
                      f"{flight['departure']:9} {flight['arrival']:8} {flight['duration']:7}")
       
        elif choice == "3":
            filename = input("Enter new filename: ")
            flight_schedule = Flights(filename)
            print("Flight schedule filename set.")
       
        elif choice == "9":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")




if __name__ == "__main__":
    main()

