from behave import given, when, then
from appointment_service import AppointmentService


@given('an appointment slot "{slot}" is available')
def step_available_slot(context, slot):
    context.service = AppointmentService([slot])


@when('resident "{name}" books the slot "{slot}"')
def step_book_slot(context, name, slot):
    context.result = context.service.book(name, slot)


@then('the booking should be confirmed')
def step_booking_confirmed(context):
    assert context.result == "Booking confirmed"


@then('the slot "{slot}" should no longer be available')
def step_slot_unavailable(context, slot):
    assert slot not in context.service.available_slots

@when('a resident books the slot "{slot}" without a name')
def step_book_without_name(context, slot):
    context.result = context.service.book("", slot)


@then('the booking should be rejected with "{message}"')
def step_booking_rejected(context, message):
    assert context.result == message


@then('the slot "{slot}" should remain available')
def step_slot_remains_available(context, slot):
    assert slot in context.service.available_slots


@then('no booking should be created')
def step_no_booking_created(context):
    assert context.service.bookings == {}

@given('resident "{name}" has already booked the slot "{slot}"')
def step_existing_booking(context, name, slot):
    result = context.service.book(name, slot)
    assert result == "Booking confirmed"


@then('the booking for slot "{slot}" should belong to "{name}"')
def step_booking_owner(context, slot, name):
    assert context.service.bookings[slot] == name
