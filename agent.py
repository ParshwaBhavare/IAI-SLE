
# Function to display sensor data
def display_sensor_data(soil_moisture, temperature, humidity,rainfall, tank_level):

    print("\n---------- SENSOR DATA ----------")
    print("Soil Moisture :", soil_moisture, "%")
    print("Temperature   :", temperature, "°C")
    print("Humidity      :", humidity, "%")
    print("Rainfall      :", rainfall, "mm")
    print("Water Tank    :", tank_level, "%")
    print("--------------------------------")


# Function for AI decision
def irrigation_decision(soil_moisture, temperature, humidity, rainfall, tank_level):

    score = 0

    # Check soil moisture
    if soil_moisture < 40:
        score += 3

    # Check temperature
    if temperature > 35:
        score += 2

    # Check humidity
    if humidity < 40:
        score += 2

    # Check rainfall
    if rainfall > 5:
        score -= 4

    print("\n---------- AI DECISION ----------")
    print("Irrigation Score:", score)

    # Make final decision
    if tank_level < 20:
        decision = "PUMP OFF"
        reason = "Water tank level is too low."

    elif rainfall > 5:
        decision = "PUMP OFF"
        reason = "Rainfall is sufficient."

    elif score >= 4:
        decision = "PUMP ON"
        reason = "Plants need water."

    else:
        decision = "PUMP OFF"
        reason = "Plants have enough water."

    print("Decision:", decision)
    print("Reason:", reason)

    return decision


# Function to calculate watering time
def calculate_watering_time(soil_moisture):

    if soil_moisture < 20:
        return 15

    elif soil_moisture < 40:
        return 10

    elif soil_moisture < 60:
        return 5

    else:
        return 0


# Main program
def main():

    print("   SMART IRRIGATION AI AGENT")

    # Take sensor values
    soil_moisture = float(input("Enter soil moisture (%): "))
    temperature = float(input("Enter temperature (°C): "))
    humidity = float(input("Enter humidity (%): "))
    rainfall = float(input("Enter rainfall (mm): "))
    tank_level = float(input("Enter water tank level (%): "))

    # Display sensor data
    display_sensor_data(soil_moisture,temperature,humidity,rainfall,tank_level )

    # AI makes decision
    decision = irrigation_decision(soil_moisture,temperature,humidity,rainfall,tank_level)

    # Calculate watering time
    watering_time = calculate_watering_time(soil_moisture)

    # Display final action
    print("\n FINAL ACTION ")

    if decision == "PUMP ON":
        print("Water Pump: ON")
        print("Watering Time:", watering_time, "minutes")

    else:
        print("Water Pump: OFF")
        print("No irrigation required.")



# Start the program
if __name__ == "__main__":
    main()
