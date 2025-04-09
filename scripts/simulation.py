import random
from scripts.insert_DB_script import (
    save_to_purchases_table,
    save_to_flavors_count_table,
    save_simulation_type,
    save_total_purchases
)
from database_layer import db_setup

class CustomerSimulation:
    def __init__(self):
        self.choice = None
        self.results = []
        self.flavor_count = []
        self.probability = 2
        self.times = 100
        db_setup()
        self.lava = 0
        self.hot_fudge = 0
        self.blizzard = 0
        self.chocolate = 0
        self.vanilla = 0

    def flavors(self):
        flavor_likelihood = ["lava", "hot_fudge", "blizzard", "chocolate", "vanilla"]
        self.choice = random.choice(flavor_likelihood)
        return self.choice
    
    def flavors_count(self):
        if self.choice == "lava":
            self.lava += 1
        elif self.choice == "hot_fudge":
            self.hot_fudge += 1
        elif self.choice == "blizzard":
            self.blizzard += 1
        elif self.choice == "chocolate":
            self.chocolate += 1
        elif self.choice == "vanilla":
            self.vanilla += 1
        self.flavor_count = [self.lava, self.hot_fudge, self.blizzard, self.chocolate, self.vanilla]
        return self.flavor_count
        
    def simulations(self):
        for _ in range(self.times):
            if random.randint(1, self.probability) == 1:
                flavor = self.flavors()
                self.results.append(flavor)
                self.flavors_count()
        save_simulation_type(self)
        save_to_purchases_table(self)
        save_to_flavors_count_table(self)
        save_total_purchases(self)
        return self.results

class Winter(CustomerSimulation):
    def flavors(self):
        flavor_likelihood = ["lava", "hot_fudge", "chocolate", "vanilla", "blizzard"]
        flavor_likelihood += ["blizzard", "blizzard", "chocolate"] 
        self.choice = random.choice(flavor_likelihood)
        return self.choice
    
    def simulations(self):
        self.probability = 2
        self.times = 85
        super().simulations()

class Summer(CustomerSimulation):
    def flavors(self):
        flavor_likelihood = ["lava", "hot_fudge", "chocolate", "vanilla", "blizzard"]
        flavor_likelihood += ["lava", "lava", "hot_fudge"]  
        self.choice = random.choice(flavor_likelihood)
        return self.choice
    
    def simulations(self):
        self.probability = 1
        self.times = 100
        super().simulations()

if __name__ == "__main__":
    run = Winter()  
    run.simulations()