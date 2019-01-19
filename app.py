from flask import Flask, render_template
from forms import DwfForm

app = Flask(__name__)
app.secret_key = 'secret string'
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route('/', methods=['GET', 'POST'])
def dwf():
    form = DwfForm()
    print(form.category)
    return render_template('dwf.html', form=form)
