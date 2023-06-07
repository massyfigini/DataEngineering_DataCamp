############################
# Flexibly Structured Data #
############################

### Listing databases and collections

# Save a list of names of the databases managed by client
db_names = client.list_database_names()
print(db_names)

# Save a list of names of the collections managed by the "nobel" database
nobel_coll_names = client.nobel.list_collection_names()
print(nobel_coll_names)


### List fields of a document

# Connect to the "nobel" database
db = client.nobel

# Retrieve sample prize and laureate documents
prize = db.prizes.find_one()
laureate = db.laureates.find_one()

# Print the sample prize and laureate documents
print(prize)
print(laureate)
print(type(laureate))

# Get the fields present in each type of document
prize_fields = list(prize.keys())
laureate_fields = list(laureate.keys())

print(prize_fields)
print(laureate_fields)


### Composing filters

# 1
# Create a filter for laureates who died in the USA
criteria = {"diedCountry": "USA"}

# Save the count of these laureates
count = db.laureates.count_documents(criteria)
print(count)

# 2
# Create a filter for laureates who died in the USA but were born in Germany
criteria = {"diedCountry": "USA", 
            "bornCountry": "Germany"}

# Save the count
count = db.laureates.count_documents(criteria)
print(count)

# 3
# Create a filter for Germany-born laureates who died in the USA and with the first name "Albert"
criteria = {"diedCountry": "USA", 
            "bornCountry": "Germany", 
            "firstname": "Albert"}

# Save the count
count = db.laureates.count_documents(criteria)
print(count)


### We've got options

# 1
# Save a filter for laureates born in the USA, Canada, or Mexico
criteria = { "bornCountry":  
                { "$in": ["USA", "Canada", "Mexico"]}
             }

# Count them and save the count
count = db.laureates.count_documents(criteria)
print(count)

# 2
# Save a filter for laureates who died in the USA and were not born there
criteria = { "diedCountry": "USA",
               "bornCountry": { "$ne": "USA"}, 
             }

# Count them
count = db.laureates.count_documents(criteria)
print(count)


### Starting our ascent

# Filter for laureates born in Austria with non-Austria prize affiliation
criteria = {"bornCountry": "Austria", 
              "prizes.affiliations.country": {"$ne": "Austria"}}

# Count the number of such laureates
count = db.laureates.count_documents(criteria)
print(count)


### Our 'born' approximation, and a special laureate

# 1
# Filter for documents without a "born" field
criteria = {"born": {"$exists": False}}

# Save count
count = db.laureates.count_documents(criteria)
print(count)

# 2
# Filter for laureates with at least three prizes
criteria = {"prizes.2": {"$exists": True}}

# Find one laureate with at least three prizes
doc = db.laureates.find_one(criteria)

# Print the document
print(doc)



