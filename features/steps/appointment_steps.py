from behave import given, when, then


@given('an appointment slot "{slot}" is available')
def step_available_slot(context, slot):
    context.available_slots = {slot}


@when('resident "{name}" books the slot "{slot}"')
def step_book_slot(context, name, slot):
    context.result = None  # Booking behaviour is not implemented yet.


@then('the booking should be confirmed')
def step_booking_confirmed(context):
    assert context.result == "Booking confirmed"


@then('the slot "{slot}" should no longer be available')
def step_slot_unavailable(context, slot):
    assert slot not in context.available_slots