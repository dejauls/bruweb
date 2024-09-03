from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/acian')
def acian():
    return render_template('acian.html')

@app.route('/acianbeton')
def acianbeton():
    return render_template('acianbeton.html')

@app.route('/betoninstan')
def betoninstan():
    return render_template('betoninstan.html')

@app.route('/perata')
def perata():
    return render_template('perata.html')

@app.route('/plester')
def plester():
    return render_template('plester.html')

@app.route('/pasanganbata')
def plesterbata():
    return render_template('plesterbata.html')

@app.route('/render')
def render():
    return render_template('render.html')

@app.route('/thinbed')
def thinded():
    return render_template('thinbed.html')

@app.route('/tile')
def tile():
    return render_template('tile.html')

@app.route('/tileontile')
def tileontile():
    return render_template('tileontile.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8989')