import json
from flask import request, Blueprint, render_template
import webserver.graph
import webserver.forms.upload

bp = Blueprint("home", __name__, url_prefix="/")


@bp.route("/", methods=["GET", "POST"])
def homepage():
    """
    Method that defines the main web-app route, in case of a GET request, the server returns the homepage

    If the server receives a POST request with the required JSON file, the server returns the visualization page
    :return: Appropriate route given the request method and if the required parameters are present (JSON file)
    """

    form = webserver.forms.upload.UploadForm()
    if request.method == "POST":
        # POST request submitted without the json field
        if "json" not in request.files:
            return "error"
        json_file = request.files["json"]
        # POST request submitted with an empty JSON field
        if json_file.filename == "":
            return "error"
        # retrieving the set from the JSON file
        parsed = json.loads(json_file.read())
        # generation of the graphs
        html = webserver.graph.make_graphs(parsed)
        # Visualization page
        return render_template("viz.html", parsed=parsed, graphs=html)
    # Homepage of the site
    return render_template("home.html", form=form)
