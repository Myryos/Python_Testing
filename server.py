import json
from flask import Flask,render_template,request,redirect,flash,url_for, abort



def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'



competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def showSummary():
    email = request.form['email']
    matching_clubs = [club for club in clubs if club['email'] == email]

    if matching_clubs:
        club = matching_clubs[0]
        return render_template('welcome.html', club=club, competitions=competitions), 200
    else:
        flash('Wrong email', 'error')
        return render_template('index.html')


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again", 'error')
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    club_request = request.form['club']
    competition_request = request.form['competition']

    matching_club = [c for c in clubs if c['name'] == club_request]
    matching_competition = [comp for comp in competitions if comp['name'] == competition_request]

    club = None
    competition = None

    if matching_club:
        club = matching_club[0]
    if matching_competition:
        competition = matching_competition[0]
   
    places_required = int(request.form['places'])
    places_availables= int(competition['numberOfPlaces'])-places_required
    cost_in_points = int(club['points']) - places_required

    if cost_in_points < 0:
        flash('Error : Not enough points', 'error')
    else :
        club['points'] =  cost_in_points
        competition['numberOfPlaces'] = places_availables
        flash(f'Great booking complete! {places_required} purchased!', 'success')
    return render_template('welcome.html', club=club, competitions=competitions)



# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))