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
    self.min_critical_level =  int(input(f"Insert critical {self.name} (inferior): ")) #setting minimum value
    self.max_critical_level =  int(input(f"Insert critical {self.name} (superior): ")) #setting maximum value
    self.log = [] #log with data registered

  #command to cool down the system
  def cool_system(self):
    self.actual_value -= float(input("How much is the system going to cool down?:" ))
    
  #command to heat up the system
  def heat_system(self):
    self.actual_value += float(input("How much is the system going to heat up?: " ))

  #method to check the values of the system
  def monitoring(self):
    self.actual_value = self.actual_value - (np.random.choice(np.linspace(-2, 2))) #simulating a change in the values of the system
    print(f"the actual {self.name} value is {self.actual_value}")
    self.log.append((dt.now(), self.actual_value)) #adding to registry the data collected
    
    #check if the values are safe
    if self.actual_value < self.min_critical_level: #check if the system is below minimun selected value
      print(f"The {self.name} system is under critical value!")
      try:
        self.heat_system()
      finally:
        print("The system was heated succesfully")
        
    elif self.actual_value > self.max_critical_level: #check if the system is above maximum selected value
      print(f"The {self.name} system is over critical value!")
      try:
        self.cool_system()
      finally:
        print(f"The {self.name} system was cooled succesfully")  
          
    else: #the system is ok
      print("The system its between allowed values")
    
  #method to estimate future values with collected data
  def system_estimation(self):
    average_change = float(sum(self.log[i][1]-self.log[i-1][1] for i in range(0, len(self.log))))/len(self.log)
    future_value_prediction = self.actual_value + average_change
    print(f"The predicted next value is {future_value_prediction}")
   
  #method to create a graph with all the collected data  
  def collected_data_plot(self):
    x = [i for i in range(0, len(self.log))]
    y = [self.log[i][1] for i in range(0, len(self.log))]
    data = plt.plot(x, y)
    plt.show()
    
  #method to create a data frame with all collected data
  def collected_data_frame(self):
    data_frame = pd.DataFrame(self.log)
    print(data_frame)
  
  #method to run a simulation over x hours
  def simulate(self):
    x = int(input("How many hours you want to simulate? "))
    for i in range(1, x):
      try:
        self.monitoring()
        self.system_estimation()
        print("-" * 50)
        t.sleep(1)
      finally:
        pass
    
    #asking the user to print a dataframe with all collected data  
    while True:
      df = input("Print dataframe? [Y/N]: ").upper()
      if df == "Y":
        try:
          self.collected_data_frame()
          break
        finally:
          pass
      elif df == "N":
        break
      else:
        print("Invalid command, please try again")
    
    #asking the user to print a plot with all the data    
    while True:
      df = input("Print plot with data? [Y/N]: ").upper()
      if df == "Y":
        try:
          self.collected_data_plot()
          break
        finally:
          pass
      elif df == "N":
        break
      else:
        print("Invalid command, please try again")
        
#creating an instance of the temperature module
temperature = system("temperature")

#initializing simulation
temperature.simulate()