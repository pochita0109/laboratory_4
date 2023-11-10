from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/contact')
def contact():
    return render_template('contacts.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)


@app.route('/circle_area', methods=['GET', 'POST'])
def circle_area():
    result = None
    if request.method == 'POST':
        radius = request.form.get('radius', '')
        result = 3.14*(int(radius)**2)
    return render_template('circle_area.html', result=result)

@app.route('/triangle_area', methods=['GET','POST'])
def triangle_area():
    result= None
    if request.method == 'POST':
        base = float(request.form.get('base',''))
        height = float(request.form.get('height',''))
        result = 0.5 * base * height
    return render_template('triangle_area.html',result=result)

if __name__ == "__main__":
    app.run(debug=True)
