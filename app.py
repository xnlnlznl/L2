from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def hello_world():
    # return 'Hello World!'
    _title = '恭喜XXX'
    # return render_template('1.html', name=name)
    return render_template('L.html', _title=_title)

@app.route('/1')
def test():
    return render_template('1.html')

if __name__ == '__main__':
    app.run(static_folder="../static")
