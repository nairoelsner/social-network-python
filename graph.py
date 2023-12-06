from linked_queue import *
from user import Person, Organization

class Vertex:
    def __init__(self, key, value, connectionsTypes):
        self.__key = key
        self.__value = value
        self.__connections = {}

        for connType in connectionsTypes:
            self.addConnectionType(connType)
    
    def __repr__(self):
        return str(self.__value.getUsername()) + ' ' + str(self.__connections)

    def getKey(self):
        return self.__key
    
    def getValue(self):
        return self.__value
    
    def getConnections(self):
        return self.__connections
    
    def getConnection(self, connectionType):
        return self.__connections[connectionType]

    def getWeight(self, adjKey, connectionType):
        return self.__connections[connectionType][adjKey]
    
    def addConnection(self, adjKey, connectionType, weight=0):
        self.__connections[connectionType][adjKey] = weight
        return True
    
    def addConnectionType(self, connectionType):
        self.__connections[connectionType] = {}


class Graph:
    def __init__(self):
        self.__vertices = {}
        self.__numVertices = 0

    def __contains__(self, key):
        return key in self.__vertices

    def __iter__(self):
        return iter(self.__vertices.values())

    def getVerticesKeys(self):
        return self.__vertices.keys()
    
    def getVerticesValues(self):
        return self.__vertices.values()

    def addVertex(self, key, value, connectionsTypes):
        if key in self.__vertices:
            return False
        
        newVertex = Vertex(key, value, connectionsTypes)
        self.__vertices[key] = newVertex
        self.__numVertices += 1
        return True

    def getVertex(self, key):
        if key in self.__vertices:
            return self.__vertices[key]
        return None

    def addUnidirectionalEdge(self, p, q, connectionType, weight=0):
        if p in self.__vertices and q in self.__vertices:
            self.__vertices[p].addConnection(q, connectionType, weight)
            return True
        return False

    def addBidirectionalEdge(self, p, q, connectionType1, connectionType2, weight1=0, weight2=0):
        if p in self.__vertices and q in self.__vertices:
            self.__vertices[p].addConnection(q, connectionType1, weight1)
            self.__vertices[q].addConnection(p, connectionType2, weight2)
            return True
        return False

    #testing
    def breadthFirstSearch(self, key, value, maxDepth):
        if key not in self.__vertices:
            return False
        
        visitedVertices = {}
        distance = 0
        queue = LinkedQueue()
        queue.enqueue(self.__vertices[key])

        while queue.length > 0 and distance <= maxDepth:
            currentVertex = queue.dequeue()
            for adjVertex in currentVertex.getConnections():
                queue.enqueue(self.__vertices[adjVertex])
                print(adjVertex)
            distance += 1

    def bfs(self, start, value, maxDepth):
        if value not in self.__vertices:
            return False
        color = {}  # Cores dos vértices
        d = {}  # Distâncias dos vértices
        pi = {}  # Vértices predecessores
        distance = 0
        queue = []  # Fila
        find_user = False
        for u in self.__vertices:
            if u != start:
                color[u] = "WHITE"
                d[u] = float("inf")
                pi[u] = None
                print(u)
        color[start] = 'GRAY'
        d[start] = 0
        pi[start] = None
        queue.append(start)
        while queue and distance <= maxDepth and not find_user:
            s = queue.pop(0)
            is_user = isinstance(self.getUser(s).getValue(), Person)
            if (is_user):
                connections = list(set(list(self.__vertices[s].getConnections()["friends"].keys()) + list(self.__vertices[s].getConnections()["following"].keys()) + list(self.__vertices[s].getConnections()["followers"].keys()) + list(self.__vertices[s].getConnections()["relatives"].keys()) + list(self.__vertices[s].getConnections()["acquaintances"].keys())))
            else:
                connections = list(set(list(self.__vertices[s].getConnections()["clients"].keys()) + list(self.__vertices[s].getConnections()["client"].keys()) + list(self.__vertices[s].getConnections()["following"].keys())))
            for v in connections:
                if (isinstance(self.getUser(v).getValue(), Person)):
                    user = self.getUser(v).getValue().getPublicInfos().values()
                else:
                    user = self.getUser(v).getValue().getInfos().values()
                if color.get(v) == "WHITE": 
                    color[v] = "GRAY" 
                    d[v] = d[s] + 1  
                    pi[v] = s 
                if value in user:
                    find_user = True
                    break
            color[s] = "BLACK" # 
            distance += 1
        return d[value],pi[value]