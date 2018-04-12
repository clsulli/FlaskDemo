from pymongo import MongoClient
from pprint import pprint
from random import randint

connectionString = "mongodb+srv://sully:sIf5R3HGFw8Nduqd@pythonflask-cyxqv.mongodb.net/test"
client = MongoClient(connectionString)
# dbAdmin = client.admin
# serverStatusResult = dbAdmin.command("serverStatus")
# pprint(serverStatusResult)

db = client.example
names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
company_type = ['LLC','Inc','Company','Corporation']
company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']

# for x in range(1, 501):
#     business = {
#         'name' : names[randint(0, (len(names)-1))] + ' ' + names[randint(0, (len(names)-1))]  + ' ' + company_type[randint(0, (len(company_type)-1))],
#         'rating' : randint(1, 5),
#         'cuisine' : company_cuisine[randint(0, (len(company_cuisine)-1))]
#     }
#     result = db.reviews.insert_one(business)
#     print('Created %s of 100 as %s' % (x, result.inserted_id))
#
# print('finished creating 100 business reviews')

fivestar = db.reviews.find({'rating':5}).count()
pprint(fivestar)

ASingleReview = db.reviews.find_one({})
print('A Sample Document:')
pprint(ASingleReview)

result = db.reviews.update_one({'_id' : ASingleReview.get('_id')}, {'$inc': {'likes': 1}})
print('Number of documents modified :' + str(result.modified_count))

UpdatedDocument = db.reviews.find_one({'_id':ASingleReview.get('_id')})
print('The updated document:')
pprint(UpdatedDocument)



