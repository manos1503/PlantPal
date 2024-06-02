# Code Structure

## Project Structure

APP_DEV/

│

├── app.py # Main application file

│

├── templates/

│ └── index.html # HTML template for the app

│

├── static/

│ └── style.css # CSS for styling the app

│ └── script.js # CSS for dynamic content

## Description
- `app.py`: Main script to run the application. It sets up the Flask server, initializes the database, and defines the routes and endpoints.
- `templates/index.html`: HTML template for the web interface. This file defines the structure of the web page that users interact with.
- `static/style.css`: CSS file for styling the web interface. This file contains the styles that make the web page visually appealing.
- `static/script.js`: avaScript code that adds interactivity, dynamic content, and functionality to the web page.

## Detailed Descriptions

### app.py
The main entry point of the application. It performs the following tasks:
- Imports necessary libraries such as Flask, Dash, Pandas, and SQLite.
- Sets up the Flask app and CORS for handling cross-origin requests.
- Initializes the Dash app for data visualization.
- Defines routes and endpoints for the web application, including the index route and sensor data handling.
- Initializes the database and creates the necessary tables if they do not exist.

- responsible for collecting data from sensors. It performs the following tasks:
- Connects to the sensors and retrieves data on temperature, humidity, and light.
- Formats the collected data and makes it available to the Flask app for further processing and storage.

### templates/index.html
The HTML template for the web interface. It includes:
- The structure of the web page, including elements for displaying sensor data and charts.
- Placeholders for dynamic content that will be filled in by the Flask app.

### static/style.css
The CSS file for styling the web interface. It includes:
- Styles for various HTML elements to ensure a consistent and visually appealing design.
- Custom styles for specific components of the web page, such as charts and data tables.

### static/style.css
This JavaScript file 
- manages data fetching and updates for the web interface. 
- It includes functions to fetch the latest sensor values (temperature, humidity, light) and plant care recommendations, displaying a loading spinner during the fetch, and updating the UI with the results. The data is periodically refreshed to provide real-time updates to the user.

---

By understanding the code structure, users can easily navigate through the project and locate specific files and functionality. This makes it easier to contribute to the project and troubleshoot any issues that may arise.




