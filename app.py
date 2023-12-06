from flask import Flask, jsonify, request
import json
from social_network import *
from test import *

app = Flask(__name__)

#print(socialNetwork.getUsers())

@app.route("/users")
def getUsers():
    users = socialNetwork.getUsers()
    response = json.dumps(users)
    #print(response)
    return jsonify({'users': users}), 200

@app.post('/login')
def login():
    data = request.get_json()
    userType = data['type']
    if data['type'] == 'Person':
        response = socialNetwork.addPerson(data['username'], data['name'], data['age'])
    elif data['type'] == 'Organization':
        response = socialNetwork.addOrganization(data['username'], data['name'])
    else:
        response = False

    if response:
        return jsonify({'success': response}), 200
    return jsonify({'success': response}), 200