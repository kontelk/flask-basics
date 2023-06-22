from flask import Flask, jsonify, request


app = Flask(__name__)

# 127.0.0.1:5000/
@app.route('/')
def hello_world():
    retJson = {
        'Name':'John',
        'Age':24,
        'phones':[
            {
                'phoneName':'Iphone8',
                'phoneNumber':11111
            },
            {
                'phoneName':'Nokia',
                'phoneNumber':11121
            }
        ]
    }
    return jsonify(retJson)

@app.route('/add_two_nums', methods=["POST"])
def add_two_nums():
    # Get x,y from the posted data
    dataDict = request.get_json()
    if "x" not in dataDict:
        return "Error: value for x is missing!", 305
    if "y" not in dataDict:
        return "Error: value for y is missing!", 305
    x = dataDict["x"]
    y = dataDict["y"]
    # Add z = x + y
    z = x + y
    # Prepare a JSON, "z":z
    retJSON = {
        "z":z
    }
    # Return jsonify(map_prepared)
    return jsonify(retJSON), 200

if __name__=="__main__":
    app.run(debug=True)
    # app.run()
    # app.run(host='127.0.0.1',port=8080)
    

