import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS

with open('model.pkl','rb') as db:
    clf = pickle.load(db)

with open('mood_pred.pkl','rb') as emotions:
    vectorizer, model=pickle.load(emotions)

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

    # 1,155,78,31,0,25.3,0.6777,39
    prediction = clf.predict([X])
    print(prediction)

    message="Diabetic" if prediction else "Non-Diabetic"

    return jsonify({"message": message}), 200

@app.route('/emotions',methods =['POST'])
def emotions():
    request_text = request.get_json()
    # print("Text recieved: ", request_text)

    text=vectorizer.transform([request_text])
    prediction=model.predict(text)

    # print(prediction[0])

    if (prediction[0]==0):
        message='Are you experiencing Sadness..?'
    elif (prediction[0]==1):
        message='Seems joyous and happy'
    elif (prediction[0]==2):
        message='It feels like Love'
    elif (prediction[0]==3):
        message='Are you experiencing Anger?'
    elif (prediction[0]==4):
        message='Comes across as fearful'
    elif (prediction[0]==5):
        message='Surprise'

    return jsonify({"emotion": message}), 200

if __name__ == '__main__':
    app.run(debug=True)