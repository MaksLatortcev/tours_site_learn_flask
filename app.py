from flask import Flask, render_template
import mock_data as md
from help_functions import get_tours_for_main, get_name_departures, get_tours_departure, get_nights, get_prices

app = Flask(__name__)

@app.route("/")
def main():
    name_departure = get_name_departures(md.departures)
    tours_for_main = get_tours_for_main(md.tours)
    output = render_template("index.html",
                             title=md.title,
                             departures=md.departures,
                             subtitle=md.subtitle,
                             description=md.description,
                             name_departure=name_departure,
                             tours=tours_for_main)

    return output

@app.route("/departures/<departure>/")
def departures(departure):
    name_departure = get_name_departures(md.departures)[departure]
    tours_departure = get_tours_departure(md.tours, departure)
    nights = get_nights(tours_departure)
    prices = get_prices(tours_departure)

    output = render_template("departure.html",
                             title=md.title,
                             departures=md.departures,
                             tours=tours_departure,
                             name_departure=name_departure,
                             nights=nights,
                             prices=prices)
    return output


@app.route("/tours/<id>/")
def tours(id):
    name_departure = get_name_departures(md.departures)
    id = int(id)

    output = render_template("tour.html",
                             title=md.title,
                             departures=md.departures,
                             tours=md.tours,
                             name_departure=name_departure,
                             id=id)
    return output


@app.errorhandler(500)
def internal_error(error):

    output = render_template('500.html',
                             title=md.title,
                             departures=md.departures), 500

    return output

@app.errorhandler(404)
def internal_error(error):

    output = render_template('404.html',
                             title=md.title,
                             departures=md.departures), 404

    return output

app.run()