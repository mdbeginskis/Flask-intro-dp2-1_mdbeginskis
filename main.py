from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Sveika, pasaule test</h1>'

    @app.route('/about')
    def about():
        return render_template('about.html')

app.run(host='0.0.0.0', port=80, debug=True)