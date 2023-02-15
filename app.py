from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        value = float(request.form['value'])

        # Convert units
        result = convert(from_unit, to_unit, value)

        # Return result
        return render_template('index.html', result=result)
    else:
        # Return form
        return render_template('index.html')


def convert(from_unit, to_unit, value):
    # Add your conversion logic here
    # For example: miles to kilometers
    if from_unit == 'mi' and to_unit == 'km':
        return value * 1.60934
    else:
        return value


if __name__ == '__main__':
    app.run()
