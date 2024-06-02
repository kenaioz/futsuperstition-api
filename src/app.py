from flask import Flask, json
from werkzeug.exceptions import HTTPException

from database.config import Config
from database.connection import db

from src.routes.pong import ping
from src.routes.jerseys import jerseys
from src.routes.stadiums import stadiums


def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.json.sort_keys = False

    blueprints = [ping, jerseys, stadiums]

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    app.config.from_object(Config)
    db.init_app(app)

    @app.errorhandler(HTTPException)
    def handle_exception(e):
        response = e.get_response()
        response.data = json.dumps(
            {
                "error": {
                    "code": e.code,
                    "name": e.name,
                    "description": e.description,
                }
            }
        )
        print(response.data)
        response.content_type = "application/json"
        return response

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
