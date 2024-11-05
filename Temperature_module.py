#calling needed libraries
import datetime as dt
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
    self.actual_value = self.actual_value - (np.random.choice(np.linspace(-1, 1))) #simulating a change in the values of the system
    self.log.append((dt.now(), self.actual_value)) #adding to registry the data collected
    
    #check if the values are safe
    if self.actual_value < self.min_critical_level: #check if the system is below minimun selected value
      print(f"The {self.name} system is under critical value!")
      try:
        self.heat_system
      finally:
        print("The system was heated succesfully")
        
    elif self.actual_value > self.max_critical_level: #check if the system is above maximum selected value
      print(f"The {self.name} system is over critical value!")
      try:
        self.cool_system
      finally:
        print(f"The {self.name} system was cooled succesfully")  
          
    else: #the system is ok
      print("The system its between allowed values")
    
  def system_estimation(self):
    average_change = float(sum(self.log[i][1]-self.log[i-1][1] for i in range(0, int(len(self.log)/2)))/len(self.log))
    self.average_change = average_change
    y = [self.log[i][1] for i in range(0, len(self.log))]
    x = [i for i in range(0, len(self.log))]
    data = plt.plot(x, y)
    x = [i for i in range(0, len(self.log))]
    y = [average_change * x[i] + self.log[0][1] for i in range(0, len(x))]
    data_2 = plt.plot(x, y)
    plt.show()
    del self.log[:]

    return average_change