#calling needed libraries
from datetime import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import time as t
import pandas as pd

#creating the class (it will be oriented to temperature)
class  system(object):
  def __init__(self, name):
    self.name = name #setting name to the system
    self.actual_value = int(input(f"Insert current {self.name}: ")) #setting actual value
    self.min_critical_level =  int(input(f"Insert critical {self.name} (minimum): ")) #setting minimum value
    self.max_critical_level =  int(input(f"Insert critical {self.name} (maximum): ")) #setting maximum value
    self.log = [] #log with data registered

  #command to cool down the system
  def cool_system(self):
    self.actual_value -= float(input("How much is the system going to cool down?:" ))
    print("Cooling system...")
    t.sleep(2)
    
  #command to heat up the system
  def heat_system(self):
    self.actual_value += float(input("How much is the system going to heat up?: " ))
    print("Heating system...")
    t.sleep(2)

  #method to check the values of the system
  def monitoring(self):
    self.actual_value = self.actual_value - (np.random.choice(np.linspace(-2, 2))) #simulating a change in the values of the system
    print(f"The actual {self.name} value is {round(self.actual_value, 3)}°") #printing the value obtained
    self.log.append((dt.now(), self.actual_value)) #adding to registry the data collected
    
    #check if the values are safe
    if self.actual_value < self.min_critical_level: #check if the system is below minimun selected value
      print("The system is under critical value!")
      try:
        self.heat_system()
      finally:
        print("")
        print("The system was heated succesfully")
        t.sleep(1)
        
    elif self.actual_value > self.max_critical_level: #check if the system is above maximum selected value
      print("The system is over critical value!")
      try:
        self.cool_system()
      finally:
        print("")
        print("The system was cooled succesfully")  
        t.sleep(1)
          
    else: #the system is ok
      print("The system its between allowed values")
    
  #method to estimate future values with collected data
  def system_estimation(self):
    average_change = float(sum(self.log[i][1]-self.log[i-1][1] for i in range(1, len(self.log))))/len(self.log)
    future_value_prediction = self.actual_value + average_change
    print(f"The predicted next value is {round(future_value_prediction, 3)}°")
   
  #method to create a graph with all the collected data  
  def collected_data_plot(self):
    x = [i for i in range(0, len(self.log))]
    y = [self.log[i][1] for i in range(0, len(self.log))]
    data = plt.plot(x, y)
    plt.show()
    
  #method to create a data frame with all collected data
  def collected_data_frame(self):
    data_frame = pd.DataFrame(self.log)
    data_frame = data_frame.rename(columns={0: "Hour", 1: "Temperature"})  #changing the name of the columns
    print(data_frame)
  
  #method to run a simulation over x hours
  def simulate(self):
    x = int(input("How many hours you want to simulate? "))
    print("-" * 50)
    t.sleep(2)
    for i in range(1, x):
      try:
        self.monitoring()
        print("")
        self.system_estimation()
        print("-" * 50)
        t.sleep(1)
      finally:
        pass
    
    #asking the user if they want a dataframe with all collected data  
    while True:
      df = input("Print dataframe? [Y/N]: ").upper()
      if df == "Y":
        try:
          print("Printing data frame...")
          t.sleep(2)
          print("-" * 50)
          self.collected_data_frame()
          print("-" * 50)
          break
        finally:
          pass
      elif df == "N":
        break
      else:
        print("Invalid command, please try again")
  
    t.sleep(1)
  
    #asking the user if they want a plot with all the data    
    while True:
      df = input("Print plot with data? [Y/N]: ").upper()
      if df == "Y":
        try:
          print("Printing plot...")
          print("")
          self.collected_data_plot()
          break
        finally:
          pass
      elif df == "N":
        break
      else:
        print("Invalid command, please try again")
        
#creating an instance of the temperature module
if __name__ == "__main__":
  temperature = system("temperature")

  #initializing simulation
  temperature.simulate()