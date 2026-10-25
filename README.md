# Resident Appointment Booking

A small Python prototype developed for SWE6301 Agile Programming.
It demonstrates Behaviour-Driven Development using behave and Gherkin.

## Stakeholder and problem

The main user is a resident who needs an appointment with a council officer.
The service validates the resident's name and prevents double booking.

## User story

As a resident, I want to book an available appointment so that I can
speak to a council officer.

## Acceptance criteria

- A valid name and available slot produce a confirmed booking.
- A missing or whitespace-only name is rejected without creating a booking.
- An unavailable slot is rejected without changing the existing booking.

## Automated BDD scenarios

1. Successfully book an available appointment.
2. Reject a booking without a resident name.
3. Reject a booking for an already booked slot.

The scenarios check booking outcomes, slot availability and preservation
of the original booking.

## Setup and execution

Run these commands from the project folder in Windows PowerShell.

Create a virtual environment:

```powershell
python -m venv .venv
```

Install dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Run the BDD scenarios:

```powershell
.\.venv\Scripts\python.exe -m behave
```

## Project files

- appointment_service.py: booking logic and input validation.
- features/appointment_booking.feature: Gherkin scenarios.
- features/steps/appointment_steps.py: Python step definitions.
- requirements.txt: project dependency.

## Limitations

This prototype stores bookings in memory and uses time labels for slots.
It has no persistent database, dates, authentication or graphical interface.
The automated scenarios cover selected business rules; they do not
demonstrate production security, accessibility or concurrent booking safety.