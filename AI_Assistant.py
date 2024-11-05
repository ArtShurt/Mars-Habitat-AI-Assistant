# The AI code was developed separately according to the three resources to be monitored, with their specific classes
# This file is to test the created class in an isolated space

# Importing the class
from Energy_module import system

# Creating an instance of the energy module
Energy = system("energy")

# Initializing simulation
Energy.simulate()