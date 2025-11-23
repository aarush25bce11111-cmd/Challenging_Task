import math 
import time 
import json
import random

FARE_CONFIG = {
    "base_fare": 2.50,
    "rate_per_km_weekday": 0.50,
    "rate_per_km_weekend": 0.75,
    "max_distance_km": 100,
    "currency": "USD"
}

def get_current_day_type():
    day_of_week = time.localtime().tm_wday
    if day_of_week >= 5:
        return "WEEKEND"
    else:
        return "WEEKDAY"

def calculate_fare(distance_km: float, config: dict) -> float:
    day_type = get_current_day_type()
    if day_type == "WEEKEND":
        rate_per_km = config["rate_per_km_weekend"]
    else:
        rate_per_km = config["rate_per_km_weekday"]
    billed_distance = math.ceil(distance_km)
    distance_cost = billed_distance * rate_per_km
    total_fare = config["base_fare"] + distance_cost  
    print(f"\n> Calculated with **{day_type}** rate: {config['currency']} {rate_per_km:.2f} per km.")
    print(f"> Billed distance (rounded up): {billed_distance} km.") 
    return total_fare

def run_calculator():
    transaction_id = f"TXN-{random.randint(1000, 9999)}"
    print(f"---  Bus Fare Calculator - {transaction_id} ---")
    print("\n##  Fare Configuration (via JSON)")
    print(json.dumps(FARE_CONFIG, indent=4))
    print("---------------------------------------")
    
    try:
        distance_str = input("Enter travel distance in kilometers (e.g., 8.5): ")
        distance = float(distance_str)
        if distance <= 0:
            print(" Distance must be a positive number.")
            return    
        if distance > FARE_CONFIG["max_distance_km"]:
            print(f" Warning: Distance exceeds the configured max limit of {FARE_CONFIG['max_distance_km']} km.")
        print("\nCalculating fare...")
        time.sleep(random.uniform(0.5, 1.5))
        final_fare = calculate_fare(distance, FARE_CONFIG)
        print("\n--- ✅ FARE RESULT ---")
        print(f"**Distance Traveled:** {distance:.2f} km")
        print(f"**Base Fare:** {FARE_CONFIG['currency']} {FARE_CONFIG['base_fare']:.2f}")
        print(f"**TOTAL FARE:** {FARE_CONFIG['currency']} {final_fare:.2f}")
        print("-----------------------")
    except ValueError:
        print("\n Invalid input. Please enter a numerical value for distance.")
    except Exception as e:
        print(f"\n An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_calculator()