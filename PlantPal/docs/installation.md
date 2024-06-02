# Installation

## System Requirements
- **Operating System:** Windows 10/11, macOS, or Linux
- **Python:** Version 3.8 or higher

## Steps to Install

1. **Clone the Repository**
   ```sh
   git clone <repository-url> 
   ```

2. **Navigate to the Project Directory**
    ```sh
    cd APP_DEV
    ```


3. **Install Dependencies**
    Install the required Python packages using pip. Create a requirements.txt file in your project root if it doesn't already exist, and include the following dependencies:
    ```sh
        flask
        flask-cors
        dash
        plotly
        pandas
        sqlite3
        csv
    ```

   Then run:
   ```sh
    pip install -r requirements.txt
    ```



4. **Run Database Migrations (if applicable)**

    If your project uses a database, you may need to set it up. Based on the app.py file, your database setup is handled within the script. Ensure the database is initialized by running the application.

5. **Start the Application**

    Finally, start the application. The command may vary depending on your project setup. For your Flask app, you can typically start it with:
    ```sh
    flask run
    ```
    or directly using Python:
    ```sh
    python app.py
    ```
6. **Access the Application**

    Open a web browser and go to http://localhost:5001 to see the app in action.


