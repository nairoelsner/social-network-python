from graph import *
from user import *

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
    
    def getUsers(self) -> dict:
        userVertices = self.getVerticesValues() 
        users = []
        for userVertex in userVertices:
            userConnectionTypes = list(userVertex.getConnections().keys())
            connections = {}
            for key in userConnectionTypes:
                connections[key] = list(userVertex.getConnections()[key].keys())
            users.append({'info': userVertex.getValue().getPublicInfos(), 'connections': connections})
        return users
        
    def getUser(self, username: str) -> Vertex:
        return self.getVertex(username)
    
    def getUserValues(self, username: str) -> User:
        return self.getUser(username).getValue()

    def getUserRelations(self, username: str) -> dict:
        return self.getUser(username).getConnections()

    def addPerson(self, username: str, name: str, age: int) -> bool:
        newUser = Person(username, name, age)
        if self.addVertex(username, newUser, newUser.connectionTypes):
            self.__personsQty += 1
            return True
        return False
    
    def addOrganization(self, username: str, name: str) -> bool:
        newUser = Organization(username, name)
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