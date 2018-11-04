# import Flask
from flask import Flask, jsonify

# Create an app, being sure to pass __name__
app = Flask(__name__)

#hello_dict = {"Hello":"World"}

# Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")

    return (
        f"Welcome to Vacation Weather Predictions 'Home' page!<br/>"
        f"/about <br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/start_date/<start> <br/>" 
        f"/api/v1.0/start_end_date/<start><end> "
        
        
    )

# 4. Define what to do when a user hits the /about route
@app.route("/about")
def about():
    author = "Jeff Olson"
    location = "Minneapolis-St.Paul, Minnesota"
    print("Server received request for 'About' page...<br/>")
    return f"Author: {author} Location: {location}"

# 1. Define what to do when a user hits the index route
@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for 'Precipitation' page...<br/>")
    return "Precipitations for selected vacation dates is<br/>"
# 2. Define what to do when a user hits the index route
@app.route("/api/v1.0/stations")
def stations():
    print(" Return a JSON list of stations from the dataset.")
    return "List of weather stations"

# 3. Define what to do when a user hits the index route
@app.route("/api/v1.0/tobs")
def temps():
    print(" Return a JSON list of Temperature Observations (tobs) for the previous year.<br/>")
    return "Returns the list of observed temperatures"

# 4. Define what to do when a user hits the index route
@app.route("/api/v1.0/start_date/<start>")
def start_vac():
    print(" * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range..<br/>")
    print("When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.<br/>")
    print("When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive <br/>")
    return "Weather statistics for a single date"

# 5. Define what to do when a user hits the index route
@app.route("/api/v1.0/start_end_date/<start>/<end>")
def start_endvac():
    print("Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.<br/>")
    print("When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.<br/>")
    print("* When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.Query for the dates and temperature observations from the last year.<br/>")
    return "Weather statistics for a date range"

if __name__ == "__main__":
    app.run(debug=True)