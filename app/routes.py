from app.woodcut.algorithms.greedy import greedy_algorithm
from flask import render_template, redirect, url_for, jsonify
from app import app
from app.forms import WoodcutForm
import time

@app.route('/')
@app.route('/index')
def index():
	form = WoodcutForm()
	return render_template('index.html', form=form)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/cut', methods=['post'])
def cut():
	form = WoodcutForm()
	if form.validate_on_submit():
		start = time.time()
		material_size = form.material_size.data
		#input is string, which we need to split, convert each element to float and output as a new list
		item_list_of_float = [float(i) for i in form.item_list.data.split(',')] 
		response = greedy_algorithm(item_list_of_float)
		end = time.time()
		elapsed = "Calculation time: " + str( "{0:.6f}".format( end - start ) ) + " seconds."
		return jsonify({ "payload" : response, "time" : elapsed })
	return jsonify({'payload':"Error: couldn\'t submit anything"})