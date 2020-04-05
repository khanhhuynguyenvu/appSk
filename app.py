from flask import Flask, jsonify, Response
from sklearn import datasets, svm
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)

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

@app.route('/b')
def genList():
	arr = np.arange(int(1e6))
	return ", ".join(map(str,arr))

@app.route('/post/<int:postId>')
def getPostId(postId):
	return "Post Id %" + str(postId)

@app.route('/get/<int:idx>')
def getNum(idx):
	return jsonify(value=idx), 200

