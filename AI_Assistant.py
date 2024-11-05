#The AI ​​code was developed separately according to the three resources to be monitored, with their specific classes

#-------------------------------------------------------------------------------------------------------------------------#

#Oxygen Module:

#Importing Class
from Oxygen_Module import OxygenMonitor

#Initialize the oxygen monitor
monitor = OxygenMonitor(initial_oxygen_level= float(input("Enter the initial oxygen level (%): ")), critical_threshold=19.5)

print("-" * 50)

#Simulating
for _ in range(10):  #Simulating ten hours 
    monitor.run_monitoring_cycle()
    monitor.plot_oxygen_levels()
    print("-" * 50)