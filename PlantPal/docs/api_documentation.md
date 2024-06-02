# API Documentation

## Endpoints

### GET /api/sensors
- **Description:** Retrieves the latest sensor data.
- **Parameters:** None
- **Example Response:**
  ```json
  {
    "temperature": 22.5,
    "humidity": 45,
    "light": 40000
  }

### POST /api/sensors
- **Description:** Updates the sensor data.
- **Parameters:** 

    -temperature (float): New temperature value

    -humidity (float): New humidity value

   -light (int): New light value
- **Example Request:**
 ```json
  {
    
  "temperature": 23.0,
  "humidity": 50,
  "light": 45000
  }
  ```

- **Example Response:**
```json
{
  "status": "success",
  "message": "Sensor data updated successfully."
}
```

## Detailed Descriptions

### GET /api/sensors

**This endpoint retrieves the latest sensor data from the database. The data includes temperature, humidity, and sunlight values.**

**Response:** 

-temperature (float): The new temperature value in degrees Celsius.

-humidity (float): The new humidity percentage.

-light (int): The new light level in lux.

**Response:** 

-status (string): Indicates success or failure of the operation.

-message (string): A message describing the outcome of the operation.


