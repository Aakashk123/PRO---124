
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

List = {
        {
            "id" : 1,
            "Contact": 9987644456,
            "Name": "Raju",
            "done":False
        },
        {
            "id" : 2,
            "Contact": 9999112262,
            "Name": "Kaju",
            "done":False
        },
}


@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    List.append(contact)
    return jsonify({
        "status":"success",
        "message": "Contact added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : List
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)
