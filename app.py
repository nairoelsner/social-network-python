from flask import Flask, jsonify, request
import json
from social_network import *
from test import *

app = Flask(__name__)

@app.route("/users")
def getUsers():
    users = socialNetwork.getUsers()
    return jsonify({'users': users}), 200


@app.post('/login')
def login():
    data = request.get_json()
    username = data['username']
    userInfo = socialNetwork.getUserValues(username).getAllInfo()

    if userInfo:
        return jsonify(userInfo), 200
    return jsonify({'success': False,}), 400


@app.post('/register')
def register():
    data = request.get_json()
    userType = data['type'].lower()
    if userType == 'person':
        response = socialNetwork.addPerson(data['username'], data['name'], data['age'])
    elif userType == 'organization':
        response = socialNetwork.addOrganization(data['username'], data['name'])
    else:
        response = False

    if response:
        return jsonify({'success': response}), 200
    return jsonify({'success': response}), 400


@app.get('/user/<username>')
def getUser(username):
    response = socialNetwork.getUser(username)

    if response:
        return jsonify(response), 200
    return jsonify({'success': False}), 400


@app.post('/search')
def search():
    data = request.get_json()
    username = data['username']
    searchTerm = data['searchTerm']
    response = socialNetwork.search(username, searchTerm)
    return jsonify({'results': response}), 200


@app.post('/add-relation')
def addRelation():
    data = request.get_json()
    username1 = data['username1']
    username2 = data['username2']
    relationType = data['type'].lower()

    print(relationType)
    response = socialNetwork.addRelation(username1, username2, relationType)
    if response:
        return jsonify({'results': response}), 200
    return jsonify({'success': False}), 400


@app.get('/user-centered-graph/<username>')
def getGraph(username):
    response = socialNetwork.getUserCenteredGraph(username)
    if response:
        return jsonify(response), 200
    return jsonify({'success': response}), 400