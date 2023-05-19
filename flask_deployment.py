from flask import Flask

app = Flask(__name__)

@app.route('/')
def sample():
    return 'it is sampled'

@app.route('/new')
def sample2():
    return '<h1>This is a heading</hi>'

app.run(debug=True)
