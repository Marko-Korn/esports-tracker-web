# esports-tracker-web
This is a Flask-based web application that tracks upcoming and past esports tournaments and matches using the PandaScore API. The application allows users to view details of tournaments and matches for various games, including sorting functionality for the matches.

## Features

- Display upcoming esports tournaments.
- Display upcoming and past esports matches.
- Sort matches by date or by game.
- View details such as start and end dates, game name, and winner for past matches.

## Technologies Used

- Python
- Flask
- HTML
- Bootstrap
- PandaScore API

## Routes

- `/` - Homepage displaying upcoming tournaments.
- `/matches` - Page displaying upcoming matches with sorting options.
- `/past_matches` - Page displaying past matches with sorting options and match winners.
- `/tournaments/<game>` - Page displaying tournaments for a specific game.

## Preview
![main](https://github.com/Marko-Korn/esports-tracker-web/assets/9790303/c1e18bb1-1630-496d-ac4e-b103dfa4848e)
![past_matches](https://github.com/Marko-Korn/esports-tracker-web/assets/9790303/e2c76107-9f6e-4482-b105-2458d104d75d)
![upcoming_matches](https://github.com/Marko-Korn/esports-tracker-web/assets/9790303/7fac7ad5-e6f5-4a8d-adec-49fc12a3a2c1)

## Acknowledgements

- [PandaScore API](https://pandascore.co/) for providing esports data.
- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [Bootstrap](https://getbootstrap.com/) for the UI components.
