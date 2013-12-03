from flask import Flask, request, render_template
import pymongo
import json

app = Flask(__name__)

m_client = pymongo.MongoClient()
db = m_client.webapp

@app.route("/")
def index():
	users_list = list(db.users.find())

	return render_template('index.html', users=users_list)

@app.route("/users")
def all_users():
	users = list(db.users.find())
	return json.dumps(users)

@app.route("/users/<username>", methods=["GET"])
def get_user(username):
	users = list(db.users.find({"name": username}))
	return json.dumps(users)

@app.route("/users/<username>", methods=["DELETE"])
def delete_user(username):
	try:
		db.users.remove({'name': username})
		return json.dumps({'deleted': True})
	except Exception as e:
		return json.dumps({'deleted': False})


@app.route("/users", methods=["POST"])
def add_user():
	try:
		u_id, username, country = request.form['id'], request.form['name'], request.form['country']
		db.users.insert({'_id': u_id, 'name': username, 'country': country})
		return index()
	except Exception as e:
		return json.dumps({"error": True})

def init_db():
	db.drop_collection('users')

	db.users.insert({'_id': 0, 'name': 'Adrian', 'country': 'France'})
	db.users.insert({'_id': 1, 'name': 'Loric', 'country': 'France'})
	db.users.insert({'_id': 2, 'name': 'Valentina', 'country': 'Italy'})
	db.users.insert({'_id': 3, 'name': 'Ahmed', 'country': 'Morocco'})

if __name__ == "__main__":
    init_db()

    app.run()
