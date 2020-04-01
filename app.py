from flask import Flask, jsonify
from sklearn import datasets, svm

app = Flask(__name__)

# Load Dataset from scikit-learn.
digits = datasets.load_digits()

@app.route('/p')
def hello():
    clf = svm.SVC(gamma=0.001, C=100.)
    clf.fit(digits.data[:-1], digits.target[:-1])
    prediction = clf.predict(digits.data[-1:])

    return jsonify({'prediction': repr(prediction)})

@app.route('/')
def index():
	return "Hi"
