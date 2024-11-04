from datetime import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

class  system(object):
  def __init__(self, name):
    self.name = name
    self.actual_value = int(input(f"insert current {self.name} value: "))
    self.critical_level =  int(input(f"insert critical {self.name} value: "))
    self.log = []

  def monitoring(self):
    self.actual_value = self.actual_value - (np.random.choice(np.linspace(-0.5, 0.5)))
    self.log.append((dt.now(), self.actual_value))
    if self.actual_value < self.critical_level:
      return True
      raise RuntimeError(f"The {self.name} system is under critical value")
    else:
      return False

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