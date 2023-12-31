from flask import Flask, jsonify, request
from flask_cors import CORS
from src.social_network.social_network import *
from src.initialization.default_accounts import *

socialNetwork = SocialNetwork()
createUsers(socialNetwork)

app = Flask(__name__)
CORS(app)

@app.route('/')
def health():
    return jsonify({'status': 'Ok!'}), 200

@app.route('/users')
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
def getUserCenteredGraph(username):
    graph = socialNetwork.getUserCenteredGraph(username)
    if not graph:
        return jsonify({'success': False}), 400

    nodes = list(graph['distance'].keys())
    edges = []
    for node in list(graph['connections'].keys()):
        for edge in graph['connections'][node]:
            edges.append({'source': node, 'target': edge})
    
    response = {'nodes': nodes, 'edges': edges, 'distances': graph['distance']}
    return jsonify(response), 200


@app.get('/social-network-graph')
def getSocialNetworkGraph():
    return socialNetwork.getSocialNetworkGraph()


@app.put('/user-info-visibility')
def changeInfoVisibility():
    data = request.get_json()
    username = data['username']
    field = data['field']

    user = socialNetwork.getUserValues(username)
    response = user.changeInfoVisibility(field)

    if response:
        return jsonify({'success': response}), 200



@app.get('/user-info-visibility/<username>')
def getInfoVisibility(username):
    user = socialNetwork.getUserValues(username)
    response = user.getInfoVisibility()

    if response:
        return jsonify({'infoVisibility': response}), 200
    return jsonify({'success': response}), 400
    