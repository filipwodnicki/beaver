from app import app
from app.forms import WoodcutForm
from flask import render_template, redirect, url_for, request

@app.route('/')
@app.route('/index')
def index():
	form = WoodcutForm()
	return render_template('index.html', form=form)

@app.route('/success', methods=['GET','POST'])
def success():
	material_size = request.form.get('material_size')
	item_list = request.form.get('item_list')
	return render_template( 'success.html', material_size=material_size, item_list=item_list)