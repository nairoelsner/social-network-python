from social_network import *

socialNetwork = SocialNetwork()

#add persons
socialNetwork.addPerson('n_elsner', 'Nairo', '23')
socialNetwork.addPerson('clarossa', 'Clarisse', '20')
socialNetwork.addPerson('seven.renato', 'Paulo', '19')
socialNetwork.addPerson('seven.renato', 'Paulo', '19')
socialNetwork.addPerson('e-musk', 'Elon Musk', '52')
socialNetwork.addPerson('bill_gates', 'Bill Gates', '52')
socialNetwork.addPerson('steve_jobs', 'Steve Jobs', '52')

#add organizations
socialNetwork.addOrganization('coca-cola', 'Coca-Cola')
socialNetwork.addOrganization('guanabara', 'Guanabara')

#add friendships
socialNetwork.addRelation('n_elsner', 'clarossa', 'friendship')
socialNetwork.addRelation('n_elsner', 'seven.renato', 'friendship')
socialNetwork.addRelation('clarossa', 'seven.renato', 'friendship')
socialNetwork.addRelation('clarossa', 'bill_gates', 'friendship')
socialNetwork.addRelation('e-musk', 'bill_gates', 'friendship')
socialNetwork.addRelation('bill_gates', 'steve_jobs', 'friendship')

#add relatives
socialNetwork.addRelation('n_elsner', 'clarossa', 'relative')

#add acquaintances
socialNetwork.addRelation('seven.renato', 'e-musk', 'acquaintance')

#add follows
socialNetwork.addRelation('n_elsner', 'seven.renato', 'follow')
socialNetwork.addRelation('seven.renato', 'n_elsner', 'follow')
socialNetwork.addRelation('clarossa', 'n_elsner', 'follow')
socialNetwork.addRelation('seven.renato', 'coca-cola', 'follow')
socialNetwork.addRelation('coca-cola', 'n_elsner', 'follow')

#add clients
socialNetwork.addRelation('guanabara', 'coca-cola', 'client')
socialNetwork.addRelation('seven.renato', 'guanabara', 'client')
socialNetwork.addRelation('n_elsner', 'guanabara', 'client')
socialNetwork.addRelation('clarossa', 'guanabara', 'client')

users = socialNetwork.getUsers()
print('All users:')
for user in users:
    print(user, '\n')
    pass

#relations - OK!


print('Users qty -->', socialNetwork.getUsersQty(), '\n')


nairo = socialNetwork.getUserValues('n_elsner')
print('public info -->', nairo.getInfo())

print('public info -->', nairo.getInfo())
nairo.changeInfoVisibility('username')
#nairo.changeInfoVisibility('followersQty')
#nairo.changeInfoVisibility('age')
print('public info -->', nairo.getInfo())

#nairo.changeInfoVisibility('followersQty')
print('public info -->', nairo.getInfo())

#visibility - OK!


#search user
#print(socialNetwork.search('n_elsner', 'paul'))

#graph centered in user
#print(socialNetwork.getUserCenteredGraph('n_elsner'))
print(socialNetwork.getSocialNetworkGraph())