from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('CesiumMapBase.html')

@app.route('/DangerMap')
def danger_map():
    return render_template('DangerMapCesiumMap.html')

if __name__ == '__main__':
    app.run(debug=True)
