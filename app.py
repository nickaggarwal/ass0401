# Note-  Flask has been used for implementing my API as the source code language I know in python


import flask
import six
from flask import Flask, request, jsonify, redirect, url_for, render_template, abort, make_response
from flask_restful import Resource, Api
from json import dumps
import os


# # db_connect = create_engine('sqlite:///chinook.db')
# setting up the FLASK API using flask_restful library 
app = Flask(__name__)
api = Api(app)

# this is my predefined dataset with two products as of now.
prods = [
    {
    	'id': 1,
        'name':u'Buy groceries',
        'category_name':'',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'buy_price':'',
        'sell_price':'',
        'quantity':'',
    },
    {
    	'id': 2,
        'name':u'Learn Python',
        'category_name':'',
        'description': u'Need to find a good Python tutorial on the web',
        'buy_price':'',
        'sell_price':'',
        'quantity':'',
    }
]

# error handling mechanism using flask_restful for BAD request errors
@app.errorhandler(400)
def bad_request(error):
	# the response in case of such an error
    return make_response(jsonify({'status': 'failure', 'reason' :'bad request'}), 400)

# error handling mechanism using flask_restful for Page not found errors
@app.errorhandler(404)
def not_found(error):
	# the response in case of such an error
    return make_response(jsonify({}), 404)

#the GET request mechanism using flask_restful, app route contains the path given on the url, method is GET
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_tasks(product_id):
	#error handling for 404 type errors
	products = [products for products in prods if products['id'] == product_id]
	if len(products) == 0:
		abort(404)
	return jsonify({'data': products[0]})

#the POST request mechanism using flask_restful, app route contains the path given on the url, method is POST
@app.route('/api/products', methods=['POST'])
def create_task():
	#error handling for 400 type errors
    if not request.json or 'name' not in request.json:
        abort(400)
    prod_return = {
        'id': 1,
    }
    return jsonify({'data': make_public_task(task)}), 201

#the POST request mechanism using flask_restful, app route contains the path given on the url, method is POST
@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_task(product_id):
	# error handling for 404 and 400 type errors
    prod = [prod for prod in prods if prod['id'] == product_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    
    return jsonify({'status': 'success'})

#the DELETE request mechanism using flask_restful, app route contains the path given on the url, method is DELETE
@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_task(product_id):
    prod = [prod for prod in prods if prod['id'] == product_id]
    if len(prod) == 0:
        abort(404)
    return jsonify({'result': True})
# # if __name__ == '__main__':
# #      app.run(port='80')


#command to run the API on the given host and port
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)