import datetime

class Destination:
    def __init__(self, name, attractions):
        self.name = name
        self.attractions = attractions

    def add_attraction(self, attraction):
        if attraction not in self.attractions:
            self.attractions.append(attraction)

    def remove_attraction(self, attraction):
        if attraction in self.attractions:
            self.attractions.remove(attraction)

    def list_attractions(self):
        return self.attractions

    def update_attractions(self, attractions):
        self.attractions = attractions

    def get_destination_details(self):
        return {
            'Name': self.name,
            'Attractions': self.attractions
        }

class Accommodation:
    def __init__(self, name, location, room_types, availability):
        self.name = name
        self.location = location
        self.room_types = room_types
        self.availability = availability

    def book_room(self, room_type, start_date, end_date):
        if room_type in self.room_types and self.availability[room_type] > 0:
            self.availability[room_type] -= 1
            return f"Booked {room_type} at {self.name} from {start_date} to {end_date}"
        return "Room type unavailable"

    def check_availability(self, room_type):
        return self.availability.get(room_type, 0)

    def modify_availability(self, room_type, availability):
        if room_type in self.room_types:
            self.availability[room_type] = availability

    def get_accommodation_details(self):
        return {
            'Name': self.name,
            'Location': self.location,
            'Room Types': self.room_types,
            'Availability': self.availability
        }

class Itinerary:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.destinations = []
        self.bookings = []

    def add_destination(self, destination):
        self.destinations.append(destination)

    def add_booking(self, accommodation, room_type, start_date, end_date):
        booking_info = accommodation.book_room(room_type, start_date, end_date)
        self.bookings.append((booking_info, start_date, end_date))

    def get_itinerary_details(self):
        itinerary_details = {
            'Travel Period': (self.start_date, self.end_date),
            'Destinations': [dest.name for dest in self.destinations],
            'Bookings': self.bookings
        }
        return itinerary_details

    def update_destination(self, old_dest_name, new_dest):
        for i, dest in enumerate(self.destinations):
            if dest.name == old_dest_name:
                self.destinations[i] = new_dest
                break

    def update_booking(self, old_booking, new_booking):
        if old_booking in self.bookings:
            index = self.bookings.index(old_booking)
            self.bookings[index] = new_booking

class TravelPlanner:
    def __init__(self):
        self.destinations = {}
        self.accommodations = {}

    def add_destination(self, name, attractions):
        if name not in self.destinations:
            self.destinations[name] = Destination(name, attractions)

    def add_accommodation(self, name, location, room_types, availability):
        if name not in self.accommodations:
            self.accommodations[name] = Accommodation(name, location, room_types, availability)

    def plan_trip( start_date,self, end_date, destination_names, accommodation_bookings):
        itinerary = Itinerary(start_date, end_date)
        for dest_name in destination_names:
            if dest_name in self.destinations:
                itinerary.add_destination(self.destinations[dest_name])
        for acc_name, room_type, acc_start_date, acc_end_date in accommodation_bookings:
            if acc_name in self.accommodations:
                itinerary.add_booking(self.accommodations[acc_name], room_type, acc_start_date, acc_end_date)
        return itinerary.get_itinerary_details()

    def get_destination_details(self, dest_name):
        if dest_name in self.destinations:
            return self.destinations[dest_name].get_destination_details()
        return None

    def get_accommodation_details(self, acc_name):
        if acc_name in self.accommodations:
            return self.accommodations[acc_name].get_accommodation_details()
        return None