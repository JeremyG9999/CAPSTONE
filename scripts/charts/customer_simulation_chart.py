import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from scripts.DB_queries import customer_simulation_data  

def customer_simulation_chart():
    data = customer_simulation_data()
    if not data:
        data = [0, 0, 0, 0, 0]
    lava, hot_fudge, blizzard, chocolate, vanilla = data

    plt.bar('Lava', lava)
    plt.bar('Hot Fudge', hot_fudge)
    plt.bar('Blizzard', blizzard)
    plt.bar('Chocolate', chocolate)
    plt.bar('Vanilla', vanilla)
    plt.xlabel('Flavor')
    plt.ylabel('Total Purchases')
    plt.title('Customer Simulation')
    plt.grid()
    plt.savefig('static/charts/simulation_chart_Customer.png')
    plt.close()