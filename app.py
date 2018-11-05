import numpy as np
import datetime as dt
#########################################
#  ORM
#########################################
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)
#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# 1 Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")

    return (
        f"Welcome to Vacation Weather Predictions 'Home' page!<br/>"
        f"/about <br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/start_dateYYYY-MM-DD <br/>" 
        f"/api/v1.0/start_end_dateYYYY-MM-DD "  
    )

# 2. Define what to do when a user hits the /about route
@app.route("/about")
def about():
    author = "Jeff Olson"
    location = "Minneapolis-St.Paul, Minnesota"
    print("Server received request for 'About' page...<br/>")
    return (
        f"Author: {author} Location: {location}"
        f"Check the weather in Hawaii before your vacation"
        )

# 3. Define what to do when a user hits precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for 'Precipitation' page...<br/>")
    session2=Session(engine)
        # Calculate the date 1 year ago from today
    year_ago = dt.date.today() - dt.timedelta(days=365)
    print(year_ago)
    activity=func.avg(Measurement.prcp)
    sel = [Measurement.date, 
       Measurement.prcp]
    # Perform a query to retrieve the data and precipitation scores
    precip_twelve_mo =session2.query(*sel).filter(Measurement.date > '2016-08-23' ).group_by(Measurement.date).order_by(Measurement.date.desc()).all()
    
    return jsonify(precip_twelve_mo)

# 2. Define what to do when a user hits the index route
@app.route("/api/v1.0/stations")
def stations():
    print(" Return a JSON list of stations from the dataset.")
    session3=Session(engine)
    activity=func.count(Measurement.prcp)
    sel = [Measurement.station, Station.name, activity]
    results=[]
    for row in session3.query(*sel).filter(Measurement.station == Station.station).group_by(Measurement.station).order_by(activity.desc()).all():
     #session.query(*sel).group_by(Measurement.station).order_by(activity.desc()).first():
        results.append(row)

    return jsonify(results)

# 3. Define what to do when a user hits the index route
@app.route("/api/v1.0/tobs")
def temps():
    print(" Return a JSON list of Temperature Observations (tobs) for the previous year.<br/>")
    session4=Session(engine)
    activity=func.avg(Measurement.tobs)
    sel = [Measurement.date,Measurement.station, Station.name, activity]
    results=[]
    for row in session4.query(*sel).filter(Measurement.station == Station.station).filter(Measurement.date > '2016-08-23').group_by(Measurement.station).order_by(activity.desc()).all():
        results.append(row)
     #session.query(*sel).group_by(Measurement.station).order_by(activity.desc()).first():
    results
    return jsonify(results)

# 4. Define what to do when a user hits the index route
@app.route("/api/v1.0/start_dateYYYY-MM-DD")
def calc_temps_start():
    # User defined dates.
    session5=Session(engine)
    start_date = '2016-08-23' #'2015-02-28'
   
    # Returns TMIN, TAVG, and TMAX for a list of dates.
    results = session5.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_date).all()

    #print(calc_temps('2017-01-03', '2017-01-14'))
    return jsonify(results)

# 5. Define what to do when a user hits the index route
@app.route("/api/v1.0/start_end_dateYYYY-MM-DD")
def calc_temps():
    print("Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.<br/>")
    print("When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.<br/>")
    print("* When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.Query for the dates and temperature observations from the last year.<br/>")
    session6=Session(engine)
    # Args:
    start_date = '2017-01-03' #'2015-02-28'
   # query_start_date = dt.date(str(start_date)) - dt.timedelta(days=365)
    end_date = '2017-01-14'#'2015-04-05'
    #query_end_date = dt.date(str(end_date) - dt.timedelta(days=365)

    # Returns TMIN, TAVG, and TMAX for a list of dates.
    results = session6.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

    print(calc_temps('2017-01-03', '2017-01-14'))
    return fjsonify(results)

if __name__ == "__main__":
    app.run(debug=True)