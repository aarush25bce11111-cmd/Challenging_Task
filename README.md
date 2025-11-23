# Challenging_Task
#  Bus Fare Calculator

#  Project Overview

 The script uses a configurationThis Python script simulates a simple bus fare calculator. It determines the total fare based on the travel distance and the day of the week (weekday or weekend). The fare calculation logic includes a fixed **base fare** and a **distance-based cost**, where the distance is always **rounded up** to the nearest whole kilometer for billing. dictionary to manage rates, making the pricing structure easily adjustable.

# Features

  * **Dynamic Rate Selection:** Automatically selects a different rate per kilometer based on whether the current day is a **WEEKDAY** or a **WEEKEND**.
  * **Distance Rounding:** Bills the customer based on the distance rounded **up** to the nearest whole kilometer (e.g., 8.2 km is billed as 9 km).
  * **Configurable Pricing:** All fare parameters (base fare, rates, currency, max distance) are managed via an external configuration dictionary (`FARE_CONFIG`).
  * **Input Validation:** Handles non-numeric and negative distance inputs gracefully.
  * **Max Distance Warning:** Provides a warning if the entered distance exceeds the configured maximum limit.
  * **Clear Output:** Displays a detailed breakdown of the calculation and the final fare.

# Technologies/Tools Used

  * **Primary Language:** Python 3.x
  * **Built-in Modules:**
      * `math`: Used for the `math.ceil()` function to round up the distance.
      * `time`: Used to determine the current day of the week.
      * `json`: Used to display the configuration in a clean format.
      * `random`: Used to generate a unique transaction ID and a simulated calculation delay.

# Steps to Install & Run the Project

### 1\. Installation

This project requires a functional Python 3 environment. No external libraries are needed.

1.  **Save the Code:** Save the provided Python code into a file named `fare_calculator.py`.

### 2\. Running the Project

Open your terminal or command prompt, navigate to the directory where you saved `fare_calculator.py`, and run the script:

```bash
python fare_calculator.py
```

### 3\. Usage

The script will prompt you for the travel distance:

```
Enter travel distance in kilometers (e.g., 8.5): 
```

Enter a numerical value and press Enter. The script will then display the full configuration, the calculation steps, and the final fare.

# Instructions for Testing

To ensure the calculator works correctly, test it with the following scenarios, keeping the current configuration in mind:

| Configuration Item | Value |
| :--- | :--- |
| `base_fare` | $2.50 |
| `rate_per_km_weekday` | $0.50 |
| `rate_per_km_weekend` | $0.75 |

### Test Cases

| Scenario | Input Distance (km) | Expected Billed Distance (km) | Calculation Example (Assuming WEEKDAY) | Expected Final Fare (WEEKDAY) |
| :--- | :--- | :--- | :--- | :--- |
| **Simple Whole Number** | 10.0 | 10 | $2.50 + (10 \times \$0.50)$ | $7.50 |
| **Fractional Distance** | 8.2 | 9 | $2.50 + (9 \times \$0.50)$ | $7.00 |
| **Distance just above** | 5.01 | 6 | $2.50 + (6 \times \$0.50)$ | $5.50 |
| **Max Limit Check** | 100.0 | 100 | $2.50 + (100 \times \$0.50)$ | $52.50 |

**Note:** For the **WEEKEND** rate, the distance-based cost will be calculated using $\$0.75$ per km instead of $\$0.50$. Verify the output reflects the correct rate based on the day you run the script.

### Error Handling Tests

  * **Invalid Input:** Enter a non-numeric value (e.g., `ten`). The script should output: `Invalid input. Please enter a numerical value for distance.`
  * **Zero/Negative Distance:** Enter `0` or `-5`. The script should output: `Distance must be a positive number.`
  * **Excessive Distance:** Enter `101`. The script should output a warning: `Warning: Distance exceeds the configured max limit of 100 km.` (It will still calculate the fare).

