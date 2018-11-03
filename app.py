#  import Flask
from flask import Flask

#  Create an app, being sure to pass __name__
app = Flask(__name__)


# 1. Define what to do when a user hits the index route
@app.route("/api/v1.0/precipitation")
def home():
    print("Query for the dates and temperature observations from the last year.")
    print("Convert the query results to a Dictionary using `date` as the key and `tobs` as the value.")
    print("Return the JSON representation of your dictionary.")
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"

# 2. Define what to do when a user hits the index route
@app.route("/api/v1.0/stations")
def stations():
    print(" Return a JSON list of stations from the dataset.")
    return "Welcome to my 'Home' page!"

# 3. Define what to do when a user hits the index route
@app.route("/api/v1.0/tobs")
def temps():
    print(" Return a JSON list of Temperature Observations (tobs) for the previous year.")
    return "Welcome to my 'Home' page!"

# 4. Define what to do when a user hits the index route
@app.route("/api/v1.0/<start>")
def start_vac():
    print(" * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range..")
    print("When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date..")
    print("When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive")
    return "Welcome to my 'Home' page!"

# 5. Define what to do when a user hits the index route
@app.route("/api/v1.0/<start>/<end>")
def startvac_endvac():
    print("Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.")
    print("When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.")
    print("* When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.Query for the dates and temperature observations from the last year.")
    return "Welcome to my 'Home' page!"

if __name__ == "__main__":
    app.run(debug=True)
