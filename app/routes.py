from app import app
from app.forms import WoodcutForm
from app.woodcut.algorithms.greedy import greedy_algorithm
from flask import render_template, redirect, url_for, request, jsonify

@app.route('/')
@app.route('/index')
def index():
	form = WoodcutForm()
	return render_template('index.html', form=form)

# @app.route('/success', methods=['GET','POST'])
# def success():
# 	material_size = request.form.get('material_size')
# 	item_list = request.form.get('item_list')
# 	return render_template( 'success.html', material_size=material_size, item_list=item_list)

@app.route('/cut', methods=['POST'])
def cut():
	material_size = request.form.get('material_size')
	item_string = request.form.get('item_list')
	item_list_of_string = item_string.split(',')
	item_list_of_float = [float(i) for i in item_list_of_string]
	# print(item_list_of_float)

	statement = ""
	for board in greedy_algorithm(item_list_of_float):
		statement += str( board )
	print ( statement )
	return jsonify( { "data" : statement } )
	# return "Not yet ;)"