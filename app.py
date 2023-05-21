import pickle
with open('forecast_model.pckl', 'rb') as fin:
    m2 = pickle.load(fin)

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)
@app.route("/katana-ml/api/v1.0/forecast/ironsteel", methods=['POST'])
def predict():
   
    ret = "Joan"
    
    return ret
# running REST interface, port=3000 for direct test
if __name__ == "__main__":
    app.run()