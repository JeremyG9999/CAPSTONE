import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from scripts.DB_queries import flavor_counts_data

def purchases_over_time():
    data = flavor_counts_data()
    if not data:
        data = [(0, 0, 0, 0, 0, 0)]
    periods = []
    lava = []
    hot_fudge = []
    blizzard = []
    chocolate = []
    vanilla = []
    
    for row in data:
        periods.append(row[0])
        lava.append(row[1])
        hot_fudge.append(row[2])
        blizzard.append(row[3])
        chocolate.append(row[4])
        vanilla.append(row[5])
    
    plt.plot(periods, lava, label='Lava', marker='o')
    plt.plot(periods, hot_fudge, label='Hot Fudge', marker='o')
    plt.plot(periods, blizzard, label='Blizzard', marker='o')
    plt.plot(periods, chocolate, label='Chocolate', marker='o')
    plt.plot(periods, vanilla, label='Vanilla', marker='o')
    plt.xlabel('Period')
    plt.ylabel('Cumulative Sales')
    plt.title('Cumulative Sales Over Time')
    plt.legend()
    plt.grid()
    plt.savefig('static/charts/purchases_over_time.png')
    plt.close()