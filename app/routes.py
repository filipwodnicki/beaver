import time

from custo import greedy_algorithm
from flask import render_template, jsonify

from app import app
from app.forms import WoodcutForm
from app.woodcut.greedy import chartify


@app.route('/')
@app.route('/index')
def index():
    form = WoodcutForm()
    return render_template('index.html', form=form)

content = ""
with open("README.md", "r") as f:
    content = f.read()

@app.route('/about')
def about():
    return render_template('about.html', text=content)

@app.route('/cut', methods=['post'])
def cut():
    form = WoodcutForm()
    if form.validate_on_submit():
        start = time.time()
        material_size = form.material_size.data
        print( "item list:", form.item_list.data.split(', ') )
        #input is string, which we need to split, convert each element to float and output as a new list
        item_list_of_float = [float(i) for i in form.item_list.data.split(', ')]

        print("item list:", item_list_of_float)
        print("material_size:", material_size)
        response = greedy_algorithm(item_list_of_float, material_size)
        charty = chartify ( response )
        end = time.time()
        elapsed = "Calculation time: " + str( "{0:.6f}".format( end - start ) ) + " seconds."
        return jsonify({ "payload" : str(response), "time" : elapsed, "charty": charty})
    return jsonify({'payload':"Error: couldn\'t submit anything"})
