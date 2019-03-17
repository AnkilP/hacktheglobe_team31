# coding: utf-8

from flask import Flask, render_template, request
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
from interface import interfacing
from quickstart import survey_data

app = Flask(__name__, template_folder="templates")

GoogleMaps(
    app,
    key="AIzaSyDAGTW91aX3qcRnkT1Iq38F0FvLm3jmeEw"
)


@app.route("/")
def fullmap():

    user_number = 1
    skills = []
    survey_response = survey_data()
    interface = interfacing()
    categories = survey_response.get_survey_response(user_number)
    if(categories is not None):
        user_number = user_number + 1
        result = survey_response.get_survey_response(user_number)
        skills_index = categories.index("Please select all that apply to your skill set")
        skills = result[skills_index].split(',')

    
    for skill in skills:
        interface.get_service_information(skill)

    fullmap = Map(
        identifier="fullmap",
        varname="fullmap",
        style=(
            "height:100%;"
            "width:100%;"
            "top:0;"
            "left:0;"
            "position:absolute;"
            "z-index:200;"
        ),
        lat=43.6532,
        lng=79.3832,
        markers=[
            {
                'icon': '//maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 37.4419,
                'lng': -122.1419,
                'infobox': "Hello I am <b style='color:green;'>GREEN</b>!"
            },
            {
                'icon': '//maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': 37.4300,
                'lng': -122.1400,
                'infobox': "Hello I am <b style='color:blue;'>BLUE</b>!"
            },
            {
                'icon': '//maps.google.com/mapfiles/ms/icons/red-dot.png',
                'lat': 37.4300,
                'lng': -122.1390,
                'infobox': "Hello I am <b style='color:red;'>RED</b>!"
            },
        ],
        # maptype = "TERRAIN",
        # zoom="5"
    )
    return render_template(
        'example_fullmap.html',
        fullmap=fullmap,
        GOOGLEMAPS_KEY=request.args.get('apikey')
    )

@app.route('/clickpost/', methods=['POST'])
def clickpost():
    # Now lat and lon can be accessed as:
    lat = request.form['lat']
    lng = request.form['lng']
    print(lat)
    print(lng)
    return "ok"

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
