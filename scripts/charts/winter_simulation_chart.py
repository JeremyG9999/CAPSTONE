import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from scripts.DB_queries import winter_simulation_data  

def winter_simulation_chart():
    data = winter_simulation_data()
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
    plt.title('Winter Simulation')
    plt.grid()
    plt.savefig('static/charts/simulation_chart_Winter.png')
    plt.close()