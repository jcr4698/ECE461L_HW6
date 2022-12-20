import os
from handlers.HWSet import HWSet
from flask import Flask, send_from_directory, jsonify, request

app = Flask(__name__, static_url_path='', static_folder='ui/build/')

@app.route('/')
def index():
    return send_from_directory('ui/build/', 'index.html')

""" Test out sending data to frontend. """
@app.route("/init")
def test():
    return jsonify({"proj0": ["Project 0", "User 1", 50, 100, 30, 100],  # "Project 0", "User 1", "HWSet 1: 50/100", "HWSet 2: 30/100"
                    "proj1": ["Project 1", "User 2", 20, 80, 0, 100],    # "Project 1", "User 2", "HWSet 1: 50/100", "HWSet 2: 0/100"
                    "proj2": ["Project 2", "User 3", 50, 50, 30, 40],    # "Project 2", "User 3", "HWSet 1: 50/50", "HWSet 2: 30/40"
                    "proj3": ["Project 3", "User 4", 50, 70, 30, 80]})   # "Project 3", "User 4", "HWSet 1: 50/70", "HWSet 2: 30/50"

# Task 1 Code

hw1 = HWSet(100)
hw2 = HWSet(50)

# @app.route("/test")
# def hw_init():
#     hw_id = request.args.get("hw_id")
#     qty = request.args.get("qty")
#     return jsonify({"": 100, "HWSet1": 50})
#     # return '{}:{}'.format(hw_id, qty)

@app.route("/test", methods = ['POST', 'GET'])
def hw_pick():
    hw_id = request.form.get("hw_id")
    qty = request.form.get("qty")

    if request.method == 'POST':
        print(str(hw_id))
        print(str(qty))

    return """  <div>
                    <form method="POST" action >
                        HW Set: <input type="text" name="hw_id">
                        Quantity: <input type="text" name="qty">
                        <input type="submit" />
                    </form>
                </div>
                <div>
                    <h1> {}: {}/{} </hi>
                </div>""".format(hw_id, qty, hw1.get_capacity())

""" Query the projectId and quantity from the URL and returns the
    project id and quantity to the front end. The front end displays 
    a pop-up message which says “<qty> hardware checked in”. """
@app.route("/check_in", methods=["POST", "GET"])
def checkIn_hardware():
    hw_id = request.form.get("hw_id")
    qty = request.form.get("qty")

    # Compute Input
    if qty == None:
        qty = hw1.get_availability()
    else:
        hw1.check_in(int(qty))

    return """  <div>
                    <form method="POST" action >
                        HW Set: <input type="text" name="hw_id">
                        Quantity: <input type="text" name="qty">
                        <input type="submit" />
                    </form>
                </div>
                <div>
                    <h1> {}: {}/{} </hi>
                </div>""".format(hw_id, hw1.get_availability(), hw1.get_capacity())

""" Query the projectId and quantity from the URL and returns the
    project id and quantity to the front end. The front end displays
    a pop-up message which says “<qty> hardware checked out”. """
@app.route("/check_out", methods=["POST", "GET"])
def checkOut_hardware():
    hw_id = request.form.get("hw_id")
    qty = request.form.get("qty")

    # Compute Input
    if qty == None:
        qty = hw1.get_availability()
    else:
        hw1.check_out(int(qty))

    return """  <div>
                    <form method="POST" action >
                        HW Set: <input type="text" name="hw_id">
                        Quantity: <input type="text" name="qty">
                        <input type="submit" />
                    </form>
                </div>
                <div>
                    <h1> {}: {}/{} </hi>
                </div>""".format(hw_id, hw1.get_availability(), hw1.get_capacity())

""" Queries the projectId from the URL and returns the project id
    to the front end. The front end displays a pop-up message
    which says “Joined <projectId>”. """
@app.route("/join", methods=["POST", "GET"])
def joinProject():
    joined = request.form.get("join")
    if(joined == None):
        joined = "[insert name in field above]"
    else:
        print(joined)

    return """  <div>
                    <form method="POST" action >
                        HW Set: <input type="text" name="join">
                        <input type="submit" />
                    </form>
                </div>
                <div>
                    <h1> Joined {} </hi>
                </div>""".format(joined)

""" This function queries the projectId from the URL and returns the
project id to the front end. The front end displays a pop-up message
which says “Left <projectId>”. """
@app.route("/leave", methods=["POST", "GET"])
def leaveProject():
    left = request.form.get("leave")
    if(left == None):
        left = "[insert name in field above]"

    return """  <div>
                    <form method="POST" action >
                        HW Set: <input type="text" name="leave">
                        <input type="submit"/>
                    </form>
                </div>
                <div>
                    <h1> Leave {} </hi>
                </div>""".format(left)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))
