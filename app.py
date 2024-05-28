from flask import Flask, jsonify, abort, make_response, request
import numpy as np
import engine_model as EngineModel
import tire_model as TireModel

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    return '<h2>ML App - Dump Truck Diagnostics</h2>'

@app.route('/engine/predict', methods=['GET'])
def engine_predict():
    result = EngineModel.launch_task(request.args.get('rpm'), request.args.get('temperature'), \
                        request.args.get('pressure'), request.args.get('vibration'), 
                        request.args.get('fuel'), request.args.get('speed'),
                        request.args.get('load'),'v1.0')
	
    return make_response(jsonify(result), 200)


@app.route('/tire/predict', methods=['POST'])
def tire_predict():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    
    prediction = TireModel.model.predict(features)
    
    return jsonify({'prediction': prediction[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'code': 'PAGE_NOT_FOUND'}), 404)

@app.errorhandler(500)
def server_error(error):
    return make_response(jsonify({'code': 'INTERNAL_SERVER_ERROR'}), 500)


if __name__ == '__main__':
    app.run(port=5055, debug=True)