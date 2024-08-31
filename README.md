# MIT xPRO - Module 16 Final Project

This project demonstrates the integration of Mapbox GL JS with a Flask backend that fetches real-time data from the MBTA API. The application displays vehicle locations on a Mapbox map, which is updated every 5 seconds.

## Project Structure

- `index.html`: The frontend of the application, which includes the Mapbox GL map and JavaScript to fetch and display vehicle data.
- `main.py`: The backend Flask application that fetches vehicle data from the MBTA API and serves it to the frontend.
- `requirements.txt`: A list of Python dependencies required to run the Flask application.

## Installation

### Prerequisites

- Python 3.7 or higher
- A Mapbox account with an access token
- Flask and Flask-CORS installed (defined in `requirements.txt`)

### Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required Python packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your `.env` file** (if using environment variables):
    Set the "mapboxgl.accessToken" in your view:
    ```env
    mapboxgl.accessToken=your_mapbox_access_token_here
    ```

5. **Run the Flask application**:
    ```bash
    python main.py
    ```

6. **Open the application**:
    - Open `index.html` in your browser to see the map and the real-time vehicle data.

## File Descriptions

### `index.html`

- This file contains the HTML, CSS, and JavaScript to display a Mapbox map and dynamically add markers representing vehicle locations.
- It includes the Mapbox GL JS library and uses a `setTimeout` loop to update the map markers every 5 seconds with new data fetched from the Flask backend.

### `main.py`

- A Flask application that serves as the backend for the project.
- The `/getTransportData` route fetches data from the MBTA API, filters it to include only vehicle `id`, `latitude`, and `longitude`, and then serves this data to the frontend.
- CORS (Cross-Origin Resource Sharing) is enabled using `Flask-CORS` to allow the frontend to make requests to the Flask server.

### `requirements.txt`

- Lists all the Python dependencies required to run the Flask application. Use `pip install -r requirements.txt` to install them.

## Usage

1. **Run the Flask server** using the command provided above.
2. **Open the `index.html` file** in your web browser.
3. The map will display real-time data from the MBTA API, updating every 5 seconds to reflect the current locations of vehicles.

## Customization

- **Mapbox Style**: You can customize the map style by editing the `style` property in the `index.html` file.
- **Data Source**: The backend fetches data from the MBTA API, but you can modify the `get_transport_data()` function in `main.py` to fetch data from a different source.

## Troubleshooting

- **CORS Errors**: Ensure that Flask-CORS is properly installed and that the Flask server is running on `localhost` as expected.
- **Mapbox Token**: Ensure that your Mapbox token is correct and has the necessary permissions.
