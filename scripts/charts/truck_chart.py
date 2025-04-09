import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from scripts.DB_queries import truck_report_logic

def generate_truck_chart():
    data = truck_report_logic()
    periods = []
    lava = []
    hot_fudge = []
    blizzard = []
    chocolate = []
    vanilla = []
    
    for row in data:
        periods.append(row[0])
        lava.append(row[3])
        hot_fudge.append(row[4])
        blizzard.append(row[5])
        chocolate.append(row[6])
        vanilla.append(row[7])
    
    plt.plot(periods, lava, label='Lava', marker='o')
    plt.plot(periods, hot_fudge, label='Hot Fudge', marker='o')
    plt.plot(periods, blizzard, label='Blizzard', marker='o')
    plt.plot(periods, chocolate, label='Chocolate', marker='o')
    plt.plot(periods, vanilla, label='Vanilla', marker='o')
    plt.xlabel('Period')
    plt.ylabel('Total Purchases')
    plt.title('Truck Report Flavor Totals')
    plt.legend()
    plt.grid()
    plt.savefig('static/charts/truck_chart.png')
    plt.close()
