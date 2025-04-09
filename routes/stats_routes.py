from flask import Blueprint, render_template
from scripts.simulation_script import *
from scripts.DB_queries import *
from database_layer import *
from scripts.insert_DB_script import *
from scripts.charts.truck_chart import *
from scripts.charts.purchases_chart import *
from scripts.charts.customer_simulation_chart import *
from scripts.charts.purchases_over_time_chart import *
from scripts.charts.average_purchases_chart import *
from scripts.charts.average_truck_order_chart import *
from scripts.charts.avg_customer_simulation_chart import *
from scripts.charts.total_sales_chart import *
from scripts.charts.summer_simulation_chart import *
from scripts.charts.winter_simulation_chart import *

stats_routes = Blueprint('statistics', __name__)

@stats_routes.route('/flavor_count_data', methods=['GET'])
def flavor_count_data():
    flavor_data = flavor_counts_data()
    return render_template('stats_templates/flavor_count_display.html', flavor_data=flavor_data)

@stats_routes.route('/truck_report')  
def truck_report(): 
    save_truck_report()
    flavor_totals = truck_report_logic()
    return render_template('stats_templates/truck_report.html', flavor_totals=flavor_totals)

@stats_routes.route('/total_purchases', methods=['GET'])
def save_total_purchase():
    total_purchases = total_purchases_data()
    return render_template('stats_templates/total_purchases.html', total_purchases=total_purchases)

@stats_routes.route('/truck_chart')
def truck_chart():
    generate_truck_chart()
    return render_template('chart_templates/truck_chart.html', truck_chart='static/charts/truck_chart.png')

@stats_routes.route('/purchase_chart')
def purchase_chart():
    generate_purchase_chart()
    return render_template('chart_templates/purchase_chart.html', purchase_chart='static/charts/purchase_chart.png')

@stats_routes.route('/customer_simulation_chart')
def customer_simulation_charts():
    customer_simulation_chart()  

    return render_template('chart_templates/customer_simulation_chart.html', chart='static/charts/simulation_chart_Customer.png')

@stats_routes.route('/summer_simulation_chart')
def summer_simulation_charts():
    summer_simulation_chart()  
    return render_template('chart_templates/summer_simulation_chart.html', chart='static/charts/simulation_chart_Summer.png')

@stats_routes.route('/winter_simulation_chart')
def winter_simulation_charts():
    winter_simulation_chart()  
    return render_template('chart_templates/winter_simulation_chart.html', chart='static/charts/simulation_chart_Winter.png')

@stats_routes.route('/purchases_over_time')
def purchase_over_time():
    purchases_over_time()  
    return render_template('chart_templates/purchases_over_time_chart.html', chart='static/charts/purchases_over_time.png')

@stats_routes.route('/average_purchases')
def average_purchase_route():
    average_purchase_charts()  
    return render_template('chart_templates/average_purchases_chart.html', chart='static/charts/average_purchases_chart.png')

@stats_routes.route('/average_truck_order')
def average_truck_order_route():
    average_truck_order_chart()
    return render_template('chart_templates/average_truck_order_chart.html', chart='static/charts/average_truck_order_chart.png')

@stats_routes.route('/avg_customer_simulation')
def avg_customer_simulation_route():
    avg_customer_simulation() 
    return render_template('chart_templates/avg_customer_simulation_chart.html', chart='static/charts/average_customer_simulation_chart.png')

@stats_routes.route('/total_sales')
def total_sales_route():
    total_sale()  
    return render_template('chart_templates/total_sales_chart.html', chart='static/charts/total_sales.png')