#Lists

name = 'nanwen'
level = 5
awesomeness = 95.5
is_raining = True



backpack=[]

backpack = [
    'drink bottle',
    'yogurt',
    'heaphones',
    'laptop',
]


for index,item in enumerate(backpack):
    print(index, item)

counter = 0
for item in backpack:
    print(counter, item)
    counter = counter + 1