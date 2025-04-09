import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from scripts.DB_queries import average_truck_order_data, truck_report_logic

def average_truck_order_chart():
    data = truck_report_logic()  
    if not data:
        lava, hot_fudge, blizzard, chocolate, vanilla = [0, 0, 0, 0, 0]
    else:
        avg_data = average_truck_order_data()
        lava, hot_fudge, blizzard, chocolate, vanilla = avg_data
    
    plt.bar('Lava', lava)
    plt.bar('Hot Fudge', hot_fudge)
    plt.bar('Blizzard', blizzard)
    plt.bar('Chocolate', chocolate)
    plt.bar('Vanilla', vanilla)
    plt.xlabel('Flavor')
    plt.ylabel('Average Orders')
    plt.title('Average Truck Order by Flavor')
    plt.grid()
    plt.savefig('static/charts/average_truck_order_chart.png')
    plt.close()