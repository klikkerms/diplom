


# from flask import Flask, render_template, request
# from leva import autocorrect, ct
# import jinja2
# jinja_environment = jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader('templates'))
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/', methods=['POST'])
# def correct_text():
#     user_input = request.form['user_input']
#     corrected_text = ct(user_input)
#     return render_template('index.html', user_input=user_input, corrected_text=corrected_text)
#
# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request


from leva import autocorrect, ct
import jinja2
from playing_with_model import cap


jinja_environment = jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader('templates'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def correct_text():
    user_input = request.form['user_input']
    corrected_text = ct(user_input)
    upper = cap(corrected_text)
    return render_template('index.html', user_input=user_input, corrected_text=corrected_text, upper=upper)


if __name__ == '__main__':
    app.run(debug=True)


