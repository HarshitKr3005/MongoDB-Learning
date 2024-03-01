import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb = client['Employee']

information = mydb.employeeinformation

records = [
{
    'firstname' : "Gaurang",
    'lastname' : "Ashava",
    'dept' : "BDA"
},
{
    'firstname' : "Safal",
    'lastname' : "Mehrotra",
    'dept' : "BDA"
},
{
    'firstname' : "Ansh",
    'lastname' : "Aggarwal",
    'dept' : "BDA"
}]

information.insert_many(records)

