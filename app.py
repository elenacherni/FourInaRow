from flask import Flask


###### App setup
app = Flask(__name__)

###### Pages


## Game
from pages.game.game import game
app.register_blueprint(game)


## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)
