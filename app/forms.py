from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired

class WoodcutForm(FlaskForm):
	material_size = FloatField('board size', validators=[DataRequired()], default=2050.0)
	item_list = StringField('list of pieces you need (comma separated please!)', validators=[DataRequired()], default='450, 444, 436, 430, 389, 389, 386, 375, 362, 362, 261, 261, 261')
	submit = SubmitField('Calculate')

	# make custom validator that makes sure we have a list of integers or floats in item_list