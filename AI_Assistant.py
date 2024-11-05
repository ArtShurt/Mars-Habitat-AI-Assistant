#The AI ​​code was developed separately according to the three resources to be monitored, with their specific classes
import time
import random
from datetime import datetime, timedelta
import pandas as pd

# Define the EnergyMonitor class for the energy module
class EnergyMonitor:
    def __init__(self, critical_threshold=20.0):
        """
        Initializes the energy monitor.
        :param critical_threshold: Critical energy threshold below which an alert is generated.
        """
        self.critical_threshold = critical_threshold  # critical energy threshold in %
        self.energy_level = 100.0  # initial energy level in %
        self.energy_log = []  # list to store the energy log

    # Method to check the energy level
    def check_energy(self):
        if self.energy_level < self.critical_threshold:
            print(f"Critical Alert: Energy level is at {self.energy_level}% - Below critical threshold!")
        else:
            print(f"Energy level is safe: {self.energy_level}%")

    # Method to log the energy level
    def log_energy(self):
        timestamp = datetime.now()
        self.energy_log.append({'timestamp': timestamp, 'energy_level': self.energy_level})
        print(f"Energy log: {self.energy_level}% at {timestamp}")

    # Method to simulate energy usage
    def simulate_energy_usage(self):
        self.energy_level -= random.uniform(0.5, 3.0)  # Random decrease of energy level
        if self.energy_level < 0:
            self.energy_level = 0  # Ensure the energy level does not fall below 0

    # Method to predict energy usage
    def predict_energy_usage(self, hours=5):
        if len(self.energy_log) > 1:
            # Calculate the average consumption rate per hour
            energy_levels = [entry['energy_level'] for entry in self.energy_log]
            consumption_rate = (energy_levels[0] - energy_levels[-1]) / len(self.energy_log)
            predicted_energy = self.energy_level - (consumption_rate * hours)
            return max(predicted_energy, 0)  # Do not allow energy level to drop below 0
        else:
            return self.energy_level  # Not enough data to predict

# Create an instance of the energy monitor
energy_monitor = EnergyMonitor()

# Simulation: log and check energy every hour
for _ in range(10):  # Simulate 10 hours
    energy_monitor.simulate_energy_usage()  # Simulate energy usage
    energy_monitor.check_energy()  # Check the energy level
    energy_monitor.log_energy()  # Log the energy level
    time.sleep(1)  # Pause for 1 second to simulate the passage of time

# Display energy logs in a DataFrame
energy_df = pd.DataFrame(energy_monitor.energy_log)
print(energy_df)

# Predict energy for the next 5 hours
predicted_energy = energy_monitor.predict_energy_usage(hours=5)
print(f"\nProjected energy level for the next 5 hours: {predicted_energy}%")
