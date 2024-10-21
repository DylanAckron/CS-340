from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    
    def __init__(self, user, pwd):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32747
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        print("Creation Mode")
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary            
        else:
            raise Exception("Nothing to save, because data parameter is empty")
                
        
    def read(self, searchTerm):
        print("read method")
        if searchTerm is not None:
            data = self.database.animals.find(searchTerm,{"_id": False})
            
        #if searchTerm:
         #   data = self.database.animals.find(searchTerm)
        else:
            data = self.database.animals.find({}, {"_id": False})
            
        return data            
    
    def update(self, searchTerm, updateTerm):
        if searchTerm is not None:
            result = self.database.animals.update_many(searchTerm, {"$set": updateTerm})
            
        else: return"{}"
        
        return result.raw_result
    
    def delete(self, deleteTerm):
        if deleteTerm is not None:
            result = self.database.animals.delete_many(deleteTerm)
            
        else:
            return "{}"
        
        return result.raw_result
                
        return result

