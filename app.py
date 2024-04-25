from flask import Flask, render_template, request, jsonify
from apps.clean_data import DealData

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

d = DealData()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/clean_data', methods=['GET', 'POST'])
def clean_data():
    return jsonify("Clean data is finish.")


@app.route('/show_EDA_Chart', methods=['GET', 'POST'])
def show_EDA_Chart():
    return jsonify(d.build_chart())


@app.route('/train_data', methods=['GET', 'POST'])
def train_data():
    return jsonify(d.train_data())


@app.route('/forecasts', methods=['GET', 'POST'])
def forecasts():
    predict_X = {
        'temperature': [request.args['temperature']],
        'humidity': [request.args['humidity']],
        'wind_speed': [request.args['wind_speed']],
        'noise_level': [request.args['noise_level']],
        'precipitation': [request.args['precipitation']],
        'solar_radiation': [request.args['solar_radiation']]
    }
    return jsonify(d.forecasts(predict_X))


if __name__ == '__main__':
    app.run()
