#The AI ​​code was developed separately according to the three resources to be monitored, with their specific classes

#-------------------------------------------------------------------------------------------------------------------------#

#Code of the AI about Oxigen Levels 
#Goals = Monitor Oxigen, Warn if the resource goes down and log data every hour and provide predictions based on historical data

import random
import datetime
import time

class OxygenMonitor:
    def __init__(self, initial_oxygen_level, critical_threshold=19.5, refill_threshold=20.0, refill_rate=1.0):
        #Initializes the OxygenMonitor with a critical threshold:
        # - Param critical_threshold: The minimum safe level of oxygen (in %)
        # - Param refill_threshold: The level at which oxygen starts refilling.
        # - Param refill_rate: The rate at which oxygen is replenished.
        self.oxygen_level = initial_oxygen_level  #Set initial oxygen level based on user input (% of air composition)
        self.critical_threshold = critical_threshold
        self.refill_threshold = refill_threshold
        self.refill_rate = refill_rate
        self.log = []  # List to store oxygen level logs

    def update_oxygen_level(self):
        #Simulates a change in the oxygen level due to consumption or environmental changes.
        #If the oxygen level drops below the refill threshold, it begins to refill
        if self.oxygen_level < self.refill_threshold:
            self.oxygen_level += self.refill_rate #Refill oxygen to simulate a recovery or oxygen generation system
            print(f"Refilling oxygen... Current level: {self.oxygen_level:.2f}%")
        else:
            #Otherwise, consume oxygen normally
            self.oxygen_level -= random.uniform(0.1, 0.5)
        
        self.oxygen_level = max(self.oxygen_level, 0)  #Prevents negative levels

    def check_critical(self):
        #Checks if the oxygen level is below the critical threshold. If it is, it prints a warning.
        if self.oxygen_level < self.critical_threshold:
            print("WARNING: Oxygen level is below the critical threshold!")
            print(f"Current oxygen level: {self.oxygen_level:.2f}%")
        else:
            print(f"Oxygen level is safe at {self.oxygen_level:.2f}%.")

    def log_data(self):
        #Logs the current oxygen level with a timestamp.
        timestamp = datetime.datetime.now()
        self.log.append((timestamp, self.oxygen_level))
        print(f"Logged data: {timestamp} - Oxygen level: {self.oxygen_level:.2f}%")

    def predict_next_level(self):
        #Predicts the next oxygen level based on the historical data.
        #Uses the average consumption rate as the basis for the prediction.
        #Calculate average change in oxygen level from the log data
        if len(self.log) > 1:
            total_consumption = 0
            for i in range(1, len(self.log)):
                total_consumption += (self.log[i-1][1] - self.log[i][1])
            avg_consumption_rate = total_consumption / (len(self.log) - 1)
            predicted_next_level = self.oxygen_level - avg_consumption_rate
            print(f"Predicted next oxygen level: {predicted_next_level:.2f}%")
        else:
            print("Not enough data to make a prediction.")

    def run_monitoring_cycle(self):
        #Runs a single cycle of monitoring: updates oxygen level, checks for critical levels, logs the data, and predicts the next level
        self.update_oxygen_level()
        self.check_critical()
        self.log_data()
        self.predict_next_level()


#Main code to simulate the monitoring process
if __name__ == "__main__":
    initial_oxygen = float(input("Enter the initial oxygen level (%): "))
    oxygen_monitor = OxygenMonitor(initial_oxygen_level=initial_oxygen, critical_threshold=19.5, refill_threshold=20.0, refill_rate=1.0)  # Set a critical threshold (in %)

    #Simulating a monitoring process every hour
    print("----------------------------------------------------------------------")
    for _ in range(10):  #Run for "10" hours as an example
        oxygen_monitor.run_monitoring_cycle()
        print("----------------------------------------------------------------------")
        time.sleep(1)  #Pause for 1 second instead of an hour for demo purposes