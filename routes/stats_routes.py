from flask import Blueprint, render_template
from database_layer import *

stats_routes = Blueprint('statistics', __name__)

@stats_routes.route('/flavor_count_data', methods=['GET'])
def flavor_count_data():
    return render_template('flavor_count_display.html')

@stats_routes.route('/truck_report')  
def truck_report(): 
    return render_template('truck_report.html')

@stats_routes.route('/flavor_count_AI', methods=['GET'])
def predict():
    return render_template('flavor_count_AI.html')

@stats_routes.route('/truck_order_AI', methods=['GET'])
def predict_truck():
    return render_template('truck_order_AI.html')