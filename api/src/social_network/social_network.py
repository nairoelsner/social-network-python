from ..data_structures.graph import *
from ..social_network.user import *

class SocialNetwork(Graph):
    def __init__(self):
        super().__init__()
        self.__personsQty = 0
        self.__organizationsQty = 0
        self.enumRelationFunctions = {
            'friendship': self.__addFriendship,
            'relative': self.__addRelative,
            'follow': self.__addFollow,
            'acquaintance': self.__addAcquaintance,
            'client': self.__addClient
        }

    def getUsersQty(self) -> int:
        return self.__personsQty + self.__organizationsQty
    
    def userExists(self, username: str) -> bool:
        return username in self.getVerticesKeys()
    
    def getAllUsernames(self) -> list:
        return self.getVerticesKeys()
    
    def getUsers(self) -> dict:
        userVertices = self.getVerticesValues() 
        users = []
        for userVertex in userVertices:
            userConnectionTypes = list(userVertex.getConnections().keys())
            connections = {}
            for key in userConnectionTypes:
                connections[key] = list(userVertex.getConnections()[key].keys())
            users.append({'info': userVertex.getValue().getInfo(), 'connections': connections})
        return users
    
    def getUser(self, username: str) -> dict:
        if not self.userExists(username):
            return False
        
        userVertex = self.getUserVertex(username)
        userConnectionTypes = list(userVertex.getConnections().keys())
        connections = {}
        for key in userConnectionTypes:
            connections[key] = list(userVertex.getConnections()[key].keys())
        user = {'info': userVertex.getValue().getInfo(), 'connections': connections}
        return user
        
    def getUserVertex(self, username: str) -> Vertex:
        return self.getVertex(username)
    
    def getUserValues(self, username: str) -> User:
        return self.getUserVertex(username).getValue()

    def getUserRelations(self, username: str) -> dict:
        return self.getUserVertex(username).getConnections()
    
    def getUserConnectedTo(self, username: str) -> list:
        return list(self.getUserVertex(username).getConnectedTo())

    def addPerson(self, username: str, name: str, age: int) -> bool:
        newUser = Person(username, name, age, 'person')
        if self.addVertex(username, newUser, newUser.connectionTypes):
            self.__personsQty += 1
            return True
        return False
    
    def addOrganization(self, username: str, name: str) -> bool:
        newUser = Organization(username, name, 'organization')
        if self.addVertex(username, newUser, newUser.connectionTypes):
            self.__organizationsQty += 1
            return True
        return False
    
    def addRelation(self, username1: User, username2: User, relationType: str) -> bool:
        if username1 == username2:
            return False
        
        return self.enumRelationFunctions[relationType](username1, username2)
    
    def __addFriendship(self, username1: Person, username2: Person) -> bool:
        return self.addBidirectionalEdge(username1, username2, 'friends', 'friends')

    def __addRelative(self, username1: Person, username2: Person) -> bool:
        return self.addBidirectionalEdge(username1, username2, 'relatives', 'relatives')

    def __addAcquaintance(self, username1: Person, username2: Person) -> bool:
        return self.addUnidirectionalEdge(username1, username2, 'acquaintances')
    
    def __addFollow(self, username1: User, username2: User) -> bool:
        if self.addBidirectionalEdge(username1, username2, 'following', 'followers'):
            self.getUserValues(username2).incrementFollower()
            return True
        return False
    
    def __addClient(self, username1: User, username2: Organization) -> bool:
        if self.addBidirectionalEdge(username1, username2, 'client', 'clients'):
            self.getUserValues(username2).incrementClient()
            return True
        return False
    
    def search(self, username: str, searchTerm: str) -> list:
        if not self.userExists(username):
            return False
        
        color = {}
        queue = LinkedQueue()
        
        for user in self.getAllUsernames():
            color[user] = "WHITE"
        color[username] = "GRAY"
        
        foundUsers = []
        queue.enqueue(username)
        while queue.length > 0:
            s = queue.dequeue()
            connections = self.getUserVertex(s).getConnectedTo()
            for v in connections:
                if color.get(v) == "WHITE":
                    userPublicInfo = list(self.getUserVertex(v).getValue().getInfo().values())
                    color[v] = "GRAY"
                    queue.enqueue(v)
                    
                    for info in userPublicInfo:
                        if searchTerm.lower() in str(info).lower():
                            foundUsers.append(v)
                            break
            color[s] = "BLACK"
        
        return foundUsers
    
    def getUserCenteredGraph(self, username: str) -> dict:
        if not self.userExists(username):
            return False
        return self.breadthFirstSearch(username, 3)

    def getSocialNetworkGraph(self) -> dict:
        usernames = self.getAllUsernames()

        graph = {'nodes': usernames, 'connections': []}
        for username in usernames:
            for connectedUser in self.getUserConnectedTo(username):
                graph['connections'].append({'source': username, 'target': connectedUser})
                
        
        return graph