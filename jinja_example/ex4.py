from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
	users_list = []
	users_list.append({'name': 'Adrian', 'country': 'France'})
	users_list.append({'name': 'Loric', 'country': 'France'})
	users_list.append({'name': 'Valentina', 'country': 'Italy'})
	users_list.append({'name': 'Ahmed', 'country': 'Morocco'})

	return render_template('index.html', users=users_list)

if __name__ == "__main__":
    app.run()
