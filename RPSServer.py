import random
import json
from os import path
import cherrypy
import os

RPSItems = {"Rock": ["Scissors", "Lizard"],
            "Paper": ["Rock", "Spock"],
            "Scissors": ["Paper", "Lizard"],
            "Lizard": ["Paper", "Spock"],
            "Spock": ["Rock", "Scissors"]
            }
Messages = {
    "Tie": "The game resulted in a tie",
    "Human": "You win!",
    "Computer": "You lost to the computer",
    "Invalid": "Invalid input, try again"
}
ValidChoices = ['Rock', 'Paper', 'Scissors']


# def write(toWrite):
#     with open('stats.json', 'w', encoding='utf-8') as f:
#         json.dump(toWrite, f, ensure_ascii=False, indent=4)

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head>
            <style>
                html {
                    font-family: monospace;
                }
                input {
                    font-family: monospace;
                    border-radius: 0 !important;
                    border: 1px solid black !important;
                    padding: 4px;
                    margin-top: 4px;
                }
            </style>
          </head>
          <body>
          <h2>Welcome to Rock, Paper, Scissors, coded by slinkous</h2>
          <hr>
          <form method="get" action="results">
            <label for="name">input your username</label><br>
            <input type="text" name="name" />
            <br><br><br>
            <label for="choice">pick le thing</label><br>
            <div>
            <input type="radio" id="Rock" name="choice" value="Rock" checked>
            <label for="Rock">Rock</label>
            </div>
            <div>
            <input type="radio" id="Paper" name="choice" value="Paper">
            <label for="Paper">Paper</label>
            </div>
            <div>
            <input type="radio" id="Scissors" name="choice" value="Scissors">
            <label for="Scissors">Scissors</label>
            </div>
            <br><br><br>
            <label for="submit">press le button</label><br>
            <button type="submit">submit</button>
          </form>
          </body>
        </html>"""

    @cherrypy.expose
    def results(self, name="nobody", choice='rock'):
        username = name
        # if path.exists('stats.json') is False:
        #     x = {
        #         username: {
        #             "wins": 0,
        #             "ties": 0,
        #             "losses": 0
        #         }
        #     }
        #     write(toWrite=x)
        #
        # with open('stats.json', 'r', encoding='utf-8') as infile:
        #     globalStats = json.load(infile)
        #
        # if username not in globalStats:
        #     globalStats[username] = {
        #         "wins": 0,
        #         "ties": 0,
        #         "losses": 0
        #     }
        #     write(toWrite=globalStats)
        #
        # userStats = globalStats[username]
        # wins = userStats['wins']
        # ties = userStats['ties']
        # losses = userStats['losses']
        # wins = 0
        # ties = 0
        # losses = 0
        playerChoice = choice
        compChoice = random.choice(ValidChoices)
        if playerChoice in compChoice:
            result = 'Tie'
            # ties += 1
        elif compChoice in RPSItems[playerChoice]:
            result = 'Human'
            # wins += 1
        else:
            result = 'Computer'
            # losses += 1
        ChoiceMessage = ('You chose', playerChoice.upper(), "<br>The computer chose", compChoice.upper())
        ResultMessage = (Messages[result])

        # userStats['wins'] = wins
        # userStats['ties'] = ties
        # userStats['losses'] = losses
        #
        # write(toWrite=globalStats)
        return """<html>
          <head>
            <style>
                html {
                    font-family: monospace;
                }
                input {
                    font-family: monospace;
                    border-radius: 0 !important;
                    border: 1px solid black !important;
                    padding: 4px;
                    margin-top: 4px;
                }
            </style>
          </head>
          <body>
          <h2>Rock, Paper, Scissors, coded by slinkous</h2>
          <hr>
          <h2>RESULTS:</h2>
          username: """, name.upper(), """
          <br>
          """, ChoiceMessage, """
          <br>
          """, ResultMessage, """
          <br><br><br>
          all stats:
          <br>
          soon(TM)
          </body>
        </html>"""


conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
    }
cherrypy.server.socket_host = '0.0.0.0'
cherrypy.quickstart(HelloWorld())

print(os.path.abspath(os.getcwd()))
