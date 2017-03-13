bigkey = ''
big = 0
for key in animals.keys():
    if(big < len(animals[key])):
        big = len(animals[key])
        bigkey = key 
