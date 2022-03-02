from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
df = pd.read_csv('moives.csv')
app = Flask(__name__)
title = df['original_title'].tolist()

@app.route('/getMoive')
def getMoives():
    return jsonify({
        'data':title
    })

if (__name__ == '__main__'):
    app.run(debug=True)