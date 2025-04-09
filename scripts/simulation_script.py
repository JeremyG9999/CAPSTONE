from scripts.simulation import *

def get_simulation(simulation_type):
    run1 = Winter()
    run2 = Summer()
    run3 = CustomerSimulation()
    if simulation_type == 'run1':
        return run1
    elif simulation_type == 'run2':
        return run2
    elif simulation_type == 'run3':
        return run3