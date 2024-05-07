import unittest
from travelItineraryPlanner import Destination, Accommodation, Itinerary, TravelPlanner
import datetime

class TestDestination(unittest.TestCase):
    def setUp(self):
        self.destination = Destination("Paris", ["Eiffel Tower", "Louvre Museum"])

    def test_add_attraction(self):
        self.destination.add_attraction("Notre Dame")
        self.assertIn("Notre Dame", self.destination.attractions)

    def test_remove_attraction(self):
        self.destination.remove_attraction("Louvre Museum")
        self.assertNotIn("Louvre Museum", self.destination.attractions)

    def test_list_attractions(self):
        attractions = self.destination.list_attractions()
        self.assertEqual(attractions, ["Eiffel Tower", "Louvre Museum"])

    def test_get_destination_details(self):
        details = self.destination.get_destination_details()
        self.assertEqual(details['Name'], "Paris")
        self.assertIn("Eiffel Tower", details['Attractions'])

class TestAccommodation(unittest.TestCase):
    def setUp(self):
        self.accommodation = Accommodation("Hilton Paris", "Paris", {"single": 2, "double": 2}, {"single": 10, "double": 5})

    def test_book_room(self):
        result = self.accommodation.book_room("single", "2023-06-01", "2023-06-05")
        self.assertEqual(self.accommodation.availability["single"], 9)
        self.assertIn("Booked single", result)

    def test_check_availability(self):
        available = self.accommodation.check_availability("double")
        self.assertEqual(available, 5)

    def test_modify_availability(self):
        self.accommodation.modify_availability("double", 10)
        self.assertEqual(self.accommodation.availability["double"], 10)

    def test_get_accommodation_details(self):
        details = self.accommodation.get_accommodation_details()
        self.assertEqual(details['Name'], "Hilton Paris")
        self.assertEqual(details['Location'], "Paris")

class TestItinerary(unittest.TestCase):
    def setUp(self):
        self.itinerary = Itinerary(datetime.date( 5,2023, 10), datetime.date(2023, 5, 20))
        self.destination = Destination("Paris", ["Eiffel Tower"])
        self.accommodation = Accommodation("Hilton Paris", "Paris", {"double": 2}, {"double": 5})

    def test_add_destination(self):
        self.itinerary.add_destination(self.destination)
        self.assertIn(self.destination, self.itinerary.destinations)

    def test_add_booking(self):
        self.itinerary.add_booking(self.accommodation, "double", "2023-05-10", "2023-05-15")
        self.assertEqual(len(self.itinerary.bookings), 1)

    def test_get_itinerary_details(self):
        self.itinerary.add_destination(self.destination)
        details = self.itinerary.get_itinerary_details()
        self.assertIn("Paris", details['Destinations'])

    def test_update_destination(self):
        new_dest = Destination("Nice", ["Promenade"])
        self.itinerary.add_destination(self.destination)
        self.itinerary.update_destination("Paris", new_dest)
        self.assertIn(new_dest, self.itinerary.destinations)
        self.assertNotIn(self.destination, self.itinerary.destinations)

class TestTravelPlanner(unittest.TestCase):
    def setUp(self):
        self.planner = TravelPlanner()
        self.planner.add_destination("Paris", ["Eiffel Tower"])
        self.planner.add_accommodation("Hilton Paris", "Paris", {"double": 2}, {"double": 5})

    def test_plan_trip(self):
        itinerary_details = self.planner.plan_trip(datetime.date(2023, 5, 10), datetime.date(2023, 5, 20), ["Paris"], [("Hilton Paris", "double", "2023-05-10", "2023-05-15")])
        self.assertIn("Paris", itinerary_details['Destinations'])

    def test_get_destination_details(self):
        details = self.planner.get_destination_details("Paris")
        self.assertIn("Eiffel Tower", details['Attractions'])

    def test_get_accommodation_details(self):
        details = self.planner.get_accommodation_details("Hilton Paris")
        self.assertIn("double", details['Room Types'])

if __name__ == '__main__':
    unittest.main()