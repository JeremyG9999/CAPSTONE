import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from scripts.DB_queries import average_purchases, flavor_counts_data

def avg_customer_simulation():
    data = flavor_counts_data() 
    if not data:
        lava, hot_fudge, blizzard, chocolate, vanilla = [0, 0, 0, 0, 0]
    else:
        avg_data = average_purchases()
        lava, hot_fudge, blizzard, chocolate, vanilla = avg_data
    
    plt.bar('Lava', lava)
    plt.bar('Hot Fudge', hot_fudge)
    plt.bar('Blizzard', blizzard)
    plt.bar('Chocolate', chocolate)
    plt.bar('Vanilla', vanilla)
    plt.xlabel('Flavor')
    plt.ylabel('Average Customer Simulation')
    plt.title('Average Customer Simulation Amount')
    plt.grid()
    plt.savefig('static/charts/average_customer_simulation_chart.png')
    plt.close()