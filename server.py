import json
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    flash,
    url_for,
    make_response,
)
from datetime import datetime


def loadClubs():
    with open("clubs.json") as c:
        listOfClubs = json.load(c)["clubs"]
        return listOfClubs


def loadCompetitions():
    with open("competitions.json") as comps:
        listOfCompetitions = json.load(comps)["competitions"]
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = "something_special"


competitions = loadCompetitions()
clubs = loadClubs()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/showSummary", methods=["POST"])
def showSummary():
    email = request.form["email"]
    matching_clubs = [club for club in clubs if club["email"] == email]

    if matching_clubs:
        club = matching_clubs[0]
        flash("Email found", "success")
        return make_response(
            render_template("welcome.html", club=club, competitions=competitions), 200
        )
    else:
        flash("Wrong email", "error")
        return make_response(render_template("index.html"), 400)


@app.route("/book/<competition>/<club>")
def book(competition, club):
    foundClub = [c for c in clubs if c["name"] == club][0]
    foundCompetition = [c for c in competitions if c["name"] == competition][0]
    if foundClub and foundCompetition:
        return make_response(
            render_template(
                "booking.html", club=foundClub, competition=foundCompetition
            ),
            200,
        )
    else:
        flash("Something went wrong-please try again", "error")
        return make_response(
            render_template("welcome.html", club=club, competitions=competitions), 400
        )


@app.route("/purchasePlaces", methods=["POST"])
def purchasePlaces():
    club_request = request.form["club"]
    competition_request = request.form["competition"]

    matching_club = [c for c in clubs if c["name"] == club_request]
    matching_competition = [
        comp for comp in competitions if comp["name"] == competition_request
    ]

    if not matching_club or not matching_competition:
        flash("ERROR: No matching club or matching competition", "error")
        return make_response(render_template("index.html"), 404)

    club = matching_club[0]
    competition = matching_competition[0]
    competition_date = datetime.strptime(competition["date"], "%Y-%m-%d %H:%M:%S")
    if competition_date < datetime.now():
        flash("Error: Competition is in the past.", "error")
        return make_response(
            render_template("welcome.html", club=club, competitions=competitions), 400
        )

    places_required = int(request.form["places"])
    places_availables = int(competition["numberOfPlaces"]) - places_required
    remaining_points = int(club["points"]) - places_required

    error_message, category = validate_booking(
        places_required, places_availables, remaining_points
    )
    if error_message:
        flash(error_message, category)
        return make_response(
            render_template("welcome.html", club=club, competitions=competitions), 400
        )
    else:
        club["points"] = remaining_points
        competition["numberOfPlaces"] = places_availables
        flash(f"Great booking complete! {places_required} purchased!", "success")
    return make_response(
        render_template("welcome.html", club=club, competitions=competitions), 200
    )


def validate_booking(places_required, places_availables, remaining_points):

    if places_required > 12:
        return "Error : Too many places requested", "error"
    elif places_availables < 0:
        return "Error: Not enough places!", "error"
    elif remaining_points < 0:
        return "Error : Not enough points", "error"
    else:
        return None, "success"


@app.template_filter("to_datetime")
def to_datetime_filter(value):
    return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")


@app.context_processor
def inject_datetime():
    return {"datetime": datetime}


@app.route("/leaderboard", methods=["GET"])
def leaderboard():
    sorted_clubs = sorted(clubs, key=lambda club: int(club["points"]), reverse=True)

    return make_response(render_template("leaderboard.html", clubs=sorted_clubs), 200)


@app.route("/logout")
def logout():
    return redirect(url_for("index"))
