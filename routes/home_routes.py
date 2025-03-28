from flask import Blueprint, render_template
from database_layer import *

home_routes = Blueprint('home_routes', __name__)

@home_routes.route('/simulation', methods=['GET'])
def display_simulation():
    return render_template('simulation.html')

@home_routes.route('/run_simulation', methods=['POST'])
def run_simulation():

    return render_template('simulation.html')

@home_routes.route('/statistics')
def statistics():
    return render_template('statistics.html')

