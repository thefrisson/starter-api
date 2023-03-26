from flask import Blueprint, Response, request, jsonify, make_response, render_template_string
from flask_restful import Resource, Api
from . import r
import uuid
from pydo import Client as DO


api_endpoints = Blueprint('api_endpoints', __name__)
api = Api(api_endpoints)

class Login(Resource):
    def post(self):
        login_request_id = str(uuid.uuid4())
        data = request.get_json()
        token = data['token']
        r.set(login_request_id + "/email", data["email"])
        r.set(login_request_id + "/token", token)
        
        do = DO(token = token)
        user = do.account.get(headers = {"Content-Type": "application/json"})
        return user





api.add_resource(Login, '/login')

