from flask import Flask, render_template, request, redirect, url_for

# dummy data for now
raters = ['', 'Alice', 'Bob', 'Cindy', 'David']
sites = ['', 'Bliss', 'Drum', 'JBLM']
maltreatment_types = ['', 'Child Physical', 'Child Sexual', 'Child Emotional', 'Child Neglect', 'Partner Physical', 'Partner Sexual', 'Partner Emotional', 'Partner Neglect']

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic_info():
    return render_template('basic_info.html', raters=raters, sites=sites)

@app.route('/maltreatment-category')
def maltreatment_category():
    return render_template('maltreatement_category.html', maltreatment_types=maltreatment_types)

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')


@app.route('/medical-form')
def medical_form():
    return render_template('medical_form.html')

@app.route('/housekeeping')
def housekeeping():
    return render_template('housekeeping.html')


if __name__ == '__main__':
    app.run(debug=True)