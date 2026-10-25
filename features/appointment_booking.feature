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