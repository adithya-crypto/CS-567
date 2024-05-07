# Travel Itinerary Planner

## Overview:
The Travel Itinerary Planner project facilitates efficient trip planning by managing destinations, accommodations, and itineraries. Here's a breakdown of the key components:

- **Destination:** Manages destination details and attractions.
- **Accommodation:** Handles accommodation details and availability.
- **Itinerary:** Organizes travel plans including destinations and accommodation bookings.
- **TravelPlanner:** Facilitates trip planning by coordinating destinations and accommodations.

## Code Structure:

### Classes:
1. **Destination:**
    - Manages destination details and attractions.
    - Methods:
        - `add_attraction(attraction)`: Adds an attraction to the destination.
        - `remove_attraction(attraction)`: Removes an attraction from the destination.
        - `list_attractions()`: Lists all attractions of the destination.
        - `update_attractions(attractions)`: Updates the list of attractions.
        - `get_destination_details()`: Retrieves destination details.

2. **Accommodation:**
    - Manages accommodation details and availability.
    - Methods:
        - `book_room(room_type, start_date, end_date)`: Books a room for specified dates.
        - `check_availability(room_type)`: Checks availability for a room type.
        - `modify_availability(room_type, availability)`: Modifies availability of a room type.
        - `get_accommodation_details()`: Retrieves accommodation details.

3. **Itinerary:**
    - Organizes travel plans including destinations and accommodation bookings.
    - Methods:
        - `add_destination(destination)`: Adds a destination to the itinerary.
        - `add_booking(accommodation, room_type, start_date, end_date)`: Adds a booking to the itinerary.
        - `get_itinerary_details()`: Retrieves itinerary details.
        - `update_destination(old_dest_name, new_dest)`: Updates destination details.
        - `update_booking(old_booking, new_booking)`: Updates booking details.

4. **TravelPlanner:**
    - Facilitates trip planning by coordinating destinations and accommodations.
    - Methods:
        - `add_destination(name, attractions)`: Adds a destination to the planner.
        - `add_accommodation(name, location, room_types, availability)`: Adds accommodation to the planner.
        - `plan_trip(start_date, end_date, destination_names, accommodation_bookings)`: Plans a trip and returns itinerary details.
        - `get_destination_details(dest_name)`: Retrieves destination details.
        - `get_accommodation_details(acc_name)`: Retrieves accommodation details.

### Testing:
The project includes comprehensive unit tests for each class to ensure functionality and reliability. Test cases cover various scenarios for accurate validation.

## Conclusion:
The Travel Itinerary Planner project provides a robust framework for efficient trip planning. With well-defined classes and thorough testing, it ensures reliability and accuracy in managing travel arrangements.

For more details, refer to the provided unit test cases and class implementations.
