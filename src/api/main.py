import flask
import json
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
supplies = [
    {'Id': 0,
     'Name': 'Bandages',
     'Description': 'Medical bandages',
     'Weight': '5 kgs',
     'stockAvailable': 5,
     'imageURL':'https://tinyurl.com/7r966zn8'},
    {'Id': 1,
     'Name': 'Ammo',
     'Description': 'Ammunition for the Glock 17',
     'Weight':'10 kgs',
     'stockAvailable': 200,
     'imageURL':'https://www.clarkesofwalsham.co.uk/pub/media/staempfli_imageresizer/cache/catalog/category/700x400_co_ar_tr_fr_bc/ammo.png'},
    {'Id': 2,
     'Name': 'Care package',
     'Description': 'Random selection of supplies',
     'Weight': '100 kgs',
     'stockAvailable': 10,
     'imageURL':'https://www.veteransunited.com/assets/craft/images/blog/_blogWideThumb/care-package.jpg'},
    {'Id': 3,
    'Name': 'dynamite',
    'Description': 'Blows stuff up',
    'Weight': '101 kgs',
    'stockAvailable': 3,
    'imageURL':'https://cbrnecentral.com/wp-content/uploads/2017/02/explosives-threats.jpg'}  
]

status = {"status":"Success"}

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Supply Catalogue</h1> <p>This is a REST api, used to communicate between the web app and mcrobit.</p>'''

# A route to return all of the available entries in our catalog.
@app.route('/supplies', methods=['GET'])
def getItems():
    return jsonify(supplies)

@app.route('/supplies/item/<id>', methods=['GET'])
def getItem(id):
    return jsonify(supplies[int(id)])

# A simple test to ensure the api is returning requests.
@app.route('/test', methods=['POST'])
def getStatus():
    return jsonify(status)

app.run()

