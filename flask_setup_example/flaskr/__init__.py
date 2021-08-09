from flask import Flask, jsonify
from .model import setup_db, Plant
from flask_cors import CORS, cross_origin


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    #CORS(app, resources={r"*/api/*" : {origins: '*'}})
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTION')
        return response

    #@cross_origin
    @app.route('/plants')
    def get_plants():
       plants = Plant.query.all()
       formatted_plants = [plant.format() for plant in plants]
       return jsonify({
            'success': True,
            'plants':formatted_plants
            })
    return app