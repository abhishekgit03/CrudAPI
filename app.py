from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import pymongo
import uuid
from dotenv import load_dotenv
load_dotenv()
import os
mongo_password = os.environ.get("MONGO_PASSWORD")
app = Flask(__name__)
api = Api(app)


class Allusers(Resource):
    def __init__(self):
        self.client = pymongo.MongoClient(f"mongodb+srv://abhishekcode30:{mongo_password}@cluster0.qg5rjgo.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.client["database"]
        self.collection = self.db["users"]
    def get(self,id):          #Returns the user with the specified ID.
        
        existing_user = mongo_api.collection.find_one({'_id':id})
        if not existing_user:
            return jsonify({"error":"No such user exists"})
        return jsonify(existing_user)

    def delete(self,id):        #Deletes the user with the specified ID.
        existing_user = mongo_api.collection.find_one({'_id':id})
        if not existing_user:
            return jsonify({"error":"No such user found"})
        mongo_api.collection.delete_one({"_id":id})
        return jsonify({"message":"The user has been successfully deleted"})
   
    def put(self,id):       #Updates the user with the specified ID with the new data.
        
        data = request.get_json()
        if 'name' not in data or 'email' not in data or 'password' not in data:
            return jsonify({'error': 'Name, email, and password are required'})
        existing_user = mongo_api.collection.find_one({'_id': id})
        if not existing_user:
            return jsonify({'error': 'User does not exists'})
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        payload={
            "name":name,
            "email":email,
            "password":password
        }
        mongo_api.collection.update_one({'_id': id}, {'$set': payload})
        return jsonify({"message":"User details have been successfully updated"})

class User(Resource):
    def __init__(self):
        self.client = pymongo.MongoClient(f"mongodb+srv://abhishekcode30:{mongo_password}@cluster0.qg5rjgo.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.client["database"]
        self.collection = self.db["users"]

    def get(self):      #Returns a list of all users.
        
        all_users = mongo_api.collection.find()
        if len(list(all_users))==0:
            return jsonify({"error":"The database is empty"}), 400
        all_users=[]
        for user_data in mongo_api.collection.find():
            all_users.append(user_data)
        return jsonify(all_users)
    

    def post(self):    #Creates a new user with the specified data.
        
        data = request.get_json()
        if 'name' not in data or 'email' not in data:
            return jsonify({'error': 'Name and email are required'})
        id = str(uuid.uuid4())
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        existing_user = mongo_api.collection.find_one({'email': email})
        if existing_user:
            return jsonify({'error': 'User with the same email already exists'})

        payload={
            "_id":id,
            "name":name,
            "email":email,
            "password":password
        
        }
        mongo_api.collection.insert_one(payload)
        return jsonify({"message": f"User has been sucessfully inserted with id {id}"})

    

mongo_api = User()
api.add_resource(User, '/users',methods=["GET","POST"])
api.add_resource(Allusers, '/users/<string:id>',methods=["GET","DELETE","PUT"])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True) 