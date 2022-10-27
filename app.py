import os
from handlers.HWSet import HWSet
from flask import Flask, send_from_directory, jsonify

app = Flask(__name__, static_url_path='', static_folder='ui/build/')

@app.route('/')
def index():
    return send_from_directory('ui/build/', 'index.html')

""" Test out sending data to frontend. """
@app.route("/init")
def init_data():
    respJson = jsonify({"proj0": ["Project 0", "User 1", 50, 100, 30, 100],  # "Project 0", "User 1", "HWSet 1: 50/100", "HWSet 2: 30/100"
                    "proj1": ["Project 1", "User 2", 20, 80, 0, 100],    # "Project 1", "User 2", "HWSet 1: 50/100", "HWSet 2: 0/100"
                    "proj2": ["Project 2", "User 3", 50, 50, 30, 40],    # "Project 2", "User 3", "HWSet 1: 50/50", "HWSet 2: 30/40"
                    "proj3": ["Project 3", "User 4", 50, 70, 30, 80]})   # "Project 3", "User 4", "HWSet 1: 50/70", "HWSet 2: 30/50"
    print(respJson)
    return respJson

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))

# Task 1 Code

hw1 = HWSet(100)
hw2 = HWSet(50)

""" Query the projectId and quantity from the URL and returns the
    project id and quantity to the front end. The front end displays 
    a pop-up message which says “<qty> hardware checked in”. """
@app.route("/hardware/proj_id=<projectId>/chk_out=<qty>")
def checkIn_hardware(projectId, qty):
    hw1.check_out(qty)
    return jsonify({"HWSet1": hw1}, {"HWSet2": hw2})

""" Query the projectId and quantity from the URL and returns the
    project id and quantity to the front end. The front end displays
    a pop-up message which says “<qty> hardware checked out”. """
def checkOut_hardware(projectid, qty):
    pass

""" Queries the projectId from the URL and returns the project id
    to the front end. The front end displays a pop-up message
    which says “Joined <projectId>”. """
def joinProject(projectid):
    pass

""" This function queries the projectId from the URL and returns the
project id to the front end. The front end displays a pop-up message
which says “Left <projectId>”. """
def leaveProject(projectid):
    pass
