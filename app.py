import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS

with open('model.pkl','rb') as file:
    clf = pickle.load(file)

app = Flask(__name__)
CORS(app) 

@app.route('/',methods=['GET'])
def route():
    return "Hello"

@app.route('/back', methods=['POST'])
def example_route():
    X=[]
    request_data = request.get_json()
    print("Request JSON Object:", request_data)

    for x in request_data:
        data=float(request_data[x])
        X.append(data)

    prediction = clf.predict([X])
    print(prediction)

    message="Diabetic" if prediction else "Non-Diabetic"

    return jsonify({"message": message}), 200

if __name__ == '__main__':
    app.run(debug=True)