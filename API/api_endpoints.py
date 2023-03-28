from flask import Blueprint, Response, request, jsonify, make_response, render_template_string
from flask_restful import Resource, Api
from . import r
import uuid
import json
import requests
import os
from pydo import Client as DO


api_endpoints = Blueprint('api_endpoints', __name__)
api = Api(api_endpoints)

class Login(Resource):
    def post(self):
        login_request_id = str(uuid.uuid4())
        data = request.get_json()
        data = json.loads(data)
        email = data['email']
        token = data['token']
        # r.set(login_request_id + "/email", data["email"])
        # r.set(login_request_id + "/token", token)
        
        do = DO(token = token)
        user = do.account.get(headers = {"Content-Type": "application/json"})
        if user['account']['email'] == email and user['account']['status'] == "active":
            return {"message": "success"}
        

class GetMyAcct(Resource):
    def get(self):
        data = request.get_json()
        data = json.loads(data)
        token = data['token']
        do = DO(token = token)
        user = do.account.get(headers = {"Content-Type": "application/json"})
        return user



class PythonanywhereLogin(Resource):
    def post(self):
        data = request.get_json()
        data = json.loads(data)
        username = data['username']
        token = data['token']
        default_host = 'www.pythonanywhere.com'
        response = requests.get(
            'https://{host}/api/v0/user/{username}/cpu/'.format(
                host=default_host, username=username
            ),
            headers={'Authorization': 'Token {token}'.format(token=token)}
        )
        if response.status_code == 200:
            return {"message": "success"}

class PythonanywhereCreateAlwaysOnTask(Resource):
    def post(self):
        data = request.get_json()
        data = json.loads(data)

        # Set the file path
        file_path = os.getcwd() + "/telegram_setup.zip"

        # Set the file name
        new_file_name = "uploaded_zip_file.zip"

        # Open the file and set the content
        with open(file_path, "rb") as f:
            file_content = f.read()

        # Set the multipart-encoded file with the name "content"
        files = {"content": (new_file_name, file_content)} 

        default_host = 'www.pythonanywhere.com'
        response = requests.post(
            'https://{0}/api/v0/user/{1}/files/path/{2}'.format(
                default_host, data['username'], data['path']
            ), files = files, headers={'Authorization': 'Token {token}'.format(token=data['token'])}
        )

            # Check if the upload was successful
        if response.status_code == 201:
            return response.json()
        elif response.status_code == 200:
            return response.json()
        else:
            return {"message": "failed"}, response.json()

api.add_resource(GetMyAcct, '/myacctinfo')
api.add_resource(Login, '/login')
api.add_resource(PythonanywhereLogin, '/pa_login')
api.add_resource(PythonanywhereCreateAlwaysOnTask, '/createalwaysontask')

