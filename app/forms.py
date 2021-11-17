from flask_wtf import FlaskForm
from wtforms import StringField, Form
from wtforms.validators import DataRequired

#formação do formulário para html:
class SearchForm(Form):
  search = StringField('search')