"""Models and database functions for SFMTA Board Resolutions project."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import create_engine, func, between
from sqlalchemy.engine.url import URL
from geoalchemy2 import Geometry

db = SQLAlchemy()


##############################################################################
# Model definitions

class SavedGeometry(db.Model):
    """SFMTA Board Resolutions"""

    __tablename__ = "geometryData"

    geo_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    shape = db.Column(db.String(500), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    latlng = db.Column(Geometry(geometry_type='POINT'), nullable=False)

    def __repr__(self):

        return "<Geo ID=%s>" % (self.geo_id)


##############################################################################
# Helper functions


def connect_to_db(app, db_uri=None):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri or 'postgresql:///geodata'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # state of being able to work with the database directly.

    from server import app

    connect_to_db(app)
    print "Connected to DB."

    # In case tables haven't been created, create them
    db.create_all()
