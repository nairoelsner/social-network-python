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
        self.__info = {
            'username': [username, True], 
            'name': [name, True], 
            'age': [age, True],
            'followersQty': [0, True]
        }
        self.connectionTypes = ['friends', 'relatives', 'acquaintances', 'client', 'following', 'followers']
        
    def __repr__(self):
        return str(self.getInfo())
    
    def __str__(self):
        return str(self.getInfo())
    
    def changeInfoVisibility(self, key):
        if key not in self.__info or key == 'username':
            return False
        self.__info[key][1] = not self.__info[key][1]
        return True
        
    def incrementFollower(self):
        self.__info['followersQty'][0] += 1

    def getInfo(self):
        publicinfo = {}
        for key in self.__info.keys():
            if self.__info[key][1]:
                publicinfo[key] = self.__info[key][0]
        return publicinfo
    
    def getAllInfo(self):
        info = {}
        for key in self.__info.keys():
            info[key] = self.__info[key][0]
        return info

class Organization(User):
    def __init__(self, username, name):
        super().__init__(username, name)
        
        self.__info = {
            'username': username, 
            'name': name,
            'clientsQty': 0,
            'FollowersQty': 0
        }
        self.connectionTypes = ['clients', 'client', 'following', 'followers']

    def getInfo(self):
        return self.__info

    def incrementClient(self):
        self.__info['clientsQty'] += 1
    
    def incrementFollower(self):
        self.__info['FollowersQty'] += 1