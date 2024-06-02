from flask import Flask, request, jsonify, render_template
import sqlite3
from flask_cors import CORS
from dash import dcc, html, dash_table
import dash
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import os
import csv
from homeassistant_api import Client
from datetime import datetime
import time
import threading
from llama_integration import get_plant_care_recommendation  # Updated import

# Home Assistant configuration
ha_ip_addr = '10.11.22.52'
ha_access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIzMGY5NTZmYWQxMTM0YzJiYWVkMmNmMDgxMTk2NmUyNSIsImlhdCI6MTcxNzI0MzA0MywiZXhwIjoyMDMyNjAzMDQzfQ.IOfRnnqDmJ3bA3LYg_sTUGdWFs5djNIIsOPEvSn9ZiE'

# Entity IDs for your sensors
entity_ids = {
    "temperature": "sensor.psoc6_micropython_sensornode_office_box_temperature",
    "humidity": "sensor.psoc6_micropython_sensornode_office_box_relative_humidity",
    "light": "sensor.psoc6_micropython_sensornode_office_box_light"
}

# CSV file to store the data
csv_file = "sensor_data1.csv"

# Function to initialize the CSV file with headers
def initialize_csv(file):
    with open(file, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "temperature", "humidity", "light"])

# Function to append data to the CSV file
def append_to_csv(file, data):
    with open(file, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)

# Initialize the CSV file
initialize_csv(csv_file)

# Function to retrieve current data and store in CSV
def retrieve_and_store_data():
    with Client(
        f'http://{ha_ip_addr}:8123/api',
        ha_access_token
    ) as client:
        while True:
            try:
                # Retrieve current sensor values every 30 seconds and store in CSV
                sensor_data1 = {}
                for name, entity_id in entity_ids.items():
                    entity = client.get_entity(entity_id=entity_id)
                    try:
                        sensor_data1[name] = float(entity.state) if isinstance(entity.state, (float, int, str)) else float(entity.state.state)
                    except (ValueError, AttributeError) as e:
                        print(f"Invalid value for {name} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {entity.state} - Error: {e}")
                        continue

                # Get the current timestamp
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # Prepare data to append
                data_to_append = [timestamp, sensor_data1.get("temperature"), sensor_data1.get("humidity"), sensor_data1.get("light")]

                # Print the data to console
                print(f"Data at {timestamp}: {sensor_data1}")

                # Append data to CSV
                append_to_csv(csv_file, data_to_append)

                # Wait for 30 seconds before the next reading
                print("Waiting for 30 seconds...")
                time.sleep(30)
            
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(30)  # Wait before retrying in case of an error

# Flask app setup
app = Flask(__name__)
CORS(app)
dash_app = dash.Dash(__name__, server=app, url_base_pathname='/dashboard/')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sensor-data', methods=['POST'])
def sensor_data1():
    data = request.json
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO sensor_data1 (temperature, humidity, soil_moisture, soil_temperature, light, sound) VALUES (?, ?, ?, ?, ?, ?)',
              (data['temperature'], data['humidity'], data['soil_moisture'], data['soil_temperature'], data['light'], data['sound']))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'})

@app.route('/latest-sensor-values', methods=['GET'])
def latest_sensor_values():
    # Read the latest values from the CSV file
    try:
        df = pd.read_csv('sensor_data1.csv')
        latest_values = df.iloc[-1].to_dict()
        return jsonify(latest_values)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/get-recommendations', methods=['GET'])
def get_recommendations():
    try:
        # Get the latest sensor values
        df = pd.read_csv('sensor_data1.csv')
        latest_values = df.iloc[-1]
        
        temperature = latest_values['temperature']
        humidity = latest_values['humidity']
        sunlight = latest_values['light']

        # Get recommendations based on the latest sensor values
        recommendation = get_plant_care_recommendation(temperature, humidity, sunlight)
        
        # Print the recommendation to the console
        print("Generated Recommendation:", recommendation)
        
        return jsonify({"recommendation": recommendation})
    except Exception as e:
        return jsonify({"error": str(e)})




# Dash layout
dash_app.layout = html.Div([
    dcc.Graph(id='live-update-graph'),
    dcc.Interval(id='interval-component', interval=5*1000, n_intervals=0)
])

@dash_app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    df = pd.read_csv('sensor_data1.csv')
    fig = px.line(df, x='timestamp', y=['temperature', 'humidity', 'light'])
    return fig

# Fix the URL routing for Dash
@app.route('/dashboard/')
def render_dashboard():
    return dash_app.index()

def run_flask_app():
    app.run(debug=True, port  = 5001)

if __name__ == '__main__':
    # Run data collection in a separate thread
    data_thread = threading.Thread(target=retrieve_and_store_data)
    data_thread.daemon = True
    data_thread.start()

    # Run the Flask app
    run_flask_app()
