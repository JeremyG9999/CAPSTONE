from flask import Blueprint, render_template, request
from scripts.simulation_script import *
from scripts.DB_queries import *
from database_layer import *
from scripts.insert_DB_script import *

home_routes = Blueprint('home_routes', __name__)

@home_routes.route('/simulation', methods=['GET'])
def display_simulation():

    return render_template('home_templates/simulation.html')

@home_routes.route('/run_simulation', methods=['POST'])
def run_simulation():
    day_number = get_day_number() 
    simulation_type = request.form.get("simulation_type")
    run = get_simulation(simulation_type)

    run.simulations() 
    
    save_truck_report() 
    last_entry = get_last_flavor_count() 
    return render_template('home_templates/simulation.html', run=run, day_number=day_number, last_entry=last_entry)

@home_routes.route('/statistics')
def statistics():
    return render_template('home_templates/statistics.html')

@home_routes.route('/about_us')
def about_us():
    return render_template('home_templates/about_us.html')

@home_routes.route('/feedback')
def feedback():
    return render_template('home_templates/feedback.html')

