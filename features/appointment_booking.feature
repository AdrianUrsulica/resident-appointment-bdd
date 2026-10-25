Feature: Resident appointment booking
  As a resident
  I want to book an available appointment
  So that I can speak to a council officer

  Scenario: Successfully book an available appointment
    Given an appointment slot "09:00" is available
    When resident "Alex Smith" books the slot "09:00"
    Then the booking should be confirmed
    And the slot "09:00" should no longer be available

      Scenario: Reject a booking without a resident name
    Given an appointment slot "10:00" is available
    When a resident books the slot "10:00" without a name
    Then the booking should be rejected with "Resident name is required"
    And the slot "10:00" should remain available
    And no booking should be created

      Scenario: Reject a booking for an already booked slot
    Given an appointment slot "11:00" is available
    And resident "Alex Smith" has already booked the slot "11:00"
    When resident "Jamie Brown" books the slot "11:00"
    Then the booking should be rejected with "Appointment slot is unavailable"
    And the slot "11:00" should no longer be available
    And the booking for slot "11:00" should belong to "Alex Smith"
    