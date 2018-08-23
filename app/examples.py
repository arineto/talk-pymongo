from pymongo import MongoClient

# Opens the connection with the server
client = MongoClient()

# Gets the database
db = client.get_database('talk_pymongo')

# Gets the collection
collection = db.get_collection('cars')

# Create example 1
data = {
    'brand': 'Volkswagen',
    'model': 'Gol',
    'plate': 'PGI-1596',
    'year': 2013
}

collection.insert(data)

# Create example 2
data = [
    {
        'brand': 'Volkswagen',
        'model': 'Fox',
        'plate': 'PMN-7456',
        'year': 2015
    },
    {
        'brand': 'Chevrolet',
        'model': 'Cobalt',
        'plate': 'PPM-3409',
        'year': 2018
    }
]

collection.insert(data)

# Retrieve example 1
for car in collection.find():
    print(car.get('_id'))

# Retrieve example 2
for car in collection.find({'brand': 'Volkswagen'}):
    print(car.get('_id'))

# Retrieve example 3
for car in collection.find({'year': {'$gte': 2015}}):
    print(car.get('_id'))

# Retrieve example 4
for car in collection.find({'plate': {'$regex': '^PMN-*'}}):
    print(car.get('_id'))

# Retrieve example
filters = {
    '$and': [
        {'brand': 'Volkswagen'},
        {'year': {'$gte': 2015}}
    ]
}
for car in collection.find(filter):
    print(car.get('_id'))

# Update example 1
collection.update(
    {'plate': 'PPM-3409'},
    {'year': '2015'}
)

# Update example 2
collection.update(
    {'plate': 'PPM-3409'},
    {'$set': {'year': '2015'}}
)

# Delete example 1
collection.remove({'brand': 'Volkswagen'})
