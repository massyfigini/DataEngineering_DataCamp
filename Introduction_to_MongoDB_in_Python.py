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




#########################################
# Working with Distinct Values and Sets #
#########################################

### Never from there, but sometimes there at last

# Countries recorded as countries of death but not as countries of birth
countries = set(db.laureates.distinct("diedCountry")) - set(db.laureates.distinct("bornCountry"))
print(countries)


### Countries of affiliation

# The number of distinct countries of laureate affiliation for prizes
count = len(db.laureates.distinct("prizes.affiliations.country"))
print(count)


### Triple plays (mostly) all around

# Save a filter for prize documents with three or more laureates
criteria = {"laureates.2": {"$exists": True}}

# Save the set of distinct prize categories in documents satisfying the criteria
triple_play_categories = set(db.prizes.distinct("category", criteria))

# Confirm literature as the only category not satisfying the criteria.
assert set(db.prizes.distinct("category")) - triple_play_categories == {"literature"}


### Meanwhile, in other categories...

# Save a filter for laureates with unshared prizes
unshared = {
    "prizes": {"$elemMatch": {
        "category": {"$nin": ["physics", "chemistry", "medicine"]},
        "share": "1",
        "year": {"$gte": "1945"},
    }}}

# Save a filter for laureates with shared prizes
shared = {
    "prizes": {"$elemMatch": {
        "category": {"$nin": ["physics", "chemistry", "medicine"]},
        "share": {"$ne": "1"},
        "year": {"$gte": "1945"},
    }}}

ratio = db.laureates.count_documents(unshared) / db.laureates.count_documents(shared)
print(ratio)


### Organizations and prizes over time

# Save a filter for organization laureates with prizes won before 1945
before = {
    "gender": "org",
    "prizes.year": {"$lt": "1945"},
    }

# Save a filter for organization laureates with prizes won in or after 1945
in_or_after = {
    "gender": "org",
    "prizes.year": {"$gte": "1945"},
    }

n_before = db.laureates.count_documents(before)
n_in_or_after = db.laureates.count_documents(in_or_after)
ratio = n_in_or_after / (n_in_or_after + n_before)
print(ratio)


### Germany, then and now

# 1
from bson.regex import Regex
# Filter for laureates with "Germany" in their "bornCountry" value
criteria = {"bornCountry": Regex("Germany",0)}
print(set(db.laureates.distinct("bornCountry", criteria)))

#2
from bson.regex import Regex
# Filter for laureates with a "bornCountry" value starting with "Germany"
criteria = {"bornCountry": Regex("^Germany")}
print(set(db.laureates.distinct("bornCountry", criteria)))

# 3
from bson.regex import Regex
# Fill in a string value to be sandwiched between the strings "^Germany " and "now"
criteria = {"bornCountry": Regex("^Germany " + "\\(" + "now")}
print(set(db.laureates.distinct("bornCountry", criteria)))

# 4
from bson.regex import Regex
#Filter for currently-Germany countries of birth. Fill in a string value to be sandwiched between the strings "now" and "$"
criteria = {"bornCountry": Regex("now" + " Germany\\)" + "$")}
print(set(db.laureates.distinct("bornCountry", criteria)))


### The prized transistor

from bson.regex import Regex

# Save a filter for laureates with prize motivation values containing "transistor" as a substring
criteria = {"prizes.motivation": Regex("transistor")}

# Save the field names corresponding to a laureate's first name and last name
first, last = "firstname", "surname"
print([(laureate[first], laureate[last]) for laureate in db.laureates.find(criteria)])



