# CrudAPI

## Getting Started

- The Flask API is deployed on Render and can be accessed through the following endpoint: https://crudapi-p1kz.onrender.com
- You can also clone the repo and test using Postman

### Databases and packages used

- MongoDB
- Flask
- flask_restful
- Pymongo
- jsonify
- python-dotenv
- uuid


### Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/abhishekgit03/CrudAPI.git
2. Create virtual envioronment using the command:``` python -m venv env```
3. Activate the env using command: ```./env/Scripts/activate```
4. Install packages: ```pip install -r requirements.txt```
5. Run the flask app using: python app.py

1) POST https://crudapi-p1kz.onrender.com/users:
   
   Creates a new user with the specified data.
![image](https://github.com/abhishekgit03/CrudAPI/assets/92089364/4c14ba75-723a-4159-9d81-5fd3b5aea206)

3) GET  https://crudapi-p1kz.onrender.com/users/8b01830c-00a4-4824-b9f3-7ccb0840719b
   
   Returns the user with the specified ID.
![image](https://github.com/abhishekgit03/CrudAPI/assets/92089364/5e154c6d-d5d5-44a3-9ad1-3bf37f264579)

5) GET  https://crudapi-p1kz.onrender.com/users

   Returns a list of all users.
![image](https://github.com/abhishekgit03/CrudAPI/assets/92089364/ae81213d-af50-4060-ad37-c96ff611dde4)

7) PUT  http://192.168.0.103:5000/users/8b01830c-00a4-4824-b9f3-7ccb0840719b4

   Updates the user with the specified ID with the new data.
![image](https://github.com/abhishekgit03/CrudAPI/assets/92089364/16314078-adf7-48cf-a252-f160e38c267e)

9) DELETE https://crudapi-p1kz.onrender.com/users/8b01830c-00a4-4824-b9f3-7ccb0840719b

   Deletes the user with the specified ID.
![image](https://github.com/abhishekgit03/CrudAPI/assets/92089364/52a7de74-21c2-4f00-924e-7b1c9646272f)

## Note: In Render webservice Free plan, server becomes idle after 15 mins of inactivity. The first request may take some time. Subsequent requests will be faster.




