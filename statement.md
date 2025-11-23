 Bus Fare Calculator

 Problem Statement

The manual calculation of bus fares is often complex, requiring operators or systems to account for various factors such as base charges, distance traveled, and variable rates based on the day of the week (weekdays vs. weekends). This system must also handle fractional distances by applying a consistent, simple rounding rule for billing purposes (e.g., always rounding up to the nearest whole unit).

The challenge is to create a simple, robust, and easily configurable calculation engine in Python that automates this process, ensuring accurate and transparent fare calculation based on these dynamic rules.

 Scope of the Project

The Bus Fare Calculator is a command-line utility focused only on the core fare calculation logic.

In Scope:

Implementing the calculate_fare function to correctly apply base fare and distance rate.

Determining the current day type (WEEKDAY or WEEKEND) to select the appropriate rate.

Enforcing the billing rule of rounding the distance up using math.ceil().

Accepting user input for distance and handling basic validation (numeric, positive).

Using a central FARE_CONFIG dictionary to hold all changeable parameters.

Out of Scope:

Integration with external databases or real-time systems (e.g., GPS tracking, payment gateways).

A graphical user interface (GUI).

Complex fare structures (e.g., zonal pricing, peak hour surcharges, senior discounts).

Currency conversion or exchange rate tracking.

 Target Users

The primary target users for this script are:

Software Developers/System Integrators: Individuals needing a clean, self-contained Python module to integrate into a larger transportation or ticketing system.

Transportation Analysts: Users who need to quickly model and test different fare configurations (e.g., changing the weekend rate) without modifying the core calculation logic.

Educational Users/Learners: Students or developers learning fundamental Python programming, function design, and basic mathematical operations (math.ceil) in a practical context.

 High-Level Features

Feature

Description

Configurable Rates

All pricing parameters (base fare, rates, currency) are stored in an easily editable FARE_CONFIG object, promoting maintainability.

Contextual Pricing

The application automatically determines the day of the week and selects the appropriate WEEKDAY or WEEKEND rate.

Billing Consistency

Utilizes distance rounding (always up to the nearest kilometer) to ensure consistent and simplified billing for fractional trips.

Input Robustness

Includes basic error handling for non-numeric input and provides warnings for distances exceeding the defined maximum limit.

Transparent Output

Provides a detailed, formatted output showing the applied rate, the billed distance, and the final total fare.