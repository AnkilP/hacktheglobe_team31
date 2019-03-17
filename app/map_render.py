# coding: utf-8

from flask import Flask, render_template, request
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
from quickstart import survey_data
from IndexComputer import IndexComputer

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
    interface = IndexComputer()
    categories = [x.encode('utf8', 'replace') for x in survey_response.get_survey_responses(user_number)]
    if(categories is not None):
        user_number = user_number + 1
        result = [x.encode('utf8', 'replace') for x in survey_response.get_survey_responses(user_number)]
        skills_index = categories.index("Please select all that apply to your skill set")
        skills = result[skills_index].split(',')

    locations = []
    for skill in skills:
        locationlist = interface.ComputeIndex(skill)
        city_list = [x.City for x in locationlist]
        indexList = [float(x.index) for c in locationlist]
        city_list, indexList = (list(t) for t in zip(*sorted(zip(city_list, indexList))))
        locations.append(city_list[0])
        locations.append(city_list[1])
        locations.append(city_list[2])

    locations = sorted(set(locations))[0:2]

    # Geocoding an address
    lat_locations = []
    for i in locations:
        lat_locations.append(GoogleMaps.geocode(i))

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
                'lat': lat_locations[0][0],
                'lng': lat_locations[0][1],
                'infobox': "Hello I am <b style='color:green;'>GREEN</b>!"
            },
            {
                'icon': '//maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': lat_locations[1][0],
                'lng': lat_locations[1][1],
                'infobox': "Hello I am <b style='color:blue;'>BLUE</b>!"
            },
            {
                'icon': '//maps.google.com/mapfiles/ms/icons/red-dot.png',
                'lat': lat_locations[2][0],
                'lng': lat_locations[2][1],
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
