from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class GrandmaForm(Form):
  user_input = StringField('Speak to Grandma:', validators=[Required()])
  submit = SubmitField('Submit')
