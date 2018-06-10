import flask
import six
from flask import Flask, request, jsonify, redirect, url_for, render_template, abort, make_response
from flask_restful import Resource, Api
# from sqlalchemy import create_engine
from json import dumps
# from flask import Flask, jsonify
import os


# # db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

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

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'status': 'failure', 'reason' :'bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({}), 404)


@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_tasks(product_id):
	products = [products for products in prods if products['id'] == product_id]
	if len(products) == 0:
		abort(404)
	return jsonify({'data': products[0]})

@app.route('/api/products', methods=['POST'])
def create_task():
    if not request.json or 'name' not in request.json:
        abort(400)
    prod_return = {
        'id': 1,
    }
    return jsonify({'data': make_public_task(task)}), 201

@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_task(product_id):
    prod = [prod for prod in prods if prod['id'] == product_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    # if 'title' in request.json and \
    #         not isinstance(request.json['title'], six.string_types):
    #     abort(400)
    # if 'description' in request.json and \
    #         not isinstance(request.json['description'], six.string_types):
    #     abort(400)
    # if 'done' in request.json and type(request.json['done']) is not bool:
    #     abort(400)
    
    return jsonify({'status': 'success'})


@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_task(product_id):
    prod = [prod for prod in prods if prod['id'] == product_id]
    if len(prod) == 0:
        abort(404)
    return jsonify({'result': True})
# # if __name__ == '__main__':
# #      app.run(port='80')



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)