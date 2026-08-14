#  Smart Irrigation AI Agent

##  Project Description

The **Smart Irrigation AI Agent** is a simple Python-based AI agent that makes irrigation decisions using sensor data.

The system takes readings from different sensors such as:

* Soil Moisture
* Temperature
* Humidity
* Rainfall
* Water Tank Level

Based on these values, the AI agent calculates an **irrigation score** and decides whether the water pump should be turned **ON or OFF**.

It also calculates the required watering time based on the soil moisture level.



##  Objectives

The main objectives of this project are:

1. To understand the basic working of an AI agent.
2. To use sensor data for decision-making.
3. To determine whether irrigation is required.
4. To prevent unnecessary water usage.
5. To calculate suitable watering time.
6. To demonstrate AI-based decision-making using simple Python programming.

---

##  How the System Works

The program follows these steps:


Sensor Input
     ↓
Display Sensor Data
     ↓
Calculate Irrigation Score
     ↓
Check Water Tank Level
     ↓
Check Rainfall
     ↓
AI Irrigation Decision
     ↓
Calculate Watering Time
     ↓
Pump ON / Pump OFF




##  Input Used

| Input            | Purpose                                     |
| ---------------- | ------------------------------------------- |
| Soil Moisture    | Determines how dry or wet the soil is       |
| Temperature      | Checks environmental temperature            |
| Humidity         | Determines moisture present in the air      |
| Rainfall         | Checks whether sufficient rain is occurring |
| Water Tank Level | Checks available water for irrigation       |



##  AI Decision Logic

The program calculates an irrigation score.

### Soil Moisture

If soil moisture is below 40%:

Score +3

This indicates that the soil may need water.

### Temperature

If temperature is above 35°C:

Score +2

High temperature can increase water requirements.

### Humidity

If humidity is below 40%:

Score +2


Low humidity indicates a drier environment.

### Rainfall

If rainfall is above 5 mm:

Score -4

Rainfall reduces the need for irrigation.

##  Pump Decision

The final decision is made using the following conditions:

### 1. Low Water Tank Level

If the tank level is below 20%:

PUMP OFF

Reason:

Water tank level is too low.

### 2. Sufficient Rainfall

If rainfall is greater than 5 mm:

PUMP OFF

Reason:

Rainfall is sufficient.

### 3. High Irrigation Score

If the irrigation score is 4 or greater:

PUMP ON


Reason:

Plants need water.

### 4. Otherwise

PUMP OFF

Reason:

Plants have enough water.


##  Watering Time

The watering time depends on soil moisture.

| Soil Moisture | Watering Time |
| ------------- | ------------: |
| Below 20%     |    15 minutes |
| 20%–39%       |    10 minutes |
| 40%–59%       |     5 minutes |
| 60% or above  |     0 minutes |

---

##  Technologies Used

* **Python**
* Conditional statements
* Functions
* User input
* Basic AI decision-making
* Sensor-data simulation



##  How to Run

### Step 1: Install Python

Make sure Python is installed on your computer.

Check using:
python --version


### Step 2: Open the Project

Open the project folder in VS Code.

### Step 3: Run the Program

Open the VS Code terminal and execute:

python irrigation_agent.py

### Step 4: Enter Sensor Values

The program will ask for:

Enter soil moisture (%):
Enter temperature (°C):
Enter humidity (%):
Enter rainfall (mm):
Enter water tank level (%):

Enter the required values.


##  Example

### Input

Enter soil moisture (%): 25
Enter temperature (°C): 38
Enter humidity (%): 35
Enter rainfall (mm): 0
Enter water tank level (%): 80

### AI Decision

Irrigation Score: 7
Decision: PUMP ON
Reason: Plants need water.

### Final Action

Water Pump: ON
Watering Time: 10 minutes


