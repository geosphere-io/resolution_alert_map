"""Map of San Francisco; save pt, line, polygon to db."""

from flask import (Flask,
                   render_template,
                   redirect,
                   request, session,
                   jsonify,
                   g)

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

    if shape == "point":
      geometry = SavedGeometry(name=name,
                               shape=shape,
                               point_='POINT(37.498 -112.4324)')
    elif shape == "line":
      geometry = SavedGeometry(name=name,
                               shape=shape,
                               line_='LINESTRING(37.498 -112.4324,37.568 -112.423)')
    elif shape == "polygon":
      geometry = SavedGeometry(name=name,
                               shape=shape,
                               polygon_='POLYGON((37.498 -112.4324,37.568 -112.423,37.534 -112.469,37.498 -112.4324))')
    else:
      print "put in error handler"

    db.session.add(geometry)

    db.session.commit()

    print "******************", name, "**************"
    print "******************", shape, "**************"

    return redirect("/")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host='0.0.0.0')
