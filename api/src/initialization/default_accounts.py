from src.social_network.social_network import *
from random import randint

def createUsers(socialNetwork):
    sheet = open('./api/src/initialization/users.csv', 'r')
    users = [x[:-1].split(';') for x in sheet.readlines()]
    sheet.close()

    relationTypes = {'person': ['friendship', 'relative', 'acquaintance', 'follow'], 'organization': ['follow', 'client']}
    personInfoTypes = ['name', 'age', 'followersQty']

    for user in users:
        if user[-1] == 'person':
            socialNetwork.addPerson(user[0], user[1], user[2])
            for i in range(randint(0, 2)):
                socialNetwork.getUserValues(user[0]).changeInfoVisibility(personInfoTypes[randint(0, 2)])
        else:
            socialNetwork.addOrganization(user[0], user[1])

    
    for user in users:
        for i in range(randint(0, 2)):
            randomUser = users[randint(0, len(users) -1)]
            while randomUser == user:
                randomUser = users[randint(0, len(users) -1)]
            
            randomUserType = randomUser[-1]
            userType = user[-1]

            if userType == 'person' and randomUserType == 'organization':
                possibilities = relationTypes['organization']
            elif userType == 'organization' and randomUserType == 'person':
                possibilities = relationTypes['organization'][:-1]
            else:
                possibilities = relationTypes[userType]

            socialNetwork.addRelation(user[0], randomUser[0], possibilities[randint(0, len(possibilities)-1)])