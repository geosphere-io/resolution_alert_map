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

    __tablename__ = "geodata"

    geo_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    shape = db.Column(db.String(500), nullable=False)
    # latitude = db.Column(db.Float, nullable=False)
    # longitude = db.Column(db.Float, nullable=False)
    point_ = db.Column(Geometry(geometry_type='POINT'))
    line_ = db.Column(Geometry(geometry_type='LINESTRING'))
    polygon_ = db.Column(Geometry(geometry_type='POLYGON'))

    def __repr__(self):

        return "<Geo ID=%s Shape=%s>" % (self.geo_id, self.shape)


class User(db.Model):
    """SFMTA Board Resolutions -- Users"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):

        return "<Username=%s ID=%s>" % (self.username, self.user_id)

##############################################################################
# Sample data

def sample_data():
    """Test data to configure database"""

    first = SavedGeometry(geo_id=1,name="first",shape="point",point_='POINT(37.498 -112.4324)')
    second = SavedGeometry(geo_id=2,name="second",shape="line",line_='LINESTRING(37.498 -112.4324,37.568 -112.423)')
    third = SavedGeometry(geo_id=3,name="third",shape="polygon",polygon_='POLYGON((37.498 -112.4324,37.568 -112.423,37.534 -112.469,37.498 -112.4324))')

    db.session.add_all([first, second, third])

    db.session.commit()
##############################################################################
# Helper functions


def connect_to_db(app, db_uri=None):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri or 'postgresql:///resolutions'
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
