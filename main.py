import datetime
import pytz
from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

API_KEY = os.environ['API_KEY']
API_URL = f'https://api.pandascore.co/tournaments/upcoming?token={API_KEY}'
API_MATCHES_URL = f'https://api.pandascore.co/matches/upcoming?token={API_KEY}'
API_PAST_MATCHES_URL = f'https://api.pandascore.co/matches/past?token={API_KEY}'
LOCAL_TIMEZONE = 'Europe/Helsinki'  # Change this to your local timezone


@app.route('/')
def index():
    response = requests.get(API_URL)
    tournaments = response.json() if response.status_code == 200 else []

    games = {tournament['videogame']['name'] for tournament in tournaments}

    game_images = {
        'LoL': 'lol.png',
        'Valorant': 'valorant.jpg',
        'Dota 2': 'dota.png',
        'EA Sports FC': 'fc.jpg',
        'Mobile Legends: Bang Bang': 'mobile.jpg',
        'Rainbow 6 Siege': 'rainbow.jpg',
        'Counter-Strike': 'cs.png'
    }

    return render_template('index.html', tournaments=tournaments, games=games, game_images=game_images)


@app.route('/matches')
def upcoming_matches():
    sort_by = request.args.get('sort_by', 'date')
    response = requests.get(API_MATCHES_URL)
    matches = response.json() if response.status_code == 200 else []

    # Format dates
    for match in matches:
        match['formatted_begin_at'] = format_date(match.get('begin_at'))
        match['formatted_end_at'] = format_date(match.get('end_at'))

    # Sort matches
    if sort_by == 'game':
        matches.sort(key=lambda x: (x['videogame']['name'] or '').lower())
    else:  # Default sort by date
        matches.sort(key=lambda x: x['begin_at'] or '')

    return render_template('matches.html', matches=matches, sort_by=sort_by)


@app.route('/past_matches')
def past_matches():
    sort_by = request.args.get('sort_by', 'date')
    response = requests.get(API_PAST_MATCHES_URL)
    matches = response.json() if response.status_code == 200 else []

    # Format dates and get winner information
    for match in matches:
        match['formatted_begin_at'] = format_date(match.get('begin_at'))
        match['formatted_end_at'] = format_date(match.get('end_at'))
        match['winner'] = match['winner']['name'] if match.get('winner') else 'No winner data'

    # Sort matches
    if sort_by == 'game':
        matches.sort(key=lambda x: (x['videogame']['name'] or '').lower())
    else:
        matches.sort(key=lambda x: x['begin_at'] or '')

    return render_template('matches.html', matches=matches, past=True, sort_by=sort_by)


@app.route('/tournaments/<game>')
def tournaments_by_game(game):
    response = requests.get(API_URL)
    tournaments = response.json() if response.status_code == 200 else []

    # Filter tournaments by game
    game_tournaments = [tournament for tournament in tournaments if
                        tournament['videogame']['name'].lower() == game.lower()]

    # Format dates
    for tournament in game_tournaments:
        tournament['formatted_begin_at'] = format_date(tournament.get('begin_at'))
        tournament['formatted_end_at'] = format_date(tournament.get('end_at'))

    return render_template('tournaments.html', tournaments=game_tournaments, game=game)


def format_date(date_string):
    if date_string:
        utc_dt = datetime.datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')
        utc_dt = utc_dt.replace(tzinfo=pytz.utc)
        local_dt = utc_dt.astimezone(pytz.timezone(LOCAL_TIMEZONE))
        formatted_date = local_dt.strftime('%d.%m.%Y %H:%M')
        return formatted_date
    else:
        return ''


if __name__ == '__main__':
    app.run(debug=True)
