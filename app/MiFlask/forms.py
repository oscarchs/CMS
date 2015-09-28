from flask.ext.wtf import Form 
from wtforms import IntegerField


class SumaForm(Form):
    primero    = IntegerField('Numero 1')
    segundo = IntegerField('Numero 2')
