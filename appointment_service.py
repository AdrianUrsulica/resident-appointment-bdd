class AppointmentService:
    def __init__(self, available_slots):
        self.available_slots = set(available_slots)
        self.bookings = {}

    def book(self, name, slot):
        self.available_slots.remove(slot)
        self.bookings[slot] = name
        return "Booking confirmed"