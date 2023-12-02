class User:
    def __init__(self, username, name):
        self.__username = username
        self.__name = name
    
    def getUsername(self):
        return self.__username
    
    def getName(self):
        return self.__name

class Person(User):
    def __init__(self, username, name, age):
        super().__init__(username, name)
        self.__infos = {
            'username': [username, True], 
            'name': [name, True], 
            'age': [age, True],
            'followersQty': [0, True]
        }
        self.connectionTypes = ['friends', 'relatives', 'acquaintances', 'client', 'following', 'followers']
        
    def __repr__(self):
        return str(self.getPublicInfos())
    
    def __str__(self):
        return str(self.getPublicInfos())
    
    def changeInfoVisibility(self, key):
        if key not in self.__infos or key == 'username':
            return False
        self.__infos[key][1] = not self.__infos[key][1]
        return True
        
    def incrementFollower(self):
        self.__infos['followersQty'][0] += 1

    def getInfos(self):
        infos = {}
        for key in self.__infos.keys():
            infos[key] = self.__infos[key][0]
        return infos

    def getPublicInfos(self):
        publicInfos = {}
        for key in self.__infos.keys():
            if self.__infos[key][1]:
                publicInfos[key] = self.__infos[key][0]
        return publicInfos

class Organization(User):
    def __init__(self, username, name):
        super().__init__(username, name)
        
        self.__infos = {
            'username': username, 
            'name': name,
            'clientsQty': 0,
            'FollowersQty': 0
        }
        self.connectionTypes = ['clients', 'client', 'following', 'followers']

    def getInfos(self):
        return self.__infos
    
    def getInfo(self, key):
        if key not in self.__infos:
            return None
        return self.__infos[key]

    def incrementClient(self):
        self.__infos['clientsQty'] += 1
    
    def incrementFollower(self):
        self.__infos['FollowersQty'] += 1