from app.woodcut.algorithms.greedy import greedy_algorithm
from flask import render_template, redirect, url_for, flash, jsonify
from app import app
from app.forms import WoodcutForm

@app.route('/')
@app.route('/index')
def index():
	form = WoodcutForm()
	return render_template('index.html', form=form)

@app.route('/cut', methods=['post'])
def cut():
	form = WoodcutForm()
	if form.validate_on_submit():
		material_size = form.material_size.data
		item_string = form.item_list.data
		item_list_of_string = item_string.split(',')
		item_list_of_float = [float(i) for i in item_list_of_string]
		statement = ""
		for board in greedy_algorithm(item_list_of_float):
			statement += str( board )
		print ( statement )
		return jsonify({ "payload" : statement })
	return jsonify({'payload':"couldn\'t submit anything"})