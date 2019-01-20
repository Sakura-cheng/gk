from flask import Flask, render_template, redirect, url_for
from forms import DwfForm
from request import dwf_request

app = Flask(__name__)
app.secret_key = 'secret string'
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route('/', methods=['GET', 'POST'])
def dwf():
    form = DwfForm()
    if form.validate_on_submit():
        data = {
            'score': form.sore.data,
            'kldm': form.category.data
        }
        result = dwf_request(data)
        return render_template('dwf.html', form=form, result=result)
    return render_template('dwf.html', form=form)
