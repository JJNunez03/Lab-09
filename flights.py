import json
from datetime import datetime, timedelta


class Flights:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

        try:
            with open(filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with an empty schedule.")
        except json.JSONDecodeError:
            print(f"Error reading '{filename}'. Starting with an empty schedule.")


    def add_flight(self, origin, destination, flight_number, departure, next_day, arrival):
        try:
            dep_time = datetime.strptime(departure, "%H%M")
            arr_time = datetime.strptime(arrival, "%H%M")
        except ValueError:
            return False

        if next_day == "Y":
            arr_time += timedelta(days=1)

        duration = arr_time - dep_time
        hours, remainder = divmod(duration.seconds, 3600)
        minutes = remainder // 60
        duration_str = f"{hours}:{minutes:02d}"

        flight_data = {
            "origin": origin,
            "destination": destination,
            "flight_number": flight_number,
            "departure": dep_time.strftime("%I:%M%p").lower().lstrip('0'),
            "arrival": ("+" if next_day == "Y" else "") + arr_time.strftime("%I:%M%p").lower().lstrip('0'),
            "duration": duration_str
        }
        self.data.append(flight_data)


        try:
            with open(self.filename, 'w') as file:
                json.dump(self.data, file, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")
            return False


        return True


    def get_flights(self):
        """
        Return the flight schedule as a list of lists.
        Each list contains: [origin, destination, flight_number, departure, arrival, duration].
        """
        result = []
        for flight in self.data:
            result.append([
                flight["origin"],
                flight["destination"],
                flight["flight_number"],
                flight["departure"],
                flight["arrival"],
                flight["duration"]
            ])
        return result




