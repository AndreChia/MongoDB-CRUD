from pymongo import MongoClient

# pprint library to make the output more pretty
from pprint import pprint

def connect():
    # Connect to MongoDB
    client = MongoClient("<your connetion string")
    # Creating a database object referencing new database called "business"
    db = client.business
    return db

def insertOne(name, rating, cuisine):
    business = {
        'name' : name,
        'rating' : rating,
        'cuisine' : cuisine
    }
    result = db.reviews.insert_one(business)

def readOne(parameter, restName):
    review = db.reviews.find_one({parameter: restName})
    pprint(review)

def replaceOne(name, cuisine, rating, newValue):
    review = readOne('name', name)

    result = db.reviews.replace_one(
              {'name': name},
              {'cuisine': cuisine,
               'name': newValue,
               'rating': rating}, True)

    review = readOne('name', newValue)

def deleteOne(name):
    result = db.reviews.delete_one({'name': name})

if __name__ == '__main__':
    db = connect()
    # insertOne('Shake Shack', 5, 'Western')
    # readOne('name', 'Shake Shack')
    # replaceOne('Shake Shack', 'Western', 5, 'Five Guys')
    # readOne('name', 'Five Guys')
    # deleteOne('Five Guys')

