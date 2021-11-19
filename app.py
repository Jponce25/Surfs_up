# import the Flask dependency, add the following to your code

import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Set Up the Database
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

from flask import Flask, jsonify

# Create a New Flask App Instance
app = Flask(__name__)

# Create Flask Routes
@app.route("/")
def welcome():
    return(
    f'Welcome to the Climate Analysis API!'
    f'Available Routes:'
    f'/api/v1.0/precipitation'
    f'/api/v1.0/stations'
    f'/api/v1.0/tobs'
    f'/api/v1.0/temp/start/end'
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

if __name__ == "__main__":
    app.run(debug=True)