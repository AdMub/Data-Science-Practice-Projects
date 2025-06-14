import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

mydb = client["Employee"]

information = mydb.employeeinformation

record = {
    "firstname": "AdMub",
    "lastname": "Mubarak",
    "Department": "Civil Engineering",
    "Skills": "Data Science"
    }
information.insert_one(record)



record1 =[{
    "firstname": "AdMub",
    "lastname": "Mubarak",
    "Department": "Civil Engineering",
    "Skills": "Data Science"
    }, {
        "firstname": "AdMub1",
        "lastname": "Mubarak1",
        "Department": "Civil Engineering",
        "Skills": "Data Science"
        }, {
            "firstname": "AdMub2",
            "lastname": "Mubarak2",
            "Department": "Civil Engineering",
            "Skills": "Data Science"
            }]



information.insert_many(record1)