from flask import (
    Blueprint,
    request,
    render_template,
    flash,
    g,
    session,
    redirect,
    url_for
)
from app.MiFlask.forms import SumaForm

prueba = Blueprint('prueba', __name__, url_prefix='/prueba')


@prueba.route('/suma/', methods=['GET', 'POST'])
def suma():
    form = SumaForm(request.form)
    if form.validate_on_submit():
    	pr = form.primero.data
    	seg = form.segundo.data
        rpta = pr + seg
        return str(rpta)

    return render_template("MiFlask/suma.html", form=form)
