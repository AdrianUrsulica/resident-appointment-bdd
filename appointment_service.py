class AppointmentService:
    def __init__(self, available_slots):
        self.available_slots = set(available_slots)
        self.bookings = {}

    def book(self, name, slot):
        if not isinstance(name, str) or not name.strip():
            return "Resident name is required"

        if slot not in self.available_slots:
            return "Appointment slot is unavailable"

        self.available_slots.remove(slot)
        self.bookings[slot] = name.strip()
        return "Booking confirmed"