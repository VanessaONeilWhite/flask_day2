from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PokemonForm(FlaskForm):
    pokename= StringField('Enter a Pokemon', validators = [DataRequired()])
    submit = SubmitField('Submit')
