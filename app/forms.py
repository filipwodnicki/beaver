from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired

class WoodcutForm(FlaskForm):
	material_size = FloatField('Material Size', validators=[DataRequired()], default=2050.0)
	item_list = StringField('Pieces you need', validators=[DataRequired()], default='450, 444, 436, 430, 389, 389, 386, 375, 362, 362, 261, 261, 261')
	submit = SubmitField('Calculate')

	# make custom validator that makes sure we have a list of integers or floats in item_list