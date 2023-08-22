import pymongo
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import json
import os
import uuid
from dotenv import load_dotenv
load_dotenv()
mongo_password = os.environ.get("MONGO_PASSWORD")
client = pymongo.MongoClient(f"mongodb+srv://abhishekcode30:{mongo_password}@cluster0.qg5rjgo.mongodb.net/?retryWrites=true&w=majority")
db = client["database"]
collection = db["users"]
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/users",methods=["POST"])  #Creates a new user with the specified data.
def postuser():
    data = request.get_json()
    if 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Name and email are required'}), 400
    id = str(uuid.uuid4())
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    existing_user = collection.find_one({'email': email})
    if existing_user:
        return jsonify({'error': 'User with the same email already exists'}), 400

    payload={
        "_id":id,
        "name":name,
        "email":email,
        "password":password
    
    }
    collection.insert_one(payload)
    return jsonify({"message": "User has been sucessfully inserted"})

@app.route("/users/<string:id>",methods=["GET"])   #Returns the user with the specified ID.
def getuser(id):
    existing_user = collection.find_one({'_id': id})
    if not existing_user:
        return jsonify({"error":"No such user exists"}), 400
    return jsonify(existing_user)

@app.route("/users/",methods=["GET"])  #Returns a list of all users.
def getallusers():
    
    all_users = collection.find()
    if len(list(all_users))==0:
        return jsonify({"error":"The database is empty"}), 400
    all_users=[]
    for user_data in collection.find():
        all_users.append(user_data)
    return jsonify(all_users)

@app.route("/users/<string:id>",methods=["PUT"])  #Updates the user with the specified ID with the new data.
def updateuser(id):
    data = request.get_json()
    if 'name' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Name, email, and password are required'}), 400
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    payload={
        "name":name,
        "email":email,
        "password":password
    }
    collection.update_one({'_id': id}, {'$set': payload})
    return jsonify({"message":"User details have been successfully updated"})

@app.route("/users/<string:id>",methods=["DELETE"])    #Deletes the user with the specified ID.
def deleteuser(id):
    
    result = collection.delete_one({"_id":id})
    if not result:
        return jsonify({"error":"No such user found"}), 400

    return jsonify({"message":"The user has been successfully deleted"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True) 