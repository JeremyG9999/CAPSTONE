import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from scripts.DB_queries import flavor_counts_data, average_purchases

def average_purchase_charts():
    data = flavor_counts_data()     
    if not data:
        lava, hot_fudge, blizzard, chocolate, vanilla = [0, 0, 0, 0, 0]
    else:  # returns error if sql query is ran with no rows for AVG
        avg_data = average_purchases() 
        lava, hot_fudge, blizzard, chocolate, vanilla = avg_data
    
    plt.bar('Lava', lava)
    plt.bar('Hot Fudge', hot_fudge)
    plt.bar('Blizzard', blizzard)
    plt.bar('Chocolate', chocolate)
    plt.bar('Vanilla', vanilla)
    plt.xlabel('Flavor')
    plt.ylabel('Average Purchases per Day')
    plt.title('Average Purchases per Day by Flavor')
    plt.grid()
    plt.savefig('static/charts/average_purchases_chart.png')
    plt.close()