class Flight:
    def __init__(self, p_id, process, start_time, priority):
        self.p_id = p_id
        self.process = process
        self.start_time = start_time
        self.priority = priority

    def __str__(self):
        return f"{self.p_id} {self.process} {self.start_time} {self.priority}"

class FlightTable:
    def __init__(self, flights):
        self.flights = flights

    def sort_by_p_id(self):
        self.flights.sort(key=lambda flight: flight.p_id)

    def sort_by_start_time(self):
        self.flights.sort(key=lambda flight: flight.start_time)

    def sort_by_priority(self):
        self.flights.sort(key=lambda flight: flight.priority)

    def print_table(self):
        print("P_ID | Process | Start Time | Priority")
        print("-" * 30)
        for flight in self.flights:
            print(flight)

def main():
    flights = [
        Flight(P1, VSCode, 100, MID),
        Flight(P23, Eclipse, 234, MID),
        Flight(P93, Chrome, 189, High),
        Flight(P42, JDK, 9, High),
        Flight(P9, CMD, 7, High),
        Flight(P87, NotePad, 23, Low)
    ]

    flight_table = FlightTable(flights)

    # Get user input for the sorting parameter
    while True:
        print("Choose the sorting parameter:")
        print("1. Sort by P_ID")
        print("2. Sort by Start Time")
        print("3. Sort by Priority")

        sorting_parameter = int(input("Enter your choice: "))

        if sorting_parameter in range(1, 4):
            break
        else:
            print("Invalid choice. Please try again.")

    # Sort the flight table based on the user's choice
    if sorting_parameter == 1:
        flight_table.sort_by_p_id()
    elif sorting_parameter == 2:
        flight_table.sort_by_start_time()
    elif sorting_parameter == 3:
        flight_table.sort_by_priority()

    # Print the sorted flight table
    flight_table.print_table()

if __name__ == "__main__":
    main()
