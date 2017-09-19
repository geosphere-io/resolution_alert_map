"""Map of San Francisco; save pt, line, polygon to db."""

from flask import (Flask,
                  render_template,
                  redirect,
                  request, session,
                  jsonify,
                  g)

import json

import secret_key

from flask_debugtoolbar import DebugToolbarExtension

from model import (SavedGeometry,
                  connect_to_db,
                  db)

# from geojson import (Feature,
#                      Point,
#                      FeatureCollection)

app = Flask(__name__)

JS_TESTING_MODE = False

app.secret_key = secret_key.flask_secret_key


@app.route('/')
def index():
    """Landing page"""

    return render_template("homepage.html")

@app.route('/save_geometry.json')
def save_geometry():
    """Save geometry to database"""

    name = request.args.get("name")
    shape = request.args.get("shape")
    coordinates = json.loads(request.args.get("coordinates"))

    # Each field in the db takes either a point, line, or polygon shape
    if shape == "Point":
      point_ = 'POINT({} {})'.format(coordinates[1], coordinates[0])
      line_ = None
      polygon_ = None
    
    elif shape == "LineString":
      coord_string = stringify_coords(coordinates)

      line_ = 'LINESTRING({})'.format(coord_string)
      point_=None
      polygon_=None
    
    elif shape == "Polygon":
      coord_string = "("+stringify_coords(coordinates[0])+")"

      polygon_ = 'POLYGON({})'.format(coord_string)
      point_=None
      line_=None
    
    else:
      print("put in error handler")

    geometry = SavedGeometry(name=name,
                             shape=shape,
                             point_=point_,
                             line_=line_,
                             polygon_=polygon_)

    db.session.add(geometry)
    db.session.commit()

    print "******************", name, "**************"
    print "******************", shape, "**************"
    # print "******************", type(geo_coords), "**************"
    # print "******************", geo_coords, "**************"
    # print "******************", coord_string, "**************"


    return redirect("/")

#############HELPER FUNCTIONS########################################

def stringify_coords(coordinates):
    coord_string = ""
    
    for pair in coordinates:
        latlng_pair = '{} {}, '.format(pair[1], pair[0])
        coord_string += latlng_pair

    coord_string = coord_string.rstrip(", ")

    return coord_string


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host='0.0.0.0')
