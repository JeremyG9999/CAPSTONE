import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from scripts.DB_queries import total_sales, flavor_counts_data

def total_sale():
    if not flavor_counts_data():
        data = 0
    else:
        data = total_sales()

    plt.bar('Total Sales', data)
    plt.xlabel('Flavor')
    plt.ylabel('Total Purchases')
    plt.title('Total Cumulative Sales')
    plt.grid()
    plt.savefig('static/charts/total_sales.png')
    plt.close()