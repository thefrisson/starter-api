from flask import Blueprint, Response, request, jsonify, make_response, render_template_string
from flask_restful import Resource, Api
from .models import User
from . import db


api_endpoints = Blueprint('api_endpoints', __name__)
api = Api(api_endpoints)

class HelloWorld(Resource):
    def get(self):
        return render_template_string("Hello World!")

class HealthCheck(Resource):
    def get(self):
        return Response(status=200)

api.add_resource(HelloWorld, '/')
api.add_resource(HealthCheck, '/check')
